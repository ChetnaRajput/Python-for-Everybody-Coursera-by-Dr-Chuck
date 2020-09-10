"""
Following Links in Python-

In this assignment you will write a Python program. The program will use urllib
to read the HTML from the data files below, extract the href= vaues from the
anchor tags, scan for a tag that is in a particular position relative to the first
name in the list, follow that link and repeat the process a number of times and
report the last name you find.

We provide two files for this assignment. One is a sample file where we give you
the name for your testing and the other is the actual data you need to process
for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html

Find the link at position 3 (the first name is 1). Follow that link. Repeat this
process 4 times. The answer is the last name that you retrieve.

Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Raul.html

Find the link at position 18 (the first name is 1). Follow that link. Repeat this
process 7 times. The answer is the last name that you retrieve.

"""



# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count: "))
pos = int(input("Enter position: "))

ct=0
t=[]

while ct <= count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        t.append(tag.get('href', None))
        #print(tag.get('href', None))

    print("Retrieving: ",url)
    url=t[pos-1]
    t=[]
    ct+=1


#http://py4e-data.dr-chuck.net/known_by_Raul.html
# count = 7
# Pos = 18
#Rosie
