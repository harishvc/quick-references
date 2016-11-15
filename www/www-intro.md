## OSI Layer
  Open Systems Interconnection (OSI)) is **reference model** that shows how  applications communicate over a network. A reference model is a **conceptual framework** for understanding relationships. 
* Layer 1: Physical Layer provides the hardware for sending and receiving data 
* Layer 2: The data link layer. Ethernet is the main data link layer
* Layer 3: Network layer handles routing of the data. IP is the network layer for the Internet.
* Layer 4: Transport layer. On the internet, TCP and UDP provide these services for most applications.
* Layer 5: Session layer. Services include authentication and reconnection.
* Layer 6: Presenation layer. This layer is usually part of an **operating system (OS)** and converts incoming and outgoing data from one presentation format to another 
* Layer 7: Application layer.


## What is ASCII?
American Standard Code for Information Interchange (ASCII), was created in 1963 by the "American Standards Association" . There are 256 ASCII characters (from 0 to 255) which include control characters, printable characters and extended characters. [More information about ASCII](http://www.theasciicode.com.ar/ascii-printable-characters/capital-letter-a-uppercase-ascii-code-65.html)
```
#python3.x
$> ord('A')  #get ASCII for letter 'A'
65
```

## What is character encoding?
* A charset is the set of characters you can use
* Encoding is how these characters are stored into memory
* A byte is 8 bits and can only have 256 distinct values!  
* How can all the languages then be represented? This need has lead to several encodings and charsets. 
* A popular charset is **Unicode**  that gives each character a codepoint in format ```u+xxxx```.  It has the ambition to contain all characters (and popular icons) used in the **entire world**.
* **UTF-8, UTF-16 and UTF-32 are encodings** apply the Unicode character table and have a slightly different way on how to encode them. 
* UTF-8 will only use 1 byte when encoding an ASCII character, for other characters, it will use the first bit to indicate that a 2nd byte will follow.



## What is Data Serialization?
* Data serialization is the concept of converting structured data into a format that allows it to be shared or stored in such a way that its original structure to be recovered. 
* In some cases, the secondary intention of data serialization is to minimize the size of the serialized data which then minimizes disk space or bandwidth requirements. 

In python you can use `pickle` or `json.dumps`. `pickle` stores in binary format while `json.dumps` stores in human readable format.
```
#pickle
import pickle
>>> grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }
>>> serial_grades = pickle.dumps( grades )
>>> serial_grades
b'\x80\x03}q\x00(X\x03\x00\x00\x00Bobq\x01KHX\x05\x00\x00\x00Aliceq\x02KYX\x07\x00\x00\x00Charlesq\x03KWu.'

#json
grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }
z = json.dumps(grades)
print(z)
'{"Bob": 72, "Alice": 89, "Charles": 87}'
```

# What is JSON?
* JavaScript Object Notation (JSON) is a format that encodes objects in a string
* JSON objects can be of different types - str, int, list, dict, tuple which makes it very popular!
* JSON contains data without any labels/descriptions - less data transferred over the network! 
* Serialization means to convert an object into string (make it **flat**), and deserialization is its inverse operation.
```
https://docs.python.org/3/library/json.html
>>> import json
#
#Example 1: int
>>> a = 1234   #json object is integer
>>> type(a)
<class 'int'>
>>> json.dumps(a)
'1234'          #json object converted to string
#
#Example 2: Tuple
>>> a = (1,2,3)
>>> type(a)
<class 'tuple'>
>>> json.dumps(a)
'[1, 2, 3]'
#
#Example 3: List of dict
>>> a = ['foo', {'bar': ('baz', None, 1.0, 2)}]
>>> type(a)
<class 'list'>
>>> json.dumps(a)
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
#Example 4: dict
>>> a = {"c": 0, "b": 0, "a": 0}
>>> type(a)
<class 'dict'>
>>> json.dumps(a)
'{"b": 0, "c": 0, "a": 0}'
```
## JSON vs XML?

### XML
* XML is a language
* Generalized markup
* Create new datatypes
* XPath/XQuery for extracting information in deeply nested structures
* Relatively wordy compared to JSON

### JSON
* Simple syntax, which results in less "markup" overhead compared to XML
* Handful of different data types are supported
* JSON generally better for server to client communication - browser understands JSON natively!

## Parse JSON feed
```
import requests
import simplejson

r = requests.get('Https://api.github.com/users/harishvc/events/public')
c = r.content
j = simplejson.loads(c)

for item in j:
    for c in item['payload']['commits']:
    	print(c['sha'], c['message'])

d20bd606f4873d2a84383e04f8431253e8e99e02 update Concurrency notes location
14b3aab151b0b04f355283163d4f178560f440ff add links to examples
f2299d98b8f3c86f90b1f80fca1822f504188656 clean up 2
...
..
```

## Cookie vs Cache  (```chrome://net-internals```)

### Cookie
* Cookie is a very small encrypted text file which is stored on the client’s machine by the web site using the browser and is sent back to the server each time a page is requested
* Cookies expire afer a specific time (determined by the application setting the cookie)
* Browser preference can be modified to handle cookie - block site, remove after browser is closed

### Cache
* Use by browsers to make the loading of web pages faster
* Cache is kept in the client’s machine until they are removed manually by the user.


## What happens when a web page is requested?
* http://programmers.stackexchange.com/questions/211176/in-need-of-a-more-technical-answer-for-an-interview-question-about-how-the-inter
* http://www.howtogeek.com/138771/htg-explains-how-latency-can-make-even-fast-internet-connections-feel-slow/


## HTTP status codes, HTTP redirect
200 - Ok  
301 - permament redirection (retains SEO juice!)  
302 - temporary redirection  
304 - not modified  
403 - Directory index listing not allowed    
404 - Page not found  
500 - Server Error  


## HTTP request methods
* GET     - Request data from a specific source
* PUT     - Submit data to a specific source to process
* HEAD    - Same as GET but returns headers no other content
* PUT     - uploads a specific URI
* DELETE  - delete a specific URI
* OPTIONS - Shows all the request methods HTTP supports
* CONNECT - Converts the request connection to a transparent TCP/IP tunnel


##Explain TCP Flags

There are 6 TCP flags. [More information about TCP Flags](http://www.firewall.cx/networking-topics/protocols/tcp/136-tcp-flag-options.html)  


##  What is a recommended page load time?
* Page Load Time consists of two components: 1) network and server response time and 2) browser time   
* **Server response time** is the time it takes for a server to return the initial HTML, factoring out the network time
* Under a second (on desktops) and less than 200 ms on mobile


