""" import required libs """
from enum import Enum
from typing import List
from pydantic import BaseModel


class StringTransformation(str, Enum):
    """Types of request"""

    lowercase = "lower"
    remove_punkt = "remove_punkt"
    replace_number_like = "replace_number_like"
    replace_phone = "replace_phone"
    replace_email = "replace_email"


class PreprocessingRequest(BaseModel):
    """The data part of user request"""

    text: str
    steps: List[StringTransformation]
