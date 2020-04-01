import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen("https://www.miemssalert.com/chats/Default.aspx?hdRegion=5&hdtab=Hospitals").read()
soup = BeautifulSoup(html,features="lxml")

table = soup.find("table", {"id": "tblHospitals"})
table_data = table.find_all("tr")

table_data.pop(0)
# works 26 elements print len(table_data)

hospitals = {}

#print len(table_data)

for q in range(0,len(table_data)):
   hospitals[q] = ["null","HosName","Yellow","Red","MiniDisaster","ReRoute","TraumaByPass","null"] 

key = 0
# 8 cells per row, 6 valid elements. keeping invalid element pos: 0 and 7 as 'u\n'
for tr in table_data:
   for td in tr:
      alerts = hospitals[key]
      tmparr = [None] * len(alerts)

      for status in td:
         print "Curr line:"
         print status
         tmparr.append(status)
      
      print len(tmparr)
      print len(alerts)
      
      for i in range(len(alerts)):
         alerts[i] = tmparr[i]
      
      print alerts
      print tmparr


'''
      print td      
      print len(td)
      print len(alerts)

      for c in range(len(alerts)):
         alerts[c] = td[c]
         print alerts[c]
         print td[c]
      
   #hospitals[key] = alerts
   key = key + 1
    
'''
print hospitals

#print len(hospitals)

#for unit in hospitals:
#   print unit 

