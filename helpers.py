import re

REGEX = re.compile('^[\w\d @#\\$\\%∞‰&/\\(\\)=\\?¿_-]+$')

def is_valid_text(text: str):
    return re.match(REGEX, text)
