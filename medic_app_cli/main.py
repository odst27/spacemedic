import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen("https://www.miemssalert.com/chats/Default.aspx?hdRegion=5&hdtab=Hospitals").read()
soup = BeautifulSoup(html,features="lxml")

table = soup.find("table", {"id": "tblHospitals"})
table_data = table.find_all("tr")

# works 26 elements print len(table_data)

names = []
for td in table_data:
   print "**********"
   print td
   print "**********"
   #names.append(td.b.text.replace('\n,' ' ').strip())

#print names

#print table

#pageblk = soup.get_text()
#startpos = pageblk.find("HospitalYellow")
#endpos = pageblk.find("CountyBlue")


#print pageblk

'''
hospitalblk = pageblk[startpos+63:endpos]
reg5 = []

for hospital in hospitalblk.strip("\n").splitlines():
   reg5.append(hospital)
   if ":" in hospital:
     print "**************************"
     print hospital + "status: " + hospital[hospital.find(":")-2:]

for val in reg5:
   print val 

'''

