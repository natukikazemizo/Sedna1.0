# Design 設計書

## 学習内容
* sqllite3の基本的使用方法
  * insert
  * update
  * delete
  * commit
  * rollback
  * DB保存
* パスの指定方法
* エラーログと通常ログの使い方
* 自動テスト方法の学習

## 処理の流れ
※各処理で、infoログ出力
### 準備処理
1. DB生成
1. テーブル生成

### 本処理
1. ファイルパス決定
0. DB OPEN
0. TRANSACTION開始
0. INSERT
0. UPDATE
0. DELETE
0. COMMIT
0. UPDATE
0. ROLLBACK
0. DBClose

### テスト用処理
1. テーブル破棄
1. DB破棄

## テスト項目
* 生成パスの確認
* 正常動作
* エラー時（OPEN後）
  * トランザクションロールバック確認
  * DBクローズ確認
* エラー時（OPEN前）
* エラー時（クロース後）