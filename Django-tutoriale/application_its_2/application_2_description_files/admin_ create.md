##### admin 作成

###### 管理ユーザーを作成する

admin サイトにログインできるユーザーを作成する必要がある。

コマンドを実行

```
python3 manage.py createsuperuser
```

ユーザー名
email アドレス
パスワード
を入力する

###### 開発サーバーの起動

起動するためにコマンドを入力

```
python3 manage.py runserver
```

結果

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 05, 2020 - 00:28:42
Django version 3.0.5, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/admin/
Quit the server with CONTROL-C.
```

- http://127.0.0.1:8000/にadmin/をつけてブラウザに移行する。

移行するとブラウザ上でユーザー名とパスワードの入力を促される。

- admin サイトに入る
  ユーザー名とパスワードの入力しログインすると django のインデックスページが表示される。

###### poll アプリを admin 上で編集できるようにする。

polls アプリが表示されるように polls/admin.py を編集する。

```
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
- 編集後にブラウザ上で更新をするとPOLLSが表記される。

- "What's up?" questionを編集する。
フォームはQuestionモデルから自動的に生成される。
モデルのフィールドの型 (DateTimeField 、 CharField など) はそれぞれ異なる HTML 入力ウィジェットと対応している。

ページの末尾の部分には操作ボタンがいくつか表示されている。

保存 (Save) – 変更を保存して、このモデルのチェンジリストのページに戻る。
保存して編集を続ける (Save and continue editing) – 変更を保存して、このオブジェクトの編集ページをリロードする。
保存してもう一つ追加 (Save and add another) – 変更を保存して、このモデルのオブジェクトを新規追加するための空の編集ページをロードする。
削除 (Delete) – 削除確認ページを表示する。


「履歴 (History)」を開くと変更した時刻と変更したユーザー名が表記される。