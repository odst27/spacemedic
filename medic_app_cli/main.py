from lxml import html
from cssselect import GenericTranslator, SelectorError

file = open("https://www.miemssalert.com/chats/Default.aspx?hdRegion=5&hdtab=Hospitals", "r")
doc = html.document_fromstring(file.read())
print(doc.cssselect('title')[0].text_content())
