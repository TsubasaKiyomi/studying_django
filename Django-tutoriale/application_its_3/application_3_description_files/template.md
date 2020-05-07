##### テンプレートシステムを使う

template では主に HTML を使って表示するページを作る。

polls/templates/polls/detail.html にコードを追記

```
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

テンプレートシステムは変数の属性にアクセスするためにドット検索の構文を使用。{{ question.question_text }}を例にすると、はじめに question オブジェクトに辞書検索を行う。それに失敗すると、今度は属性として検索し、このケースは成功する。もし属性検索に失敗すると、リストインデックスでの検索を行う。

メソッドの呼び出しは{% for %}ループの中で行われる。question.choice_set.all は、question.choice_set.all() と解釈され、その結果、Choice オブジェクトからなるイテレーション可能オブジェクトを返すし{% for %}タグで使えるようになる。

###### イテレーション

反復、繰り返し

###### ハードコード

ハードコードとは、ソフトウェア開発の際に、特定の動作環境を決め打ちして、その環境を前提とした処理やデータをソースコードの中に直に記述すること。

###### なぜハードコードはダメなのか？

・「何の値なのか分からなくなるから」
・１箇所の変更で、何箇所もプログラムの変更をする必要が出るから。（保守性）

###### ハードコードされた URL を削除

polls/index.html テンプレートで質問へのリンクを買いた時、リンクは一部は次のようにハードコードされていた。

ハードコード

```
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

このハードコードされた、密結合のアプローチの問題は、プロジェクトにテンプレートが多数ある場合、URL の変更が困難になってしまう。polls.urls モジュール の path() 関数で name 引数を定義したので、テンプレートタグの {％url％} を使用して、URL 設定で定義されている特定の URL パスへの依存をなくすことができる

{％url％} を使って削除

```
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

これが機能するのは、polls.urls モジュールに指定された URL の定義を検索するから。 'detail' の URL 名は以下の箇所で定義されている。

```
{％url％}テンプレートタグによって呼び出される 'name'値
path('<int:question_id>/', views.detail, name='detail'),
```

投票の詳細ビューの URL を変更したい場合、たとえば polls/specifics/12/ のように変更したいとき、対象となるテンプレートを変更する代わりに、 polls/urls.py を変更。

```
「'specifics'仕様」という単語を追加
path('specifics/<int:question_id>/', views.detail, name='detail'),
```

###### URL 名前空間

django で今作成しているアプリは polls だけだが、実際はもっと 10,20 個も django でアプリ作成するかもしれない。そんな時 django はどうやってアプリの URL を区別しているのか？それは URLconf に名前空間を追加する事で、区別している。

名前空間を設定する。
polls/urls.py ファイル内で app_name を追加し、アプリケーションの名前空間を設定する。
polls/urls.py

```
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

polls/templates/polls/index.html のテンプレートを変更する

```
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

```

上記から以下の形にし名前空間つきの詳細ビューを指すようにする。

```
名前空間つきの詳細ビューを指すように
```
