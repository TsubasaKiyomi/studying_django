#### アプリケーション作成　その１

チュートリアルでは投票(poll)アプリケーションを作成する。
poll アプリケーションは２つの部分からなる

- ユーザーが投票したり結果を表示できる公開用のサイト
- 投票項目の追加、変更、削除を行うための管理(admin)サイト

#### 目次

###### 1.Django のインストール

install_django.md

- インストールの仕方、バージョンの確認について

###### 2.プロジェクトの作成

project_creation.md

- プロジェクトとは？
- インスタンスとは？
- mysite ディレクトリの作成 [django-admin startproject mysite]
- 作成したディレクトリが何をしているのか？

###### 3.開発用サーバー

development_server.md

- サーバーの起動方法 [python3 manage.py runserver]
- ポート番号の変更 [python manage.py runserver 8080][python manage.py runserver 0:8000]

###### 4.polls アプリケーションを作る

application_create.md

- アプリケーションを作る [python3 manage.py startapp polls ]
- プロジェクトとアプリケーションの違い

###### 5.はじめてのビュー作成

view_creation.md

- view とは?
- view の書き方
- URLconf を作成し対応付けする
- HttpResponse とは？
- URL URLconf とは？　 URL ディスパッチャとは？
- include()とは

###### 6.その他の用語

other_terms

- migreation.md
  マイグレーションとは？

- regular_expressions.md
  正規表現とは？

- path.md
  path()関数の種類
