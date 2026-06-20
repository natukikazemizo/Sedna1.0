from pathlib import Path

# このファイル（paths.py）があるディレクトリの絶対パスを取得
BASE_DIR = Path(__file__).resolve().parent.parent

TEST_DB_DIR = BASE_DIR / "data/test.db"
MAIN_DB_DIR = BASE_DIR / "data/main.db"
# logger.pyで宣言するので不要？
# LOG_DIR = BASE_DIR / "log/out.log"

