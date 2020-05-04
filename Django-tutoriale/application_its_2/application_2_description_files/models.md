##### モデルの作成

- モデルはデータベースのレイアウトとそれに付随するメタデータ。

- メタデータとは
  本体であるデータに関する付帯情報が記載されたデータ。
  データについてのデータ

###### polls アプリケーション

polls アプリケーションには Question と Choice の２つのモデルを作成する。
polls には question と publication date の情報がある。
Choice には選択肢のテキストと vote の２つのフィールドがある。
各 Choice は１つの Question に関連づけられる。

django では python クラスで表現できる。
polls/models.py

```
from django.db import models


class Question(models.Model):

    #CharFieldには必ず(max_length)と入力する
    question_text = models.CharField(max_length=200)

    #Question.pub_dateは人間可読なフィールド名を指定('date published')
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

- 各モデルは１つのクラスで表現され、いずれも django.db.models.Model のサブクラス。
- 各モデルには複数のクラス変数があり、個々のクラス変数はモデルのデータベースフィールドを表現している。

* 各フィールドは Field クラスのインスタンスとして表現されている。文字フィールドは CharField、日時フィールドは DataTimeField
  クラスは各フィールドにどのようなデータ型を記憶させるかを Django に教える。

###### field フィールドとは？

- model の属性の一つ
- 保存したいデータを表すためのデータの入れ物のようなもの。django に最初から用意されている。

###### model モデルとは？

アプリケーションのデータを保存するもの。
モデルはデータに関する情報源。データが必要とするフィールドとその動作を定義する。

- Field の最初の位置引数には、オプションとして人間可読なフィールド名も指定でき、このフィールド名は Django の二つの内省機能で使う他、ドキュメントとしての役割も果たす。人間可読なフィールド名を指定しない場合、 Django は機械可読な名前を使う。上の例では、 Question.pub_date にだけ人間可読なフィールド名を指定した。モデルの他のフィールドでは、フィールドの機械可読な名前は人間可読な名前としても十分なので定義していない。

* Field クラスの中には必須の引数を持つものがありま す。例えば CharField には max_length を指定する必要があります。この引数はデータベーススキーマで使われる他、後で述べるバリデーションでも使われます。

###### バリデーションとは？

Form の値が正しいかどうか確かめて、誤っていた場合 Form 送信後の処理の実行そ中止する機能。

- ForeignKey を使用してリレーションシップが定義されていることに注目。それぞれの Choice が一つの Question に関連付けられることを Django に伝える。 Django は 多対一(many-to-one)、多対多(many-to-many)、そして一対一(one-to-one)のような一般的なデータベースリレーションシップすべてをサポート。

###### リレーションシップ

直訳：関係、繋がり、関連

###### ForeignKey

外部キー

##### モデルを有効にする

わずかなコードを書くだけでたくさんの情報を知れる。

- アプリケーションのデータスキーマを作成(CREATE TABLE 文を実行)できる
- Question や Choice オブジェクトに Python からアクセスするためのデータベース API を作成できる。
  API（Application Programming Interface）

アプリケーションをプロジェクトに含めるには、構成クラスへ参照を INSTALLED_APPS 設定に追加する必要がある。
INSTALLED_APPS 設定（インストール済みアプリ）

- mysite/settings.py にある INSTALLED_APPS に'polls.apps.PollsConfig' を追記する。

```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

'polls.apps.PollsConfig'を追記したことで、django が polls アプリを認識する。

```
python manage.py makemigrations polls
```

結果

```
igrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

- python manage.py makemigrations polls を実行することで Django にモデルに変更があったこと(この場合、新しいものを作成)を伝え、そして変更を マイグレーション の形で保存することができた。
- マイグレーションは Django がモデル（データベーススキーマ）の変更を保存する方法。
- マイグレーションはディスク上のただのファイル。

django にはマイグレーションを代わりに実行し、自動でデータベーススキーマを管理するためのコマンドがある。
sqlmigrate コマンドはマイグレーションの名前を引数にとって SQL を返す。

sqlmigrate(SQL の移行)

```

python manage.py sqlmigrate polls 0001

```

結果

```
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```

上記は PostgreSQL の場合のみ生成。

###### PostgreSQL とは？

PostgreSQL(ポストグレスキューエル)はオープンソースのリレーショナルデータベース管理システム(RDBMS)
データベースは簡単にいうと「箱」の集まり。
リレーショナルデータベース(RDB)はその箱をテーブルのセット、表形式で持ち、１つの箱（＝表）に入ったデータを別の箱のデータと関連づけることで、複雑なデータや大規模なデータを柔軟に取り扱うことができる。RDBMS は RDB をコンピュータ上で操作できるようにした管理システム。

- sqlmigrate コマンドは実際にはデータベースにマイグレーションを実行しない。ただ、Django が必要としている SQL が何であるかをスクリーンに表示するだけ。

python manage.py migrate を実行してモデルのテーブルをデータベースに作成する。

```
python manage.py migrate
```

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
```

- migrate のコマンドは全ての適用されていないマイグレーションを補足しデータベースに対して実行する。モデルに対して行った変更はデータベースのスキーマに同期する。

- マイグレーションは強力なツールで、プロジェクトの発展に合わせて、モデルを変更し続ける事ができる。

- モデルの変更を実施するための３ステップ

```
・モデルを変更する(models.pyの中の)
・変更のためのマイグレーションを作成するためにpyrhon manage.py makemigrationsを実行する。
・データベースにこれらの変更を適用するためにpython manage.py migrateを実行
```
