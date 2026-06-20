import sqlite3
import os
import logging

logger = logging.getLogger(__name__)

# 2026.06.20 Grok生成ソースを元に作成

# ========================
# 設定
# ========================
DB_NAME = "test_database.db"
TABLE_NAME = "users"


# ========================
# 準備処理
# ========================
def prepare_database():
    """DB生成とテーブル生成"""
    logger.info("=== 準備処理 ===")
    
    # DBファイルが存在する場合は削除（再作成のため）
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        logger.info(f"既存のDBを削除しました: {DB_NAME}")
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # テーブル作成
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        )
    """)
    
    conn.commit()
    conn.close()
    logger.info(f"DBとテーブルを作成しました: {DB_NAME} / {TABLE_NAME}")

    return True


# ========================
# 本処理
# ========================
def main_operations():
    """本処理（トランザクションの例）"""
    logger.info("\n=== 本処理 ===")
    
    # 1. ファイルパス決定
    db_path = DB_NAME
    logger.info(f"DBパス: {db_path}")
    
    # 0. DB OPEN
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # 0. TRANSACTION開始
        conn.execute("BEGIN")
        logger.info("トランザクション開始")
        
        # 0. INSERT
        cursor.execute(
            f"INSERT INTO {TABLE_NAME} (name, age, email) VALUES (?, ?, ?)",
            ("太郎", 25, "taro@example.com")
        )
        cursor.execute(
            f"INSERT INTO {TABLE_NAME} (name, age, email) VALUES (?, ?, ?)",
            ("花子", 30, "hanako@example.com")
        )
        logger.info("INSERT完了")
        
        # 0. UPDATE
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET age = ? WHERE name = ?",
            (26, "太郎")
        )
        logger.info("UPDATE完了")
        
        # 0. DELETE
        cursor.execute(
            f"DELETE FROM {TABLE_NAME} WHERE name = ?",
            ("花子",)
        )
        logger.info("DELETE完了")
        
        # 0. COMMIT
        conn.commit()
        logger.info("COMMIT実行 → データが確定されました")
        
        # 0. UPDATE（別の更新）
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET email = ? WHERE name = ?",
            ("taro.new@example.com", "太郎")
        )
        logger.info("別のUPDATE実行")
        
        # 意図的にROLLBACKする例（ここではデモのため）
        # 0. ROLLBACK
        conn.rollback()
        logger.info("ROLLBACK実行 → 最後のUPDATEは取り消されました")
        
    except sqlite3.Error as e:
        logger.error(f"エラーが発生しました: {e}")
        conn.rollback()
        logger.info("エラーによりROLLBACKしました")
    finally:
        # 0. DBClose
        conn.close()
        logger.info("DBをクローズしました")


# ========================
# テスト用処理
# ========================
def cleanup_database():
    """テスト用：テーブル破棄とDB破棄"""
    logger.info("\n=== テスト用処理（クリーンアップ） ===")
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # テーブル破棄
    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
    logger.info(f"テーブルを破棄しました: {TABLE_NAME}")
    
    conn.close()
    
    # DBファイル削除
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        logger.info(f"DBファイルを破棄しました: {DB_NAME}")


# ========================
# 実行
# ========================
if __name__ == "__main__":
    prepare_database()
    main_operations()
    
    # 結果確認
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    rows = cursor.fetchall()
    logger.info("\n=== 最終的なテーブル内容 ===")
    for row in rows:
        logger.info(row)
    conn.close()
    
    # クリーンアップ（必要に応じてコメントアウト）
    cleanup_database()



