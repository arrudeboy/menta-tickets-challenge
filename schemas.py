from pydantic import BaseModel

class Input(BaseModel):
    text: str

class Output(BaseModel):
    closed_strokes_count: int
