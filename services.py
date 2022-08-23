import cv2
import textwrap
from string import ascii_letters
from PIL import Image, ImageDraw, ImageFont
from collections import Counter

def __create_text_image(text: str):
    new_text_image = Image.new('RGB', (2048, 1024), color = (73, 109, 137))
    draw = ImageDraw.Draw(new_text_image)
    unicode_font = ImageFont.truetype("DejaVuSans.ttf", 40)

    avg_char_width = sum(unicode_font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
    max_char_count = int( (new_text_image.size[0] * .95) / avg_char_width )
    scaled_wrapped_text = textwrap.fill(text=text, width=max_char_count)

    draw.text((10,10), scaled_wrapped_text, font=unicode_font, fill=(255,255,0))
    new_text_image.save('text.png')

def closed_strokes_count(text: str):
    __create_text_image(text)
    text_image = cv2.imread('text.png', cv2.IMREAD_COLOR)
    gray_text_image = cv2.cvtColor(text_image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_text_image, 200, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]
    count = 0
    for i, _ in enumerate(contours):
        if hierarchy[i][2] < 0 and hierarchy[i][3] < 0:
            count += 1

    counter = Counter(text)
    count += (counter['i'] + counter['j'])

    return count
