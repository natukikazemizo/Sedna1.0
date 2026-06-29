#from abc import ABC, abstractmethod
from typing import Generic, TypeVar #, List, Optional
from src.database.connection import DatabaseConnection

T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, db: DatabaseConnection):
        self.db = db