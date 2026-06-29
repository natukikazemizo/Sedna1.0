from utils.exceptions import BusinessError

# ビジネスロジック層（Service）
class OrderService:
    def __init__(self, order_repo, product_repo):
        self.order_repo = order_repo
        self.product_repo = product_repo

    def create_order(self, customer_id: int, items: list) -> dict:
        with self.db.get_connection() as conn:  # トランザクション
            try:
                # 在庫チェック → 注文作成 → 在庫減算 を1トランザクションで
                conn.execute("BEGIN")
                # ... ビジネスロジック ...
                conn.commit()
                return {"status": "success", "order_id": order_id}
            except Exception as e:
                conn.rollback()
                raise BusinessError(f"注文処理失敗: {e}")
