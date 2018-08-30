# Introduction to Networking (part 1)

## OSI Layer
 
Open Systems Interconnection (OSI)) is **reference model** that shows how  applications communicate over a network. A reference model is a **conceptual framework** for understanding relationships. 
* Layer 7: Application layer
* Layer 6: Presenation layer. Data encryption is handled
* Layer 5: Session layer. Session between computers are **established, managed, and torn down**
* Layer 4: Transport layer. **Logical connection** between host and destination. On the internet, TCP and UDP provide these services for most applications
* Layer 3: Network layer handles routing of the data. Internet Protocol (IP) is the standard for routing packets. Gateway, Firewall, Routers, DHCP are in Layer 3 
* Layer 2: The data link layer. Ethernet is the main data link layer (switch). MAC address is used in this layer. This layer is responsible for providing **reliable data transfer**, identify and fix **transmission errors**
* Layer 1: Physical Layer provides the hardware for sending and receiving data (hub)

## Protocols & PORT
```
HTTP:  80 ,443
DNS (named): 53
SSH: 22
SMTP: 25
```

## What is MAC address? How is it used?
 - MAC address is a **physical address**
 - Media Access Control (MAC) address is an unique identifier associated with each individual network device (wireless card, ethernet card, wireless access point)
 - MAC numbers are embedded into the hardware during the manufacturing process
 - MAC addresses is a 6 set of 2 hexadecimal values seperated by `:` 
 - 48-bits address 
 - Operates at OSI Layer 2

## What is IP address?
- **Logical address** of the network interface connected to the internet - changes when you move from one network to another!
- Operates at OSI Layer 3
- 4 sets of numbers separated by `dotted decimal`. Each set represents a 8-bit number ranging from (0-255)
- 32-bit address


## What is Class A,B,C,D,E network?
- IP address is 4 sets of 8 bits (total 32 bits = 4 bytes)
- Class A: Highest bit is set to 0, and contains 7 bits for network number & 24 bits for host number
- Class B: Highest bit is set to 10, and contains 14 bits for network number & 16 bits for host number
- Class C: Highest bit is set to 110, and contains 21 bits for network number & 8 bits for host number
- Class D: Highest bit is set to 1110 to support multicasting
- Class E: Highest bit is set to 1111 reserved for experimental use

## What is the purpose of a subnet mask?
 - A subnet mask contains four bytes (32 bits) and is often written using the same `dotted-decimal` notation as IP address
 - Applying the subnet mask to an IP address splits the address into two parts - network address, host address
 - For a subnet mask to be valid, leftmost bit must be set to `1` and right most bit must be set to `0` 
 - Subnet allows network administrators some flexibility in **defining relationships** among machines in the same network address


## What is the purpose of 127.0.0.1?
- `127.0.0.1` is the loopback IP address also referred to as the `localhost`
- Lookback address is used by the computer to communicate with itself - mainly for diagnostics and troubleshooting
- Loopback address is used by protocols such as OSPF to determine specific properties on the device
- Since loopback interface address never changes it is the preferred method for **device identification**


## What is firewall?
Firewall is part of a computer network and has set of rules designed to **block unauthorized access**

## What is a default gateway?
The default gateway that you see is a node on your network which acts as a **bridge to the outside world**. It is usually the **IP address of your router**.

## What is `NAT`?
- Reference: https://whatismyipaddress.com/nat
- Network Address Translation (NAT) is the process where a network device, usually a firewall, assigns a public address to a computer (or group of computers) inside a private network
- The main use of NAT is to limit the number of public IP addresses an organization or company must use, for both economy and security purposes

## What is my IP address?
- On Windows issue  `cmd` to open a window and then type `ipconfig` 
- On Linux/OS X issue `ifconfig`  and look for IP address of wireless or wired device

## Explain Internet Control Message Protocol (ICMP)?
- The Internet Control Message Protocol (ICMP) is a **supporting protocol** in the **Internet Protocol suite**
- Used by network devices (example: routers) to send error messages and operational information 
- Example: requested service is not available or router could not be reached

