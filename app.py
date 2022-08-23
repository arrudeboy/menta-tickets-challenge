from fastapi import FastAPI, HTTPException

from helpers import is_valid_text
from schemas import Input, Result
from services import closed_strokes_count

app = FastAPI()

@app.post("/", response_model=Result)
def root(input: Input):
    if not is_valid_text(input.text):
        raise HTTPException(status_code=400, detail='Not allowed chacarters into text')
    
    count = closed_strokes_count(input.text)
    return Result(closed_strokes_count=count)
