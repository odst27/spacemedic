import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen("https://www.miemssalert.com/chats/Default.aspx?hdRegion=5&hdtab=Hospitals").read()
soup = BeautifulSoup(html,features="lxml")

table = soup.find("table", {"id": "tblHospitals"})
table_data = table.find_all("tr")

table_data.pop(0)
# works 26 elements print len(table_data)

hospitals = []
for td in table_data:
   print "**********"
   for tags in td:
      print tags
   print "**********"


