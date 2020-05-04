##### Database の設定

- mysite/settings.py は django の設定を表現するモジュールレベルの変数がある場所(python モジュール)
- デフォルトでは SQLite を使用する。SQLite は python に標準組み込みされている。

SQLite 以外を使う場合適切な データベースのバインディング をインストールして、設定ファイルの DATABASES の 'default' 項目内を以下のキーを変更する。

```
・ENGINE -- 'django.db.backends.sqlite3'、 'django.db.backends.postgresql'、
'django.db.backends.mysql' または 'django.db.backends.oracle'にする
```

###### データバインディングとは

データと対象を結びつけ、データあるいは対象の変更を反映すること。

デフォルトでは、 INSTALLED_APPS には以下のアプリケーションが入っている。

```
django.contrib.admin - 管理（admin）サイト。
django.contrib.auth - 認証システム
django.contrib.contenttypes - コンテンツタイプフレームワーク
django.contrib.sessions - セッションフレームワーク
django.contrib.messages - メッセージフレームワーク
django.contrib.staticfiles - 静的ファイルの管理フレームワーク
これらの機能はよく使われるのでデフォルトで付属されている
```

```
python3 manage.py migrate
```

上記のコマンドで INSTALLED_APPS の設定を参照するとともに、 mysite/settings.py ファイルのデータベース設定に従って必要なすべてのデータベースのテーブルを作成。。migrate コマンドは INSTALLED_APPS のアプリのためだけに実行される。
