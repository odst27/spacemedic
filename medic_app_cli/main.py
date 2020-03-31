import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen("https://www.miemssalert.com/chats/Default.aspx?hdRegion=5&hdtab=Hospitals").read()
soup = BeautifulSoup(html,features="lxml")

table = soup.find("table", {"id": "tblHospitals"})
table_data = table.find_all("tr")

table_data.pop(0)
# works 26 elements print len(table_data)

hospitals = {}
key = 0
dataarr = []

# 8 cells per row, 6 valid elements. keeping invalid element pos: 0 and 7 as 'u\n'
for tr in table_data:   
   for td in tr:
      td = td.strip('\n')
      for txt in td:
         dataarr.append(txt)
      print dataarr     
      del dataarr[:]
      #hospitals[key] = dataarr
      #dararr = []
   #key = key + 1


print hospitals
#print len(hospitals)

#for unit in hospitals:
#   print unit 
