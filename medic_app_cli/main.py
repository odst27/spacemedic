import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen("https://www.miemssalert.com/chats/Default.aspx?hdRegion=5&hdtab=Hospitals").read()
soup = BeautifulSoup(html,features="lxml")

table = soup.find("table", {"id": "tblHospitals"})
table_data = table.find_all("tr")
table_data.pop(0)

hospitals = {}
i = 0

for unit in table_data:
   alerts = unit.find_all('td')
   hospitals[i] = []
   j = 0
   for flag in alerts:
      if j < 7:
         hospitals[i].append(flag.string)
         j = j + 1
      
   i = i + 1

print hospitals
