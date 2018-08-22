# UNIX Quick Reference - Part II

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
#
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
