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
