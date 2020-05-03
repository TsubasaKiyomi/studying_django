##### 開発サーバー

###### サーバーの起動方法

プロジェクトが動作するか確認する。
外側の mysite ディレクトリに移動してコマンドを実行する。

```
python3 manage.py runserver
```

出力結果

```
Performing system checks...

System check identified no issues (0 silenced).
May 03, 2020 - 00:03:35
Django version 3.0.5, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

サーバーが起動したことで、アクセスできるようになる。
この時点でアクセスすると、ロケットの画面表示になる。

###### ポート番号の変更

デフォルトではポート 8000 を起動
ポートを変更するコマンド

```
python manage.py runserver 8080
```

サーバの IP を指定するときには、ポート番号も一緒に指定する。例えば、 全ての IP からのリクエストを受け付ける (サーバを他のコンピュータから見えるようにする) には以下のコマンドを入力する。

```
python manage.py runserver 0:8000
```

0 は 0.0.0.0 のショートカット。
