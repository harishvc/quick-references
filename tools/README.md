#UNIX Command Line Tools

`awk, find, sort, uniq, grep, sed`


##AWK: Quick Reference

source: http://www.tutorialspoint.com/awk/

    $>cat marks.txt
    1)    Amit     Physics    80
    2)    Rahul    Maths      90
    3)    Shyam    Biology    87
    4)    Kedar    English    85
    5)    Hari     History    89
    
###Print contents of the file with text at start and end
    $>awk 'BEGIN{print "start ..."} {print} END{print "end ..."}' marks.txt
             or
    $>awk 'BEGIN{print "start ..."} // END{print "end ..."}' marks.txt
             or
    $>cat marks.txt | awk 'BEGIN{print "start ..."} // END{print "end ..."}'                  
    start ...
    1)    Amit     Physics    80
    2)    Rahul    Maths      90
    3)    Shyam    Biology    87
    4)    Kedar    English    85
    5)    Hari     History    89
    end ...    	

###List only names
    $>awk 'BEGIN{printf "Name\n-----\n"} {print $2} ' marks.txt
    Name
    -----
    Amit
    Rahul
    Shyam
    Kedar
    Hari

###List lines that contain the pattern `ar`
    $>cat marks.txt | awk '/ar/' 
    4)    Kedar    English    85
    5)    Hari     History    89

###List lines that do not contain the pattern `ar`
    $>cat marks.txt| awk '!/ar/'
    1)    Amit     Physics    80
    2)    Rahul    Maths      90
    3)    Shyam    Biology    87

###Find #occurances of `ar`
    $>cat marks.txt| awk 'BEGIN{print "looking for pattern /ar/"} /ar/ {cnt++} END{print "#occurances =" , cnt}'
    looking for pattern /ar/
    #occurances = 2

###List names (column #2) that contain the pattern `ar`
    $>cat marks.txt| awk  ' $2 ~ /ar/ {print $2}'
    Kedar
    Hari

###List all the files that contain the pattern `TODO` :notes:  
`FILENAME` which contains the name of the file which is currently being worked on.   
`nextfile` is a awk command to quit the current file and start working on a new file  
File names are listed only once even when the pattern can occurs more than once       
`BEGIN{IGNORECASE=1}` ignore case       

    $>awk 'BEGIN{IGNORECASE=1} /TODO/ {print FILENAME;nextfile}' ~/projects/*  
    ~/projects/1.py  
    ~/projects/5.py  

    $>grep -nr "TODO" ~/projects/*
    ~/projects/1.py  
    ~/projects/5.py  
  

### List all the files that contain the pattern `TODO`  from a tar.gz archive
[Several options posted on Stackoveflow](http://stackoverflow.com/questions/13983365/grep-from-tar-gz-without-extracting-faster-one)   
```    
    $>tar -zxvf projects.tar 
    $>for file in ./projects/*
        do
           awk 'BEGIN{IGNORECASE=1} /TODO/ {print FILENAME;nextfile}' $file
        done
```

## Unix commands for trouble shooting
```ping```  Check connectivity between client and server (or between two locations). Operates at Level3 of OSI  


```nslookup``` Query the Domain Name System (DNS) to obtain domain name or IP address  


```traceroute``` Diagnostic tool for displaying the route (path) from source to destination. Useful in measuring transit delays of packets  


```top```  Provides a snapshot of all the processes running on the machine, CPU, Memory, I/O and lot of useful metrics


```netstat``` shows network status on a specific machine
```
#show all sockets
$>netstat -a

#list open listining ports
$>netstat -a | grep LISTEN
tcp4       0      0  *.17500                *.*                    LISTEN     
tcp6       0      0  *.17500                *.*                    LISTEN 

$>lsof -i :17500
COMMAND PID     USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
Dropbox 326 harishvc  114u  IPv6 0x266b01c2d53a2611      0t0  TCP *:17500 (LISTEN)
Dropbox 326 harishvc  118u  IPv4 0x266b01c2d4e27000      0t0  TCP *:17500 (LISTEN)
Dropbox 326 harishvc  121u  IPv4 0x266b01c2d495d3bv      0t0  UDP *:17500
```



```ps``` List all processes running on the machine - PID, time, CMD

```uptime``` List sytem uptime, users and load average


```lsof``` List of open files
```
#List all open files
$>lsof 

#List all files with connections 'LISTENING & ESTABLISHED’
#there are several UDP states - unbounded , idle
$>lsof -i

#list all the running process of open files of TCP Port ranges from 1-1024
$>lsof -i TCP:1-1024

#list all active processes listening on port 80
$>lsof  -i :80

#List all open file of a user
$> lsof -u #pid#

#List all open file of a process
$> lsof -p #pid#
```

##Additional Resources
* [grep vs awk : 10 examples of pattern search](http://www.theunixschool.com/2012/09/grep-vs-awk-examples-for-pattern-search.html)

