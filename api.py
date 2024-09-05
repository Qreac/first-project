from fastapi import FastAPI
from langchain_community.llms import Tongyi
from typing import Union, Dict, List
from pydantic import BaseModel


class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]
    model: str = "tongyi"
    temperature: float = 0.7
    top_p: float = 0.7
    max_tokens: int = 2048
    stop: Union[str, List[str]] = None
    stream: bool = True
    logit_bias: Dict

tongyi = Tongyi(
    api_key=
)
def get_text(message:str):



