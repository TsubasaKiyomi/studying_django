###### マイグレーションとは？

マイグレーションは「移動、移住」などのこと
マイグレーション(Migreations)は Django でモデルに対して行った変更 (フィールドの追加やモデルの削除など) をデータベーススキーマに反映させる方法。

コマンド
"""

- migrate は、マイグレーションを適用したり、適用をキャンセルするのに使います。
- makemigrations は、モデルに対して行った変更をもとに、新しいマイグレーションを作成します。
- sqlmigrate は、マイグレーションに対応する SQL 文を表示します。
- showmigrations は、プロジェクトのマイグレーションとそのステータスをリストします。
  """

- makemigrations コマンド
  利用できるモデルを全てみて、まだ作成されていないテーブルを作るためのマイグレーションを生成する
- migrete コマンド
  マイグレーションを実行し、データベースにテーブルを作成する