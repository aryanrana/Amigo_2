from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib
import re
import sys

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return " ".join(t.strip() for t in visible_texts)

html = urllib.urlopen('https://en.wikipedia.org/wiki/Synthetic_diamond').read()
text = text_from_html(html)
text = text.split("See also")
text = text[0]+text[1]

text = re.sub('\[(.*?)\]','', text)

c = {}
text = text.replace(",","")
text =text.replace("-"," ")
text =text.replace("(","")
text =text.replace(")","")
text =text.replace("^","")
text =text.replace(";","")
text =text.replace(":","")
sentences = text.split(".")
for sentence in sentences:
  words = sentence.split(" ")
  words = list(dict.fromkeys(words))
  for word in words:
    if word in c:
      c[word].append(sentence.encode('ascii','ignore'))
    else:
      b=list()
      b.append(sentence.encode('ascii','ignore'))
      c[word]=b

def fun(word):
    if word in c: 
        return c[word]
    else:
        return []

print(fun(sys.argv[1]))
