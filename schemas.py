from pydantic import BaseModel

class Input(BaseModel):
    text: str

class Result(BaseModel):
    closed_strokes_count: int
