##### はじめてのビュー作成　

###### view とは

- viwe.py にビューを書き URL と対応付ける
- view は表示させたいページを決定する処理をしている。
- リクエストをもとに表示させたいページを決定している。
- 関数、クラスで実装されている view もある。

###### view の書き方

viwe.py にビューのコードを書く

```
from django.http import HttpResponse


def index(request):
<!-- return HttpResponse("実際にブラウザ上に表示される") -->
    return HttpResponse("Hello, world. You're at the polls index.")
```

###### URLconf を作成し対応付けする

- poll ディレクトリに URLconf を作成するために urls.py をファイルを作成する。

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

polls/urls.py にコードを入力

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

mysite/urls.py にコードを入力
URLconf に polls.urls モジュール の記述を反映させる。

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

###### HttpResponse とは？

import 　 HttpResponse はページなどに関するサーバーからの返信のこと

django で最も単純なビューができた。
view だけでは動かない。URL を対応付けする必要がある。そのために URLconf が必要。

###### URL URLconf とは？　 URL ディスパッチャとは？

###### URL とは？

URL はブラウザ上で表示される「https://www.・・・・」の「一意に示すもの」

- 一意・一つしか無い、オンリーワン、ユニークとも呼ばれる。

###### URLconf とは？

url ディスパッチャの動作を行う設定ファイルのこと。
URLconf = urls.py ここに書くことが決まっている。

###### URL ディスパッチャとは？

- URL に応じてどんなページを表示させるか決定する通信指令係(dispatcher)のようなもの django には初めから備わっている。
- サイト管理者が設定した URL をユーザーに返す処理をしている。

- polls ディレクトリに urls.py というファイルを作る。
  urls.py にコードを入力する。

###### include()とは

直訳：含める
includ()関数は他の URLconf への参照することができる。Django が include()に遭遇するとポイントまでに一致した URL の部分を切り落とし、次の処理のために残りの文字列をインクルードされた URLconf へ渡す。
polls は独自の URLconf を持っているので、どんなパスルート下にも置ける。
