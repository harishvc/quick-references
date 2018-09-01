# UNIX/Linux Quick Reference


## Explain Linux run levels

Run Level   | Mode   |  Action
---           ---       ---
0 |  Halt| Shuts down system  
1   |  Single-User Mode |  Does not configure network interfaces, start daemons, or allow non-root logins  
2   |  Multi-User Mode  |  Does not configure network interfaces or start daemons  
3   |  Multi-User Mode with Networking | Starts the system normally (**default for server**)  
4   |  Undefined | Not used/User-definable  
5   |  Run level 3 + display manager(X)   |  Start system normally with display manager (**default for desktops**)  
6   |  Reboot |  Reboots the system

- file `/etc/inittab` tells the `init` daemon what run level the system should enter by default
- `init` deamon is the first process that starts in a Linux system after the machine boots 
- `init` deamon has a PID of `1` -  parent of all other processes! 
 
## Explain file permissions?
```bash
$> ls -l test.py
-rw-r--r-- 1 harishvc  staff  01 Jan 18 05:13 test.py
#-                     rw-   r--       r--
#^                     ^     ^         ^
#file/directory        user  group     world
#r = read
#w = write
#x = execute
#first  three positions (after the "-" or "d") show user permission
#second three positions show group permission
#third three positions  show world permission
``` 

## Command to change file permission
numeric |  binary |  permission  
---      ---       ---

0   |   000   |   ---  
1   |   001   |   --x  
2   |   010   |   -w-  
3   |   011   |   -wx  
4   |   100   |   r--  
5   |   101   |   r-x  
6   |   110   |   rw-  
7   |   111   |   rwx  

```bash
$chmod 755 test.py  #rwxr-xr-x
$chmod 700 test.py  #rwx------
$chmod 644 test.py  #rw-r--r--
$chmod -R 755 ./test_dir  #recursively apply permission on a directory
```

## Explain `sticky` bit?
- A `sticky` bit is a permission bit that is set on **directory** or **file** that allows only the owner of the file within that directory or the root user to delete or rename the file(s)
- `/tmp` folder is where `sticky` is enabled since all users of the system have temporary files
```bash
$ls -l | grep delete-dir
drwxr-xr-x  2 harishvc  staff    68 Aug 27 05:48 delete-dir
#
#enable sticky bit on the directory - world has `t` since executable
harishvc@surya:~/nextChallenge18/google>chmod 1755 delete-dir
harishvc@surya:~/nextChallenge18/google>ls -l | grep delete-dir
drwxr-xr-t  2 harishvc  staff    68 Aug 27 05:48 delete-dir
#
#enable sticky bit on the directory - world has `T` since it is not executable
harishvc@surya:~/nextChallenge18/google>chmod 1754 delete-dir
harishvc@surya:~/nextChallenge18/google>ls -l | grep delete-dir
drwxr-xr-T  2 harishvc  staff    68 Aug 27 05:48 delete-dir
#
#remove stick bit
harishvc@surya:~/nextChallenge18/google>chmod 0754 delete-dir
harishvc@surya:~/nextChallenge18/google>ls -l | grep delete-dir
drwxr-xr--  2 harishvc  staff    68 Aug 27 05:48 delete-dir
#
```

## Explain `SUID` and `SGID`
- When a program is executed by person X it is executed with permissions of person X (located in `group` or `other`)
- However is some special case (example: changing password), you want the program to be executed as the person who `owns` the program
- When you execute a program that has set user id `SUID` or set group id `SGGID` bits set, you **inherit the permissions of the program owner**
```bash
#
harishvc@surya:~/nextChallenge18/google>touch delete.py
harishvc@surya:~/nextChallenge18/google>chmod 644 delete.py 
harishvc@surya:~/nextChallenge18/google>ls -l delete.py 
-rw-r--r--  1 harishvc  staff  0 Aug 27 06:42 delete.py
#
#set SUID
harishvc@surya:~/nextChallenge18/google>chmod 4644 delete.py 
harishvc@surya:~/nextChallenge18/google>ls -l delete.py 
-rwSr--r--  1 harishvc  staff  0 Aug 27 06:42 delete.py
#set SGID
harishvc@surya:~/nextChallenge18/google>chmod 2644 delete.py 
harishvc@surya:~/nextChallenge18/google>ls -l delete.py 
-rw-r-Sr--  1 harishvc  staff  0 Aug 27 06:42 delete.py
#set Sticky bit
harishvc@surya:~/nextChallenge18/google>chmod 1644 delete.py 
harishvc@surya:~/nextChallenge18/google>ls -l delete.py 
-rw-r--r-T  1 harishvc  staff  0 Aug 27 06:42 delete.py
```


