#### Shortcut

##### ショートカット：render()

テンプレートをロードしてコンテキストに値を入れ、テンプレートをレンダリングした結果を HttpResponse オブジェクトで返す、イディオムはよく使われる。

###### context コンテキスト

コンテキストは辞書型のデータ

###### イディオム

二、三の語が結びついて、原義とは幾分違った特殊な意味を持つ、習慣的な言いまわし

###### レンダリング

「ある情報を形を変えて表現する事」
レンダリングにはいろんな種類がある。
Djamgo では多くの情報を整理して表現する仕組み

polls/views.py を書き換える

```
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

404 エラーの送出

```
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

- リクエストした ID を持つ質問がない時に Http404 を返す。

###### ショートカット:degt_object_or_404()

get()を実行し、オブジェクトが存在しない場合は Http404 を送出するイディオムはよく使われる。
このためのショートカットを使って detail()ビューを書き換える。

polls/views.pyを書き換える
```
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```
