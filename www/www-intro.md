# WWW Quick Reference - Part I

## OSI Layer
 
Open Systems Interconnection (OSI)) is **reference model** that shows how  applications communicate over a network. A reference model is a **conceptual framework** for understanding relationships. 
* Layer 7: Application layer
* Layer 6: Presenation layer. Data encryption is handled
* Layer 5: Session layer. Services include authentication and reconnection (IP)
* Layer 4: Transport layer. On the internet, TCP and UDP provide these services for most applications
* Layer 3: Network layer handles routing of the data. IP is the network layer for the Internet (router)
* Layer 2: The data link layer. Ethernet is the main data link layer (switch)
* Layer 1: Physical Layer provides the hardware for sending and receiving data (hub)

## Why do we need SSL?
SSL (Secure Sockets Layer) is a security protocol responsible for establishing an encrypted (secure) link between a web server and a browser

## What is a digital certificate?
* SSL digital certificates are signed by Certificate Authority (CA), after verifying identity of an applicant. 
* After verification, digital certificates are issued along with Intermediate certificate that tie back to CA root certificate

## Steps to create digital certificate?
* Create private and public keys
* Store private keys in a secure place accessible by webserver
* Generate Certificate Signing Request (CSR) using the public key
* Submit the CSR to a Certificate Authority (CA)
* CA will provide you a SSL digital certificate for your domain and intermediate certificate
* Upload the SSL digital certificate and intermediate certificate on your server and then configure your webserver
* Intermediate certificate establishes the credibility of your certificate by tying it to your CA root certificate
* SSL digital certificates are signed by Certificate Authority (CA), after verifying identity of an applicant

References:
1. https://www.digicert.com/ssl/
2. https://blog.ragnarson.com/2013/10/18/why-do-we-need-ssl.html

## TCP/IP vs UPD?
TCP/IP
* TCP is connection oriented - 3 way handshake
* TCP guarantees (in-order) packet delivery
* Example: HTTP,SMTP, SSH    

UPD
* UPD is connection less
* Ideal for low latency
* Examples: DNS, streaming movie, online gaming


## What is Domain Name Service?
* DNS is the phonebook of the Internet
* In a nutshell DNS transalates URL's to IP address 

References:
1. https://www.cloudflare.com/learning/dns/what-is-dns/
2. https://aws.amazon.com/route53/what-is-dns/
3. https://developers.google.com/speed/public-dns/

## Why is DNS propagation slow?
* Entires in DNS have TTL that make take longer


## How do you change DNS? [TODO]

## How can you do a reverse lookup? [TODO]

## What is firewall?
Firewall is part of a computer system or network that is designed to *block unauthorized access* while permitting outward communication


## What is REST API?
* Representational State Transfer (REST)
* Takes advantage of HTTP - no need to install libraries or additional software!
* REST does not maintain state

## Explain `no route to host`? [TODO]

## Explain `request timedout`? [TODO]

## Howto generate a TCP dump? [TODO]


## Proxy vs Reverse Proxy
* Proxy: Website retrieves information on-behalf of someone else. Example: People is specific subnet blocked from local news. Proxy server can access news.
* Reverse Proxy: Load balancing traffic or running services on non-standard port

Reference:
1. https://stackoverflow.com/questions/224664/difference-between-proxy-server-and-reverse-proxy-server

## What is a name based virtual server?
* Webserver is configured to host name based virtual domains
* DNS configured to resolve name name based virtual domains
```
Non-authoritative answer:
Name:	harishvc.com
Address: 104.31.65.151
Name:	harishvc.com
Address: 104.31.64.151
```


## Cookie vs Cache  (```chrome://net-internals```)

### Cookie
* Cookie is a very small encrypted text file which is stored on the client’s machine by the web site using the browser and is sent back to the server each time a page is requested
* Cookies expire afer a specific time (determined by the application setting the cookie)
* Browser preference can be modified to handle cookie - block site, remove after browser is closed

### Cache
* Use by browsers to make the loading of web pages faster
* Cache is kept in the client’s machine until they are removed manually by the user.

## Session vs Token based Authentication 
* In **Session based Authentication** heavy lifting is done on the server side. After successful login, `sessionID` is generated and stored in the browser in cookies.
Future requests use this `sessionID`. Based on browser setting on expiration set by the server `sessionID` will expire and new one generated. Ideal for public - no prior signup needed
* Token are ideal for API based requests. Tokens are included in the request header to various end-points. Tokens are usually associated with an user. Works well since it is stateless. Ideal for API requests - developers have to sign up for a token 

## What happens when a web page is requested?
* http://programmers.stackexchange.com/questions/211176/in-need-of-a-more-technical-answer-for-an-interview-question-about-how-the-inter
* http://www.howtogeek.com/138771/htg-explains-how-latency-can-make-even-fast-internet-connections-feel-slow/


## HTTP status codes
200 - Ok  
301 - permament redirection (retains SEO juice!)  
302 - temporary redirection  
304 - not modified  
403 - Directory index listing not allowed    
404 - Page not found  
500 - Server Error  


## HTTP request methods
* GET     - Request data from a specific source
* PUT     - Submit data to a specific source to process
* HEAD    - Same as GET but returns headers no other content
* PUT     - uploads a specific URI
* DELETE  - delete a specific URI
* OPTIONS - Shows all the request methods HTTP supports
* CONNECT - Converts the request connection to a transparent TCP/IP tunnel


## Explain TCP Flags

There are 6 TCP flags. [More information about TCP Flags](http://www.firewall.cx/networking-topics/protocols/tcp/136-tcp-flag-options.html)  


##  What is a recommended page load time?
* Page Load Time consists of two components: 1) network and server response time and 2) browser time   
* **Server response time** is the time it takes for a server to return the initial HTML, factoring out the network time
* Under a second (on desktops) and less than 200 ms on mobile


## How can you improve the page load time?
* https://moz.com/learn/seo/page-speed

## What is HTTP pipelining & persistence?  

### Pipelining
* HTTP pipelining is a technique in which multiple HTTP requests are sent on a single TCP connection without waiting for the corresponding responses.
* Pipelining of requests results in a dramatic improvement
* Pipelining was introduced in HTTP/1.1

### Persistence
* HTTP persistent connection, also called **HTTP keep-alive** is the idea of using a single TCP connection to send and receive multiple HTTP requests/responses, as opposed to opening a new connection.
* Lower CPU and memory usage (because fewer connections are open simultaneously)
* Reduced latency in subsequent requests (no handshaking)
```
Connection: keep-alive
```

## HTTP headers
```
$>curl -I http://foo.com
HTTP/1.1 200 OK
Date: Thu, 20 Oct 2016 06:17:38 GMT
Server: Apache
Last-Modified: Tue, 18 Oct 2016 01:04:55 GMT
Accept-Ranges: bytes
Cache-Control: max-age=12345
Expires: Fri, 21 Oct 2016 06:17:38 GMT
Vary: Accept-Encoding
Content-Type: text/html
```

## References  
* [Back of the envelope calculations](http://highscalability.com/blog/2011/1/26/google-pro-tip-use-back-of-the-envelope-calculations-to-choo.html)
* http://www.yegor256.com/2015/11/16/json-vs-xml.html
* [More information about headers](https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers)