## How many bits are there to set UNIX permission?
- Reference: https://unix.stackexchange.com/questions/447334/what-are-the-final-3-bits-in-the-unix-permission-mode-bits
- There are `12` bits used to set permissions
```text
bits            000     000    000    000
permissons      suSGt   uuu    ggg    ooo

su   -> SUID
SG   -> SGID
t    -> Sticky Bit
uuu  -> user
ggg  -> group
ooo  -> other     
```

## What is `umask`?
- Reference: https://www.computerhope.com/unix/uumask.htm
- `umask` value is used to determine the **default** permissions of a created file
- each digit of the `umask` is **subtracted** from the  default value
- In Linux, the default permissions value is `666` for a regular file and `777` for a directory
- `umask 022` sets the file permission to `644` (666 - 022), `rw-r--r--`


## What is a process id?
Process ID (PID) is unique identifier. A PID is automatically assigned to each process when it is created.

## How can find a process id?
```unix
$ps -ef
#e - Display information about other users' processes, including those without controlling terminals
#f - Display the uid, pid, parent pid, recent CPU usage, process start time, controlling tty
#run man ps for more information
```

## How to find all process running on the unix machines?
```bash
$top  #all processes on the machine
#
#filter by pid
$top -pid #pid# 
#
#filter bu username
$top -U #username#


$pstree  #pid# #depends on unix distribution

$ps -ef
```

## What is PID `0` an `1`
There are two tasks with **specially distinguished process ID**
- `swapper` has process ID `0` and is responsible for **paging**, and is actually part of the kernel
- `init` has process ID `1`  and  responsible for **starting and shutting down the system**

## How can you find parent PID?
```
#solution 1
$>echo $PPID

#solution 2: Using `hoppid`
$>ps hoppid 5888
 PPID
 5887

>ps hoppid 5887
 PPID
 5886

~/Desktop>ps hoppid 5886
  PPID
    1      #init
```

## How do you kill a process?
* `Kill` has several signal names and numbers
```bash
$kill -l
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL
 5) SIGTRAP	 6) SIGABRT	 7) SIGEMT	 8) SIGFPE
 9) SIGKILL	10) SIGBUS	11) SIGSEGV	12) SIGSYS
13) SIGPIPE	14) SIGALRM	15) SIGTERM	16) SIGURG
17) SIGSTOP	18) SIGTSTP	19) SIGCONT	20) SIGCHLD
21) SIGTTIN	22) SIGTTOU	23) SIGIO	24) SIGXCPU
25) SIGXFSZ	26) SIGVTALRM	27) SIGPROF	28) SIGWINCH
29) SIGINFO	30) SIGUSR1	31) SIGUSR2	
``` 

* `kill` sends a `TERM` signal to the process to terminate. However, the process can ignore this request!
* A process can catch the`TERM` signal to handle termination gracefully and releasing resources
* A `KILL` signal can be issued to a process. `KILL` signal cannot be ignored and the process will be killed immediately
```bash
$> kill  #pid#    #TERM signal to the process to terminate. Process can ignore this request!
#
#
$kill -s KILL #pid#
$kill -s 9 #pid#
$kill -9 #pid#
#
#
#
$kill -s SIGINT  #Interrupts a process. This is the signal generated when a user presses Ctrl+C
$kill -s SIGQUIT #Terminates a process using CTRL + D . Generates a core dump of the process and also cleans up resources held up by a process
$kill -s SIGSTP  #Suspends a process
$kill -s SIGCONT #Resume a suspended process
```
## What happens when a process is killed?
Reference: https://stackoverflow.com/questions/389927/does-the-unix-kill-command-ensure-that-dynamically-allocated-memory-will-return
- When a process exits (normal or killed), the Unix OS does cleans up its memory allocations, file handles and other resources
- Each process runs in its own protected address space, and when the process ends (whether it exits voluntarily or is killed by an external signal) that address space is fully reclaimed by the OS
- The only resources that do not get cleaned up are those that are supposed to be shared, like the contents of files and of shared memory
- Many programs do not need to do any special cleanup on exit


