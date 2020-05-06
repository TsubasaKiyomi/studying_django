##### Overview

###### ビューとは

Django のアプリケーションに置いて特定の機能を提供するウェブページの「型（type）」であり、各々のテンプレートを持っている。
例え：ブログアプリケーションなら

- Blog ホームページ　-　最新エントリーをいくつか表示
- エントリー詳細ページ - 1 エントリーへのパーマリンク(permalink)ページ
- 年ごとのアーカイブページ - 指定された年のエントリーの月を全て表示
- 月ごとのアーカイブページ - 指定された月のエントリーの日を全て表示
- 日ごとのアーカイブページ - 指定された日の全てのエントリーを表示
- コメント投稿 - エントリーに対するコメントの投稿を受付

投票アプリケーションは以下４つのビューを作成。

- 質問"インデックス"ページ -- 最新の質問をいくつか表示
- 質問"詳細"ページ -- 結果を表示せず、質問テキストと投票フォームを表示
- 質問"結果"ページ -- 特定の質問の結果を表示
- 投票ページ -- 特定の質問の選択を投票として受付

django はウェブページとコンテンツはビューによって提供。

###### もっとビューを書いてみる

polls/views.py に新しい view を追記

```
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

polls/urls.py に以下を追記。新しい view とモジュールを結びつける

```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

```
python3 manage.py runserver
```

を入力しブラウザに移行するhttp://127.0.0.1:8000/

ブラウザで"/polls/34/"を表示すると You're looking at question 34.と表示される。polls/views.py に新しい view を追記したものが表示されている。（"/polls/34/results/" "polls/34/vote/"も表示される）

```
http://127.0.0.1:8000//polls/34/
You're looking at question 34.


http://127.0.0.1:8000//polls/34/results/"
You're looking at the results of question 34.


http://127.0.0.1:8000//polls/34/vote/
You're voting on question 34.
```

###### 動作するビューを書く

各ビューには２つの役割がある

- リクエストされたページのコンテンツを含む HttpResponse オブジェクトを返す事
- Http404 などの例外の送出。それ以外の処理はユーザー次第。
  Django にとって必要なのは HttpResponse か例外か。

polls/views.py に index()ビューを作成する。
システム上にある最新の５件の質問項目をカンマで区切り、日付順に表示させる。

```
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```

- 上記ではビューの中でページデザインがハードコードされているので、ページの見栄えを変更するたびに python コードを編集する必要が出てくる。templates ディレクトリを作成しデザインを分離させる。

- templates ディレクトリ内で polls というディレクトリを作成し、さらにその中に index.html というファイルを作成。

index.html にコードを入力すしテンプレートを作成する。

```
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

テンプレートを使用するために polls/views.py の index ビューを更新する。

```
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```
 polls/index.html というテンプレートをロードし、そこにコンテキストを渡す。コンテキストは、テンプレート変数名を Python オブジェクトにマッピングする辞書。

ブラウザでhttp://127.0.0.1:8000/polls/
を開くと箇条書きのリストが表示される。("What's up"が表示)

