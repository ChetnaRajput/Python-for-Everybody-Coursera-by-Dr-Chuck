"""
Extracting Data from JSON

In this assignment you will write a Python program that will prompt for a URL,
read the JSON data from that URL using urllib and then parse and extract the
comment counts from the JSON data, compute the sum of the numbers in the file.
We provide two files for this assignment. One is a sample file where we give you
the sum for your testing and the other is the actual data you need to process
for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_890829.json (Sum ends with 67)

Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

Sample output

Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
"""


import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input("Enter location: ")

print("Retrieving ",address)

Sum=0
c=0
url = urllib.request.urlopen(address, context=ctx)
data= url.read()

info = json.loads(data)
print('User count:', len(info))

for item in info['comments']:
    value = int((item['count']))
    Sum+= value
    c+=1
    
print("Count: ",c)
print("Sum: ",Sum)


#OUTPUT-
#Retrieving: http://py4e-data.dr-chuck.net/comments_890829.json
#User count:2
#Count: 50
#Sum: 2367
