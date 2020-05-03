##### Djanngo のインストール

###### python バージョンの確認

Django をインストールするにあたり python がインストールされているか確認する

```
python -V
Python 2.7.16
python3 -V
Python 3.8.1
```

- python 自体は確認できた。

###### django のインストール

```
python -m pip install Django
```

###### django のバージョン確認

ドキュメントガイドにしたがって確認できた。

```
>>> import django
>>> print(django.get_version())
3.0.5
```

しかし

```
python -m django --version
と打つとエラーとなる
エラー内容
>>> python -m django --version
  File "<stdin>", line 1
    python -m django --version
              ^
SyntaxError: invalid syntax
構文エラーとなる。
対話モード外でpython -m django --versionを打つと
/System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python: No module named django
djangoと言うmoduleが無いことが返ってくる。
```

python3 -m pip install Django 　を打つと要件が満たされて表示される。

```
Requirement already satisfied: Django in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (3.0.5)
DjangoとPythonの Library/Frameworks要件は満たされている。
Requirement already satisfied: pytz in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from Django) (2019.3)
pytzとPythonの Library/Frameworks要件は満たされている。
- pytzはpythonでタイムゾーン関係の処理をする場合にサードパーティ製のライブラリのこと。
Requirement already satisfied: sqlparse>=0.2.2 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from Django) (0.3.1)
sqlparseとPythonの Library/Frameworks要件は満たされている
Requirement already satisfied: asgiref~=3.2 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from Django) (3.2.7)
asgirefとPythonの Library/Frameworks要件は満たされている
```

インストールできていることが分かった。
