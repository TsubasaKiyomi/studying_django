##### API で遊ぶ

対話シェルを起動しコマンドを入力する。

```
python3 manage.py shell
```

- なぜ単なる「python3」での起動ではないのか？
  manage.py が DJANGO_SETTINGS_MODULE 環境変数を設定してくれる。これにより、 Django に mysite/settings.py ファイルへの import パスが与えられる。

対話の流れ

```
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.#モデルクラスをインポートする

# No questions are in the system yet.(システムに質問がないので入力していく。)
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
#新しい質問を作成する
# Support for time zones is enabled in the default settings file, so
#タイムゾーンのサポートはデフォルト設定ファイルで有効になっている
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
#Djangoはpubinfoのtzinfoで日時を期待します。 timezone.now（）を使用します
# instead of datetime.datetime.now() and it will do the right thing.
#datetime.datetime.now（）の代わりに、それは正しいことを行います。
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
#オブジェクトをデータベースに保存します。 save（）を明示的に呼び出す必要があります。
>>> q.save()

# Now it has an ID.
#現在はIDを持っています。
>>> q.id
1

# Access model field values via Python attributes.
#Python属性を介してモデルフィールド値にアクセスする
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
# 属性を変更してから値を変更し、次にsave（）を呼び出します。
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
# objects.all（）は、データベース内のすべての質問を表示します。
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

<QuerySet [<Question: Question object (1)>]>はオブジェクトの表現として成り立たない。
**str**() メソッドを Question と Choice の両方に追加する。

polls/models.py

```
from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```

モデルクラスにクラスメソッドを追加する。

polls/models.py

```
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

- import datetime と from django.utils import timezone 　を追記。標準モジュール datetime と django のタイムゾーン関連ユーティリティの django.utils.timezone を参照するため。

```
python3 manage.py shell
```

```
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
#__str __（）オプションが機能していることを確認

>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# Djangoは、以下によって完全に駆動される豊富なデータベース検索APIを提供します
# keyword arguments.
# キーワード引数。
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
# 今年発行された質問を取得します。
>>> from django.utils import timezone
# django.utilsからインポートタイムゾーン
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
# 存在しないIDをリクエストすると、例外が発生します。
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# 主キーによるルックアップが最も一般的なケースなので、Djangoは
# shortcut for primary-key exact lookups.
# 主キーの正確な検索のショートカット
# The following is identical to Question.objects.get(id=1).
# 以下はQuestion.objects.get（id = 1）と同じです。
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
# カスタムメソッドが機能することを確認します。
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# 質問にいくつかの選択肢を与えます。 create呼び出しは、新しい
# Choice object, does the INSERT statement, adds the choice to the set
# 選択肢オブジェクトは、INSERTステートメントを実行して、選択肢をセットに追加します
# of available choices and returns the new Choice object. Django creates
# 利用可能な選択肢の1つであり、新しいChoiceオブジェクトを返します。
# a set to hold the "other side" of a ForeignKey relation
# ForeignKeyリレーションの「反対側」を保持するセット
# (e.g. a question's choice) which can be accessed via the API.
# （例：質問の選択）API経由でアクセスできます。
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
# 関連するオブジェクトセットの選択肢を表示します-これまでのところはありません。
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
# 3つの選択肢を作成します
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
# 選択オブジェクトには、関連する質問オブジェクトへのAPIアクセスがあります。
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
# 逆も同様です。質問オブジェクトは選択肢オブジェクトにアクセスできます。
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# APIは必要に応じて自動的に関係を追跡します。
# Use double underscores to separate relationships.
# 二重のアンダースコアを使用して関係を分離します。
# This works as many levels deep as you want; there's no limit.
# これは、必要なだけ多くのレベルで機能します。制限はありません。
# Find all Choices for any question whose pub_date is in this year
# 今年がpub_dateである質問のすべての選択肢を検索します
# (reusing the 'current_year' variable we created above).
# （上記で作成した「current_year」変数を再利用します）
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
# 選択肢の1つを削除しましょう。そのためには、delete（）を使用します。
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```
