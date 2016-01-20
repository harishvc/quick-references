input = "Hello World!"
vowels ="aeiou"
z = "".join([x for x in input if x not in vowels])
print(input)  #Hello World!
print(z)      #Hll Wrld!