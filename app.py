from fastapi import FastAPI, HTTPException

from helpers import is_valid_text
from schemas import Input, Output
from services import closed_strokes_count

app = FastAPI(
    title='Menta Tickets Challenge!',
    description='Closed Strokes Counter API',
    version='1.0.0',
    openapi_tags=[{
        "name": "default",
        "description": "Given a text return the count of closed strokes. Font-Text: DejaVuSans"
    }]
)

@app.post("/", response_model=Output)
def closed_strokes(input: Input):
    if not is_valid_text(input.text):
        raise HTTPException(status_code=400, detail='Not allowed symbols into text. Allowed symbols are: @ # $ % ∞ ‰ & / ( ) = ? ¿ _ -')
    
    count = closed_strokes_count(input.text)
    return Output(closed_strokes_count=count)
