#Solving problems using Python 

##Table of Contents
  * [Solving problems using Python](#solving-problems-using-python)
    * [Q1: Join elements in an array](#q1-join-elements-in-an-array)
    * [Q2: Pop elements in an array](#q2-pop-elements-in-an-array)
    * [Q3: Print n elements in a string](#q3-print-n-elements-in-a-string)
    * [Q4: Get more information about python modules](#q4-get-more-information-about-python-modules)
    * [Q5: String concatenation](#q5-string-concatenation)
    * [Q6: One line if else statement](#q6-one-line-if-else-statement)
    * [Q7: Time now is epoch milliseconds](#q7-time-now-in-epoch-milliseconds)
    * [Q8: Find if substring exists in a string](#q8-find-if-substring-exists-in-a-string)
    * [Q9: What is the data type?](#q9-What-is-the-data-type?)
    * [Q10: Iterate Dictionary](#q10-Iterate-Dictionary)
    * [Q11: Convert integer to binary (base 2)](#q11-convert-integer-to-binary-base)
    * [Q12: Iterate array of key,value pairs](#q12-iterate-array-of-keyvalue-pairs)
    * [Q13: Find all directories (not recursive) inside a folder](#q13-find-all-directories-not-recursive-inside-a-folder)
    * [Q14: Given page URL, find the page title inside ](#q14-given-page-url-find-the-page-title-inside-)
    * [Q15: Open file and process line by line](#q15-open-file-and-process-line-by-line)

##Q1: Join elements in an array
    a1 = ['this','is','a','sentence']      
    a2 = '### '.join(a1)      
    print a2

##Q2: Pop elements in an array
    a1 = ['this','is','a','sentence']
    print a1.pop(-1) #last element in array
    print a1.pop(0) #first element in array
    print a1.pop(1) #new second element in array

##Q3: Print n elements in a string
    a1 = "Hello World!"
    #print 5 characters starting from position 0
    print a1[0:5] #Hello  

##Q4: Get more information about python modules
    $>pip freeze   #list all python modules and their version
    $>pip freeze > requirements.txt #generate requirements file
    $>pip show py2neo  #show information about py2neo; output includes version #
    
##Q5: String concatenation
    $>a = "Hello"
    $>b = "World"
    $>c = a + " " + b     
    $>print c  #Hello World

##Q6: One line if else statement
    a = 1 if (b > 1) else 0  
    #same as
    if (b >1):
	a = 1
    else:
	a = 0

##Q7:Time formatting
    #Time now in epoch milliseconds
    #Python 2.7.x
    import datetime
    print int(datetime.datetime.now().strftime("%s")) * 1000    

    #Python 3.4.x
    import time
    print(int(time.time()) *1000)

    #Convert time stamp to epoch
    #Python 3.4.x
    import datetime
    import pytz
    timestampZ = "2015-10-23T13:40:00-08:00"
    tz_UTC = pytz.timezone('US/Pacific')
    timestamp, _, zone= timestampZ.rpartition("-")
    time_format = "%Y-%m-%dT%H:%M:%S"
    naive_timestamp = datetime.datetime.strptime(timestamp, time_format)
    aware_timestamp = tz_UTC.localize(naive_timestamp)
    epoch = aware_timestamp.strftime("%s")
    print(int(epoch))

##Q8: Find if substring exists in a string
    a = "Hello world" #string
    b = "world"       #sub-string
    if b in a:
	print "found"

##Q9: What is the data type?
    a = []
    print type(a)
    b = {}
    print type(b)

##Q10: Iterate Dictionary 
    vowels = {8: 'a', 3: 'e', 2: 'i', 9: 'o', 1:'u'}
    print  vowels.keys()               #print all keys
    print  vowels.values()             #print all values
    
    for k, v in vowels.iteritems():
        print k, v                     #print keys and values
    vowels.pop(1)                      #remove key=1

    for k in vowels.iterkeys():
        print k                        #print keys

    for v in vowels.itervalues(): 
        print v                        #print values

    print max(vowels.keys(), key=int)  #print max key


##Q11: Convert integer to binary (base 2)
    input = 6
    print bin(input)[2:]  #110


##Q12: Iterate array of key,value pairs
    people.append({"lastname":'a', "fullname":'a bc', "url": 'abcd'})
    ...
    #sort by last name
    people.sort(key=lambda people_item: people_item['lastname'],reverse=False)	


##Q13: Find all directories (not recursive) inside a folder
    #Source: http://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
    def listdirs(folder):
       return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
    
##Q14: Given page URL, find the page title inside <title></title>
    #Source: http://stackoverflow.com/questions/51233/how-can-i-retrieve-the-page-title-of-a-webpage-using-python

    from BeautifulSoup import BeautifulSoup
    from mechanize import Browser

    def PageTitle(url):
     try:
        br = Browser()
        res = br.open(url)
        data = res.get_data()
        soup = BeautifulSoup(data)
        htmltitle = soup.find('title')
        title = []
        title = (htmltitle.renderContents()).split("|")
        return title[0].rstrip()
    except:
        print "error trying to access", url
        return ""


##Q15: Open file and process line by line
    with open(filename) as fp:
        for line in fp:
            print(line.rstrip())



[![Analytics](https://ga-beacon.appspot.com/UA-55381661-1/tools/cmd/readme)](https://github.com/igrigorik/ga-beacon)
