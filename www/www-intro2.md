# Data Transfer & Storage

## What is REST API?
* Representational State Transfer (REST)
* Takes advantage of HTTP - no need to install libraries or additional software!
* REST does not maintain state
* REST API access `end points` and header contains `access token` 

## Cookie vs Cache  (```chrome://net-internals```)

### Cookie
* Cookie is a very small encrypted text file which is stored on the client’s machine by the web site using the browser and is sent back to the server each time a page is requested
* Cookies expire afer a specific time (determined by the application setting the cookie)
* Browser preference can be modified to handle cookie - block site, remove after browser is closed

### Cache
* Use by browsers to make the loading of web pages faster
* Cache is kept in the client’s machine until they are removed manually by the user.

## Session vs Token based Authentication 
* In **Session based Authentication** heavy lifting is done on the server side. After successful login, `sessionID` is generated and stored in the browser in cookies.
Future requests use this `sessionID`. Based on browser setting on expiration set by the server `sessionID` will expire and new one generated. Ideal for public - no prior signup needed
* Token are ideal for API based requests. Tokens are included in the request header to various end-points. Tokens are usually associated with an user. Works well since it is stateless. Ideal for API requests - developers have to sign up for a token 


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
