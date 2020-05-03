##### path()関数

- path()関数は４つの引数を受け取ることができる。
- route と view の２つは必須の引数
- kwargs と name の２は省略可能な引数

###### path()引数：route

route は URL をパターンを含む文字列のこと。リクエスト処理の時に django は urlpatteerns を開始し要求されたパターンと一致するものを見つけるまでパターン比較する。
パターンは GET や POST のパラメーター、ドメイン名は検索しない。

```
例え
https://www.example.com/myapp/ へのリクエストにおいては、URLconfはmyapp/ を見る。
https://www.example.com/myapp/?page=3 へのリクエストにおいても、URLconfはmyapp/を見る
```

###### urlpatteerns

- urlpatteerns はユーザーが指定した URL （http://www.xxxxxxx.jp/index/）と urlpatteerns に格納した全ての path()の初めの引数（'admin/'や'index/'）を順番に比較する
- URL と引数が一致した場合に path()の 2 つ目の引数(admin.site.urls,include())を利用する。
- アプリケーションを追加する時だけ新しい path()を追加する。

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('myapp.urls', namespace='myapp')),
]
```

###### pth()引数:bview

django がマッチする正規表現を見つけると、django は指定されたビュー関数を呼び出す。その際、HttpRequest オブジェクトを第一引数に、キーワード引数として route から「キャプチャされた」値を呼び出す。

###### pth()引数:kwargs

任意のキーワード引数を”辞書”として対象のビューに渡せる。

###### pth()引数:name

URL に名前付けをしておくと django のどこからでも参照できる。
プロジェクトの URL にグローバルな変更を加える場合にも 1 つのファイルを変更するだけで済むようになる。
