from requests_html import HTMLSession
import json
import re
session = HTMLSession()
link = 'https://www.ccilindia.com/OMHome.aspx'
tab = session.get(link)

table = tab.html.find('table')

b = []
c = 0
for i in table:
        
    tabledata = [[c.text for c in row.find('td')]for row in i.find('tr')]
    print(str(tabledata[0]).encode("utf-8"))

    
    regex = r'(.*)Regular Market(.*)'
    if re.match(regex,str(tabledata[0])):
        #print(i)
        c+=1
        for j in tabledata[3:]:
            if j[0] == 'Total':
                break
            a = []
            for k,l in enumerate(j):
                if k != 7 and k != 8:
                    a.append(l)
            b.append(a)
tableheaders = b[0]
tabledata = b[1:]
print(c)
export = [dict(zip(tableheaders,t))for t in tabledata]
with open('export.json','w') as r:
    json.dump(export,r)
'''
for i in table:
    for row in i.find('tr'):
        print()
#for row in table.find('tr'):
#    print (row.text)
'''
'''

tabledata = [[c.text for c in row.find('td')]for row in table.find('tr')][3:]
b = []
for i in tabledata:
    if i[0] == 'Total':
        break
    a = []
    for j,k in enumerate(i):
        
        if j != 7 and j != 8:
            a.append(k)
        
    b.append(a)

tableheaders = b[0]
tabledata = b[1:]
export = [dict(zip(tableheaders,t))for t in tabledata]
with open('export.json','w') as r:
    json.dump(export,r)
'''