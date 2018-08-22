# UNIX Quick Reference

# What is a process id?
Process ID (PID) is unique identifier. A PID is automatically assigned to each process when it is created.

## How can find a process id?
```unix
$ps -ef
#e - Display information about other users' processes, including those without controlling terminals
#f - Display the uid, pid, parent pid, recent CPU usage, process start time, controlling tty
#run man ps for more information
```

## How to find all process running on the unix machines?
```
$top

$pstree  #pid# #depends on unix distribution

$ps -ef
```

## How do you kill a process?
* `Kill` has several signal names and numbers
```unix
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
```unix
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
$kill -s SIGQUIT #Terminates a process. Generates a core dump of the process and also cleans up resources held up by a process
$kill -s SIGSTP  #Suspends a process
$kill -s SIGCONT #Resume a suspended process
```

## What is `sudo`?
* System administrators can give certain users or groups access to certain commands using `sudo` without those users having to know the `root` password.
* `sudo` command stands for `superuser do`.
* All activity is logged


## What is the difference between process and thread?
* Process 
** Each process has a virtual address space, executable code, open handles to system objects, a security context, unique process identifier, 
   environment variables and at least one thread of execution
** Run in separate memory spaces
** Each process is started with a single thread, often called the primary thread.
* Threads 
** A thread is a subset of the process.
** It is termed as a ‘lightweight process’
** All threads of a process share its virtual address space and system resource
** Each thread maintains an unique identifier, own exception handlers, thread local storage and security context

Reference:
1. https://stackoverflow.com/questions/200469/what-is-the-difference-between-a-process-and-a-thread


## How to run a process in the background?
```unix
$>python hellpworld.py &  #add &
```

## What is `stdin`, `stdout` & `stderr`?
`stdin`, `stdout` & `stderr` are I/O streams and are special files in `/dev` folder
* `/dev/stdin`  for a stream input
* `/dev/stdout` for a stream out
* `/dev/stderr` for errors out
```unix
$>cat < /etc/passwd > /tmp/123.txt 2> /tmp/err
$>cat help.txt 2> /tmp/null  #sent error to /dev/null
```

## What is `/dev` and `/proc`?
* Files in `/dev` are either character or block devices connected to a device driver! They don't have a size. Example `stdin`, `stdout` & `stderr`
* `/proc` is a special virtual filesystem in Linux to keep track of runtime system information. They have size 0.

## What is a `core` dump?
A process dumps core when it is terminated by the operating system due to a fault in the program.

## What is a system call? [TODO]

## Explain `ptrace`? [TODO]

## Explain `strace`? [TODO]





