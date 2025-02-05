from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from enum import Enum
from strenum import StrEnum


class Document(BaseModel):
    id: str
    title: str
    content: str
    uri: Optional[str] = None


class VectorStore(BaseModel, ABC):

    @abstractmethod
    async def upsert(self, documents: List[Document]) -> bool:
        pass
    
    @abstractmethod
    async def query(self, query: str) -> List[Document]:
        pass

class LLM(BaseModel, ABC):

    @abstractmethod
    def ask(self, documents: List[str], question: str) -> List[List[float]]:
        pass