#AWK: Quick Reference

source: http://www.tutorialspoint.com/awk/

    $>cat marks.txt
    1)    Amit     Physics    80
    2)    Rahul    Maths      90
    3)    Shyam    Biology    87
    4)    Kedar    English    85
    5)    Hari     History    89
    
##Print contents of the file with text at start and end
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

##List only names
    $>awk 'BEGIN{printf "Name\n-----\n"} {print $2} ' marks.txt
    Name
    -----
    Amit
    Rahul
    Shyam
    Kedar
    Hari

##List lines that contain the pattern `ar`
    $>cat marks.txt | awk '/ar/' 
    4)    Kedar    English    85
    5)    Hari     History    89

##List lines that do not contain the pattern `ar`
    $>cat marks.txt| awk '!/ar/'
    1)    Amit     Physics    80
    2)    Rahul    Maths      90
    3)    Shyam    Biology    87

##Find #occurances of `ar`
    $>cat marks.txt| awk 'BEGIN{print "looking for pattern /ar/"} /ar/ {cnt++} END{print "#occurances =" , cnt}'
    looking for pattern /ar/
    #occurances = 2

##List names (column #2) that contain the pattern `ar`
    $>cat marks.txt| awk  ' $2 ~ /ar/ {print $2}'
    Kedar
    Hari

##List all the files that contain the pattern `TODO` :notes:  
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
  

##List all the files that contain the pattern `TODO`  from a tar.gz archive
//Several options at http://stackoverflow.com/questions/13983365/grep-from-tar-gz-without-extracting-faster-one
    $>tar -zxvf projects.tar 
    $>for file in ./projects/*
        do
        awk 'BEGIN{IGNORECASE=1} /TODO/ {print FILENAME;nextfile}' $file
        done

##Find file names that match a pattern


##Additional Resources
* [grep vs awk : 10 examples of pattern search](http://www.theunixschool.com/2012/09/grep-vs-awk-examples-for-pattern-search.html)

