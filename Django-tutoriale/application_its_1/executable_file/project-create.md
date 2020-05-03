##### django プロジェクトの作成

###### プロジェクトとは？

- データベースの設定や django の固有オプション、アプリケーション固有の設定など、ここの django インスタンスの設定を集めたもの。
- プロジェクトとは、設計図を基に実体化させる設定を集めたもの（オプション・アプリケーションの設定）

###### インスタンスとは？

- インスタンスは　＝　クラスの設計図を基に作成した実体

##### mysite ディレクトリの作成

- project ディレクトリに移動し　 django-admin startproject mysite 　を実行し project ディレクトリ内に mysite ディレクトリを作成した。

```
django-admin startproject mysite
```

作成結果

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

```

###### 作成したディレクトリが何をしているのか？

- 外側の mysite/のルートディレクトリは、プロジェクトのコンテナの役割なので任意の名前に変更できる。

- manage.py は Django プロジェクトに対する様々な操作を行うためのコマンドラインユーティリティ(画面上でキーボードにより操作)｡

- 内側の mysite/のディレクトリは、このプロジェクトの実際の Python パッケージのこと。この名前が Python パッケージの名前であり、import の際に使用する名前となる(例えば import mysite.urls) 。

- mysite/**init**.py は、このディレクトリが Python パッケージであることを Python に知らせるための空のファイルのこと。

- mysite/settings.py は、Django プロジェクトの設定ファイルのこと。

- mysite/urls.py は Django プロジェクトの URL 宣言、Django サイトにおける「目次」のようなもの

- mysite/asgi.py はプロジェクトを提供する ASGI 互換(非同期機能)Web サーバーのエントリポイントのこと。

- mysite/wsgi.py はプロジェクトをサーブするための WSGI 互換 Web サーバーとのエントリーポイント(接続するため)のこと。

エントリポイントとは、コンピュータプログラムを実行する際 1 番最初に実行する箇所。