## Explain Address Resolution Protocol (ARP)?
- Reference: https://www.tummy.com/articles/networking-basics-how-arp-works/
- Address Resolution Protocol (ARP) is a network layer protocol used to **convert** an IP address into a physical address (MAC address)
- A lookup (ARP) table is used to maintain a correlation between each MAC address and its corresponding IP address
- If the IP address is not found in the ARP table, using the `ARP` protocol a **broadcast packet** sent the network asking `who has a.b.c.d`
- Any machine with the requested IP address will reply back using the `ARP` protocol `I am a.b.c.d`
- Where multiple machines have the same IP address, you may get multiple responses and one that gets placed in the ARP table can vary depending on the networking implementation!
- Display ARP in linux
```bash
$>arp -an | grep 10
? (10.0.0.199) at a:b:c:d:f on en0 ifscope [ethernet]
? (10.0.0.191) at (incomplete) on en0 ifscope [ethernet]
```

## Explain `ping`?
- Ping is a **network diagnostic tool** used to diagnose if a target device is **reachable**
- Ping works by sending an `ICMP` `Echo Request` to a specified target device and waits for a `Echo Response`
- Ping repeats (until interrupted) and displays `bytes sent`, `ttl` and `time`. In the end average `round-trip time` is calculated and displayed
- Monitor network availability, can't `ping` ports (since ports are part of Transport Layer)
```bash
$ping harishvc.com (104.31.64.151): 56 data bytes
64 bytes from 104.31.64.151: icmp_seq=0 ttl=56 time=13.024 ms
64 bytes from 104.31.64.151: icmp_seq=1 ttl=56 time=19.584 ms
64 bytes from 104.31.64.151: icmp_seq=2 ttl=56 time=14.492 ms
^C
--- harishvc.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 13.024/15.700/19.584/2.811 ms
```

## Explain `traceroute`?
- Reference: https://www.youtube.com/watch?v=G05y9UKT69s
- `traceroute` is a **network diagnostic tool** used to determine **path packets** are taking to the destination
- path includes routers, computers or any other devices
- `TTL` value is incremented until the packet reaches the destination
- Router receiving a packet with `TTL` of 1  sends back to the original sender an ICMP response "TTL exceeded" - path is determined!
- Limitations: Routers have to be configured to send `ICMP` response, network has to *allow* the `ICMP` response to come back to the original sender



## List all open ports currently in use?
- On Linux/OS X issue `netstat`
- Additional flags to filter by `listening sockets`, `port number`, `tcp ports`, `udp ports`

## Is a specific service running on a target machine?
- Use `nmap`
- `nmap` ("Network Mapper") is an open source tool for network exploration and security auditing. It was designed to rapidly scan large networks.
- Example: Check if port 80 is open in `harishvc.com`
```bash
$>nmap -p 80 harishvc.com
...
...
PORT   STATE SERVICE
80/tcp open  http
```

## What is `tcpdump`?
- `tcpdump` is a tools for gathering all network traffic on the machine
- Example: `$tcpdump -i eth0 -port 8080 -src x.x.x.x -w output_file` gathers all network traffic on interface `eth0` on port `8080` from `x.x.x.x` and saves to output file! 

## Explain `no route to host`?
- `no route to host` means that your computer can’t reach the host (target) server
- Troubleshooting tips: is host running? check port, check iptables, ping by ip, ping by server name, check `/etc/hosts.allow`, `/etc/hosts.deny`  


## Explain `request timedout`?
- `request timed out` means that the host did not receive a response. 
- This error could be caused by firewall rules, routing error or packet filtering


## Anatomy of UDP Packet [TODO]
- Reference: https://www.techrepublic.com/article/exploring-the-anatomy-of-a-data-packet/


## Anatomy of TCP packet [TODO]
- Reference: https://www.techrepublic.com/article/exploring-the-anatomy-of-a-data-packet/


 
## TCP/IP vs UPD?
TCP/IP
* TCP is connection oriented - 3 way handshake, **reliable**
* TCP guarantees (in-order) packet delivery 
* Example: HTTP,SMTP, SSH    

