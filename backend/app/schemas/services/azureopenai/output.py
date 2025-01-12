from pydantic import BaseModel
from typing import List, Optional

class Choice(BaseModel):
    text: any
    index: int
    finish_reason: str
    logprobs: Optional[dict] = None

class Usage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int

class CompletionResponse(BaseModel):
    id: str
    created: int
    choices: List[Choice]
    usage: Usage
