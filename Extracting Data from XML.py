"""
Extracting Data from XML

In this assignment you will write a Python program that will prompt for a URL,
read the XML data from that URL using urllib and then parse and extract the
comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_890828.xml (Sum ends with 65)

Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
You are to look through all the <comment> tags and find the <count> values sum
the numbers.
To make the code a little simpler, you can use an XPath selector string to look
through the entire tree of XML for any tag named 'count' with the following line
of code:-counts = tree.findall('.//count')

Take a look at the Python ElementTree documentation and look for the supported
XPath syntax for details. You could also work from the top of the XML down to
the comments node and then loop through the child nodes of the comments node.

Sample Execution
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...
"""


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

Sum=0
c=0

address = input("Enter location: ")
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print("Retrieving", address)

tree = ET.fromstring(data)

counts = tree.findall('.//count')

for i in counts:
    Sum+=int(i.text)
    

print("Retrieved ", len(data) ,"characters")
print("Count: ", len(counts))
print("Sum: ", Sum)

# count: 50
# sum: 2465
