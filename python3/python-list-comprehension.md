#Python List Comprehension

**List comprehension is an elegant way to define and create list in Python**

##Example 1: Removing vowels from a sentence
````python
input = "Hello World!"
vowels ="aeiou"
z = "".join([x for x in input if x not in vowels])
print(input)  #Hello World!
print(z)      #Hll Wrld!
````


#References
* [Analytics Vidhya Tutorial on List Comprehension](http://www.analyticsvidhya.com/blog/2016/01/python-tutorial-list-comprehension-examples/)
