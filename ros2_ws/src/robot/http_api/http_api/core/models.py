from pydantic import BaseModel
from typing import Optional

class TmgrSignalModel(BaseModel):
    signal: int
    extra: Optional[int]