## How can you improve the page load time?
* https://moz.com/learn/seo/page-speed

## What is HTTP pipelining & persistence?  

### Pipelining
* HTTP pipelining is a technique in which multiple HTTP requests are sent on a single TCP connection without waiting for the corresponding responses.
* Pipelining of requests results in a dramatic improvement
* Pipelining was introduced in HTTP/1.1

### Persistence
* HTTP persistent connection, also called **HTTP keep-alive** is the idea of using a single TCP connection to send and receive multiple HTTP requests/responses, as opposed to opening a new connection.
* Lower CPU and memory usage (because fewer connections are open simultaneously)
* Reduced latency in subsequent requests (no handshaking)
```
Connection: keep-alive
```

## HTTP headers
```
$>curl -I http://foo.com
HTTP/1.1 200 OK
Date: Thu, 20 Oct 2016 06:17:38 GMT
Server: Apache
Last-Modified: Tue, 18 Oct 2016 01:04:55 GMT
Accept-Ranges: bytes
Cache-Control: max-age=12345
Expires: Fri, 21 Oct 2016 06:17:38 GMT
Vary: Accept-Encoding
Content-Type: text/html
```

## References  
* [Back of the envelope calculations](http://highscalability.com/blog/2011/1/26/google-pro-tip-use-back-of-the-envelope-calculations-to-choo.html)
* http://www.yegor256.com/2015/11/16/json-vs-xml.html
* [More information about headers](https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers)



