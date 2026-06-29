import sqlite3
from contextlib import contextmanager
from pathlib import Path
from threading import local
import logging
from config import path_settings

logger = logging.getLogger(__name__)

# データベース接続管理
class DatabaseConnection:
    def __init__(self, db_path: str = "business.db"):
        logger.info("db_path:" + db_path)
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._local = local()  # スレッドローカル
        logger.info("初期化終了")

    @contextmanager
    def get_connection(self):
        """コンテキストマネージャで接続管理（推奨）"""
        logger.info("connection取得取得")
        conn = None
        try:
            if not hasattr(self._local, "conn") or self._local.conn is None:
                logger.info("DBが無いので、作成")
                conn = sqlite3.connect(
                    str(self.db_path),
                    timeout=30,           # ロック待機時間
                    isolation_level=None, # 自動コミット制御
                    check_same_thread=False
                )
                conn.row_factory = sqlite3.Row  # 辞書形式で取得しやすく
                self._local.conn = conn
            yield self._local.conn
        finally:
            if conn:
                logger.info("conn.close()")
                conn.close()
                self._local.conn = None

    def init_db(self):
        """初回テーブル作成"""
        ret = False
        with self.get_connection() as conn:
            logger.info("初回テーブル作成")
            conn.executescript(open(path_settings.SCHEMA_DIR, encoding="utf-8").read())
        ret = True
        return ret
