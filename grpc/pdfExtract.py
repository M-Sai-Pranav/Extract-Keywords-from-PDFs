import json
import re
from PyPDF2 import PdfReader

def extractData(): 
    # Step 6 -> extractData fun called unary_server.py file is executed here
    reader = PdfReader("coding.pdf")
    page = reader.pages[30]
    text = page.extract_text()

    vocabdic = {} 
    f = open('commonwords.json', 'r')
    basic = json.load(f)

    for w in text.split():
        w = re.sub('[^0-9a-zA-Z]+', '',w)
        w = w.lower()
        if w not in basic:
            vocabdic[w] = True
 
    print(vocabdic)   # Step -> Prints the not so commonly used words to grpc py server

# /Desktop/electronfresh/grpc$ python3 unary_server.py
    


