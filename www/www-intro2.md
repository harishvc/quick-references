# Introduction to Networking (part 2): Word Wide Web (WWW) 


## HTTP status codes
200 - ok  
204 - no Content, no message body in the response
301 - permament redirection (retains SEO juice!)  
302 - temporary redirection  
304 - not modified
400 - bad request   
401 - Unauthorized Error - check credentials   
403 - Forbidden - Directory index listing not allowed    
404 - Page not found
501 - Not implemented  
502 - Bad Gateway
503 - Service unavailable


## HTTP request methods
* GET     - Request data from a specific source
* PUT     - Submit data to a specific source to process
* HEAD    - Same as GET but returns headers no other content
* PUT     - uploads a specific URI
* DELETE  - delete a specific URI
* OPTIONS - Shows all the request methods HTTP supports
* CONNECT - Converts the request connection to a transparent TCP/IP tunnel

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
### Additional References  
* [Back of the envelope calculations](http://highscalability.com/blog/2011/1/26/google-pro-tip-use-back-of-the-envelope-calculations-to-choo.html)
* http://www.yegor256.com/2015/11/16/json-vs-xml.html
* [More information about headers](https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers)


## Proxy vs Reverse Proxy
* Proxy: Website retrieves information on-behalf of someone else. Example: People is specific subnet blocked from local news. Proxy server can access news.
* Reverse Proxy: Load balancing traffic or running services on non-standard port

Reference:
1. https://stackoverflow.com/questions/224664/difference-between-proxy-server-and-reverse-proxy-server

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

## Why do we need SSL?
SSL (Secure Sockets Layer) is a security protocol responsible for establishing an encrypted (secure) link between a web server and a browser

## What is a digital certificate?
* SSL digital certificates are signed by Certificate Authority (CA), after **verifying identity** of an applicant. 
* After verification, digital certificates are issued along with Intermediate certificate that tie back to CA root certificate

## Steps to create digital certificate?
* Create private and public keys
* Store private keys in a secure place accessible by webserver
* Generate Certificate Signing Request (`CSR`) using the public key
* Submit the CSR to a Certificate Authority (`CA`)
* `CA` will provide you a SSL digital certificate for your domain and intermediate certificate
* Upload the SSL digital certificate and intermediate certificate on your server and then configure your webserver
* Intermediate certificate establishes the credibility of your certificate by tying it to your CA root certificate
* SSL digital certificates are signed by Certificate Authority (`CA`), after verifying identity of an applicant

References:
1. https://www.digicert.com/ssl/
2. https://blog.ragnarson.com/2013/10/18/why-do-we-need-ssl.html


## What is REST API?
* Representational State Transfer (REST)
* Takes advantage of HTTP - no need to install libraries or additional software!
* REST does not maintain state
* REST API access `end points` and header contains `access token` 

## Session vs Token based Authentication 
* In **Session based authentication** heavy lifting is done on the server side. After successful login, `sessionID` is generated and stored in the browser in cookies.
Future requests use this `sessionID`. Based on browser setting on expiration set by the server `sessionID` will expire and new one generated. Ideal for public - no prior signup needed
* Token are ideal for API based requests. Tokens are included in the request header to various end-points. Tokens are usually associated with an user. Works well since it is stateless. Ideal for API requests - developers have to sign up for a token 


## Cookie vs Cache  (```chrome://net-internals```)

### Cookie
* Cookie is a very small encrypted text file which is stored on the client’s machine by the web site using the browser and is sent back to the server each time a page is requested
* Cookies expire afer a specific time (determined by the application setting the cookie)
* Browser preference can be modified to handle cookie - block site, remove after browser is closed

### Cache
* Use by browsers to make the loading of web pages faster
* Cache is kept in the client’s machine until they are removed manually by the user.


## What is ASCII?
American Standard Code for Information Interchange (ASCII), was created in 1963 by the "American Standards Association" . There are 256 ASCII characters (from 0 to 255) which include control characters, printable characters and extended characters. [More information about ASCII](http://www.theasciicode.com.ar/ascii-printable-characters/capital-letter-a-uppercase-ascii-code-65.html)
```
#python3.x
$> ord('A')  #get ASCII for letter 'A'
65
$> chr(65)   #convert int to chr
'A'
```

## What is encoding, `Unicode`, `UTF`, `UTF-8`?
* Reference: https://www.quora.com/What-is-UTF8 
* Encoding is how these characters are **stored**
* A byte is 8 bits and can only have 256 distinct values (2^8)!  
* `Unicode` is a **standard** for representing a great variety of characters from many languages  
* `Unicode Transfer Format (UTF)` is a *method* for encoding `Unicode` characters
* `UTF-8` is a popular format for data transfer online  
	* Here `8` means that `8-bits` are used in the encoding
	* A character in `UTF-8` can be `1 to 4 bytes` 
	* `UTF-8` will only use 1 byte when encoding an ASCII character for other characters, first bit to indicate that a `2nd byte` will follow


## What is decoding?
* Convert a **encoded data**  to text
* Encoding and decoding are critical for **efficient transmission and storage**
```
#UTF-8
#https://www.browserling.com/tools/utf8-encode
encode('A')  #\x41
#https://www.browserling.com/tools/utf8-decode
decode('\x41')  #A
```

## What is Data Serialization?
* Data serialization is the concept of converting **structured data (object)** as **unstructured (flat,example: string)** that allows it to be shared or stored in such a way that its original structure to be **recovered** 
* In some cases, the secondary intention of data serialization is to minimize the size of the serialized data which then minimizes disk space or bandwidth requirements. 

In python you can use `pickle` or `json.dumps`. `pickle` stores in binary format while `json.dumps` stores in human readable format.
```
#pickle
import pickle
>>> grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }
>>> serial_grades = pickle.dumps( grades )
>>> serial_grades
b'\x80\x03}q\x00(X\x03\x00\x00\x00Bobq\x01KHX\x05\x00\x00\x00Aliceq\x02KYX\x07\x00\x00\x00Charlesq\x03KWu.'

#json serialize
grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }
z = json.dumps(grades)
print(z)
'{"Bob": 72, "Alice": 89, "Charles": 87}'
>>> type(z)
<class 'str'>  #flat!

#json deserialize
>>> x = json.loads(z)
>>> x
{'Alice': 89, 'Bob': 72, 'Charles': 87}
>>> type(x)
<class 'dict'>
```

# What is JSON?
* JavaScript Object Notation (JSON) is a format for serialization of objects 
* JSON object are human readable
* JSON object when deserialized **retain original type** (str, int, list, dict, tuple) which makes it very popular!
* JSON object data without any labels/descriptions - less data transferred over the network! 
```
https://docs.python.org/3/library/json.html
>>> import json
#List of dict
>>> a = ['foo', {'bar': ('baz', None, 1.0, 2)}]
>>> type(a)
<class 'list'>
>>> z = json.dumps(a)
>>> type(z)
<class 'str'>   #serialized
>>> z
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
>>> x = json.loads(z)
>>> type(x)
<class 'list'>  #deserialized
>>> x
['foo', {'bar': ['baz', None, 1.0, 2]}]
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
