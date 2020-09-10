"""
Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that
you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt
There are three ways that you might retrieve this web page and look at the
response headers:

Preferred: Modify the socket1.py program to retrieve the above URL and print out
the headers and data. Make sure to change the code to retrieve the above URL -
the values are different for each URL.
Open the URL in a web browser with a developer console or FireBug and
manually examine the headers that are returned.
"""


import socket

mysokt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysokt.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysokt.send(cmd)

while True:
    data = mysokt.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysokt.close()


"""
OUTPUT:-
HTTP/1.1 200 OK

Date: Sat, 05 Sep 2020 13:11:48 GMT

Server: Apache/2.4.18 (Ubuntu)

Last-Modified: Sat, 13 May 2017 11:22:22 GMT

ETag: "1d3-54f6609240717"

Accept-Ranges: bytes

Content-Length: 467

Cache-Control: max-age=0, no-cache, no-store, must-revalidate

Pragma: no-cache

Expires: Wed, 11 Jan 1984 05:00:00 GMT

Connection: close

Content-Type: text/plain



Why should you learn to write programs?

Writing programs (or programming) is a very creative 
and rewarding activity.  You can write programs
 for 
many reasons, ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem.  This book assumes that 
everyone needs to know how to program, and that once 
you know how to program you will figure out what you want 
to do with your newfound skills.
"""