## Can you ignore signals?
```bash
- Reference: http://www.tutorialspoint.com/unix/unix-signals-traps.htm
- `trap` command used for trapping signals
- if you ignore a signal, all subshells also ignore that signal
```bash
$> trap "rm -f $tmp/xx.* $tmp/yy*" 2  #delete $tmp/xx.* and $tmp/yy.* when signal #2 is received
$> trap '' 2   #ignore signal 2 (SIGINT)
```

## What happens when a new process is created?
- Reference: https://stackoverflow.com/questions/496702/can-a-shell-script-set-environment-variables-of-the-calling-shell


## What is `sudo`?
* System administrators can give certain users or groups access to certain commands using `sudo` without those users having to know the `root` password.
* `sudo` command stands for `superuser do`.
* All activity is logged


## What is the difference between process and thread?
### Process 
* Each process has a unique identifier, protected address space and **copy of parent's environment**
* Each process runs in its own **protected address space**, and when the process ends (whether it exits voluntarily or is killed by a signal) that address space is fully reclaimed
* Process has a **copy of the parent's environment** and no access to the parent process and environment. When the process terminates any changes to the **environment are lost**. 
* Each process is started with a single thread, often called the **primary thread**


### Thread
* A thread is a subset of the process.
* It is termed as a ‘lightweight process’
* All threads of a process share its virtual address space and system resource
* Each thread maintains an unique identifier, own exception handlers, thread local storage and security context

Reference:
1. https://stackoverflow.com/questions/200469/what-is-the-difference-between-a-process-and-a-thread


## How to run a process in the background?
```bash
$>python hellpworld.py &  #add &
```

## What is `stdin`, `stdout` & `stderr`?
`stdin`, `stdout` & `stderr` are I/O streams and are special files in `/dev` folder
* `/dev/stdin`  for a stream input
* `/dev/stdout` for a stream out
* `/dev/stderr` for errors out
```bash
$>cat < /etc/passwd > /tmp/123.txt 2> /tmp/err
$>cat help.txt 2> /tmp/null  #sent error to /dev/null
```

## What is `/dev` and `/proc` , `/dev/null`?
* Files in `/dev` are either character or block devices connected to a device driver! They don't have a size. Example `stdin`, `stdout` & `stderr`
* `/proc` is a special virtual filesystem in Linux to keep track of runtime system information. They have size 0.
* `dev/null` **special file** that is **always empty!** Data written to this device simply **disappear** - black hole where any data sent, will be discarded
```bash
$> less -f /dev/null     #empty
```

## Explain `>/dev/null 2>&1`
- Reference: https://unix.stackexchange.com/questions/163352/what-does-dev-null-21-mean-in-this-article-of-crontab-basics 
- `>/dev/null`  - send outoput to `/dev/null`
- `2>&1`       - send error to output  (`&` is the symbol for file descriptor)
- Redirect `Standard Err` and `Standard Out` to `/dev/null`


## What is a `core` dump?
A process dumps core when it is terminated by the operating system due to a fault in the program.

## How do you list all open files?
```bash
$> lsof   #list open files
```

## How to execute a script during boot?
 - `init` files are inside `/etc/`
 -  Scripts in appropriate run level starting with `S`  are run in `numeric` order with argument as `start` 
 ```bash
  /etc/rc0.d
  /etc/rc1.d   #run level 1
  /etc/rc2.d
  /etc/rc3.d
    -S01httpd   #start
    -K01httpd
    -S25test    #run after S01httpd
    -K25test
```

## Explain `strace`
- `strace` is used for real-time tracking of system calls.
```bash
$>strace #command#     #follow the command

$>strace -p #pid#            #follow pid

$>strace -c -p #pid#        #generate report of total time, calls, errors
```

## Explain `ptrace`  
- On Linux, `strace` uses `ptrace` for process tracking. 
- `ptrace` allows one process to **monitor, inspect , manipulate** the `internal state` of another process
- A process (tracker) can trace another by attaching to the process and temporarily becoming the process parent and watching


## Hardlink vs Softlink

### Hard Link 
 - Builds on **inode** (unique identifier for each file)
 - File content and name changes are picked up
 - When file is deleted, **content is still retained!**
 - Limitations
  - Only works on files - **no directories**
  - No visual indication
  - Does not work across different file systems
  - Extra care while deleting - delete more than one file
```bash
	$>ls -i h1.txt 
	8830981 h1.txt
	#
	$>ln h1.txt h2.txt
	$>ls -i h2.txt 
	8830981 h2.txt

	$>rm h1.txt 
	$>less h2.txt    #content still retained

	$>mkdir test
	$>ln test test2222
	ln: test: Is a directory
```

### Softlink (Symbolic link):
 - Changes to file contents are picked up
 - file rename or file deletion breaks the symlink
 - clear visual indication (blinking red when broken)
 - works on folders and files
 - works across mounted file systems
```bash
$>ls -i s1.txt 
8831201 s1.txt
#
$> ln -s s1.txt s2.txt  #create symlink
#
$>ls -i s2.txt 
8831213 s2.txt

$>ls -l s2.txt 
lrwxr-xr-x  1 harishvc  staff  6 Aug 27 02:37 s2.txt -> s1.txt
$>rm s1.txt                  
$>ls -l s2.txt 
lrwxr-xr-x  1 harishvc  staff  6 Aug 27 02:37 s2.txt -> s1.txt   #broken
#
#
$>less s2.txt 
s2.txt: No such file or directory
```


                               

