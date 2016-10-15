# What is Data Serialization?
Data serialization is the concept of converting structured data into a format that allows it to be shared or stored in such a way that its original structure to be recovered. In some cases, the secondary intention of data serialization is to minimize the size of the serialized data which then minimizes disk space or bandwidth requirements. 

In python you can use `pickle` or `json`. `pickle` stores in binary format while `json` stores in human readable format.
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
JavaScript Object Notation (JSON) is a format that encodes objects in a string. Serialization means to convert an object into that string, and deserialization is its inverse operation.

# JSON vs XML?
XML
	- XML is a language
	- Generalized markup
	- Create new datatypes
	- XPath/XQuery for extracting information in deeply nested structures
	- Relatively wordy compared to JSON
JSON
	- Simple syntax, which results in less "markup" overhead compared to XML
	- Handful of different data types are supported
	- JSON generally better for server to client communication - browser understands JSON natively!

# Parse JSON feed
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