UPD
* UPD is connection less
* Ideal for **low latency**
* Examples: `traceroute`, DNS, streaming movie, online gaming

## Does TCP and UDP use IP?
- Yes, TCP and UDP (layer 4) use IP (layer 3). However both the protocols work differently
- `TCP/IP` is referred to the `Internet Protocol Suite`


## Explain TCP Connection Establishment

![TCP/IP connection and termination](tcp-ip-setup-disconnect.png)

### Working
- Before a client attempts to connect with a server, the server must first bind to and listen on port - **passive open**. Once the passive open is established, a client may initiate an **active open**.
- `SYN`: The active open is performed by the client sending a `SYN` to the server. The client sets the segment **sequence number** to a random value A.
- `SYN-ACK`: server replies with  `SYN-ACK`. The acknowledgment number is set to **one more than the received sequence number i.e. A+1**, Server chooses nother random number, B as the sequence number. Connection is established on client side.
- `ACK`: Client sends `ACK` with `B+1` back to the server. Connection is established on server side.

### References
- 1. https://en.wikipedia.org/wiki/Transmission_Control_Protocol
- 2. https://www.geeksforgeeks.org/computer-network-tcp-3-way-handshake-process/
- 3. https://www.youtube.com/watch?v=Ad38n2hYOuA  
- 4. http://www.cs.northwestern.edu/~agupta/cs340/project2/TCPIP_State_Transition_Diagram.pdf

## Explain TCP Connection Termination
- `CLOSE_WAIT` indicates that the remote endpoint (server) has closed the connection [4] 
- `TIME_WAIT` indicates that local endpoint (client) has closed the connection [4]
- The connection is being kept around so that any **delayed packets** can be matched to the connection and handled appropriately [4]
- The connections will be removed when they time out [4]

### References
- 1. https://en.wikipedia.org/wiki/Transmission_Control_Protocol
- 2. https://www.performancevision.com/blog/close-tcp-sessions-diagnose-disconnections
- 3. https://www.youtube.com/watch?v=Ad38n2hYOuA
- 4. https://superuser.com/questions/173535/what-are-close-wait-and-time-wait-states


## What is Domain Name Service?
* DNS is the phonebook of the Internet
* DNS is  **hierarchical**  and **decentralized** 
* DNS works by **delegating the responsibility**  by **designating authoritative name servers** for resolution
* In a nutshell DNS transalates URL's to IP address  (forward lookup)
* In Linux, DNS server information is stored in `/etc/resolv.conf`

References:
1. https://www.cloudflare.com/learning/dns/what-is-dns/
2. https://aws.amazon.com/route53/what-is-dns/
3. https://developers.google.com/speed/public-dns/

## Explain DNS forward lookup?
https://www.youtube.com/watch?v=3EvjwlQ43_4


## Why is DNS propagation slow?
* Entires in DNS have TTL that make take longer


## How do you change DNS? [TODO]
In Linux, DNS server configuration is stored in `/etc/resolv.conf`


## How can you do a reverse lookup?
1. https://www.youtube.com/watch?v=Br8mzFu5EgA
2. https://www.youtube.com/watch?v=hYZY75xMjlY (using `dig`)


## What is Name Based Server?
- **Name based virtual server** hosting refers to hosting multiple domains on `1` IP address
- DNS can be configured to have a `CNAME` entry that maps the name based server to the IP address
- Apache can be then configured to resolve the name based server
- Name based virtual hosting also eases the demand for scarce IP addresses


## What happens when a web page is requested?
* http://programmers.stackexchange.com/questions/211176/in-need-of-a-more-technical-answer-for-an-interview-question-about-how-the-inter
* http://www.howtogeek.com/138771/htg-explains-how-latency-can-make-even-fast-internet-connections-feel-slow/


## What is a name based virtual server?
* Webserver is configured to host name based virtual domains
* DNS configured to resolve name name based virtual domains
```bash
$>nslookup harishvc.com

Non-authoritative answer:
Name:	harishvc.com
Address: 104.31.65.151
```

## IMAP vs POP? [TODO]
- Reference: https://www.youtube.com/watch?v=BK4ng6Gcits

