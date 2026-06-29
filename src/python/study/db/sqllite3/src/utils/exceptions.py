from typing import Any, Dict, Optional


class BusinessError(Exception):
    """業務ロジック上のエラー（業務例外）"""
    
    def __init__(
        self, 
        message: str, 
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.error_code = error_code or "BUSINESS_ERROR"
        self.details = details or {}
        super().__init__(self.message)

    def __str__(self):
        if self.details:
            return f"{self.message} (code: {self.error_code}, details: {self.details})"
        return f"{self.message} (code: {self.error_code})"


class ValidationError(BusinessError):
    """入力バリデーションエラー"""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, error_code="VALIDATION_ERROR", details=details)


class NotFoundError(BusinessError):
    """リソースが見つからない場合"""
    def __init__(self, resource: str, resource_id: Any):
        message = f"{resource}が見つかりません (ID: {resource_id})"
        super().__init__(message, error_code="NOT_FOUND", details={"resource": resource, "id": resource_id})


class InsufficientStockError(BusinessError):
    """在庫不足専用エラー（例）"""
    def __init__(self, product_code: str, requested: int, available: int):
        message = f"在庫が不足しています: {product_code} (要求:{requested}, 残:{available})"
        super().__init__(
            message, 
            error_code="INSUFFICIENT_STOCK",
            details={
                "product_code": product_code,
                "requested": requested,
                "available": available
            }
        )