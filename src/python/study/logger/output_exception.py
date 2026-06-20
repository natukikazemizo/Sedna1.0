import logging
import os

# 保存したいログファイルの絶対パスまたは相対パスを作成
log_path = os.path.join(os.path.dirname(__file__), 'app.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    filename=log_path,
    encoding='utf-8'
)

logger = logging.getLogger(__name__)

try:
    logger.info(log_path)
    1 / 0
except Exception:
    logger.exception("エラーが発生しました")   # これだけでOK！