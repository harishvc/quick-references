#Back of the envelope calucalations

##Fun with Bits & Bytes

###Power of 2 table
| Power of 2    | Value         | Bytes  |
| ------------- |:-------------:| ------:|
| 2 ^ 10        | 1024          | 1 KB   |
| 2 ^ 20        | ~1 M          | 1 MB   |
| 2 ^ 30        | ~1 B          | 1 GB   |
| 2 ^ 40        | ~1 T          | 1 TB   |


## 20% of 1 Billion?
```
(10^9 X 20)/100  = 10^7 *20 = 200 *10^6 = 200 Million
```

## 1% of 1 Billion?
```
10^9/100 = 10^7 = 10X10^6 = 10 Million
```

## 10,000 ns to ms?
```
1. A millisecond is one thousandth of a second
2. A nanosecond is one billionth of a second
3. 1 ms = 10^6 ns

10,000/10^6 = 0.01 ms 

Reference:
http://www.calculateme.com/Time/Seconds/ToMilliseconds.htm
```

## How much time will it take to down a 256 KB File?
```
Let's assume you are connected to a high speed network at 10 Mbps

256 Kb = 2^8 * 10^3 * 2^3  = 2^11 * 10^3  = 2*2^10*10^3 = 2048 * 10^3 bits
10 Mbps = 10 * 10^6 bits

Time taken to download =  2048 * 10^3 / 10^7 = 0.21s

Reference:
http://www.t1shopper.com/tools/calculate/downloadcalculator.php
```

## How much space will 10M entires each of 8KB take?
```
#space/entry = 8 KB = 2^3 * 2^10  =  2^13 bytes
#entries = 10 M = 10 * 10^6 =  10 * 2^20 
#total space = 2^13 * 10 * 2^20 = 2^3 * 10 *2^30 = 80 * 2^30 = 80G  
```



##How much space does 256 Billion 32 bit integers take?
```
32 bits = 32/8 = 4 = 2^2 bytes
256 billion  32 bits = 2^8 * 2^30 * 2^2 = 2^40 bytes ~ 1 TB
```

## How many CHUNKS of 16G memory needed for 256 Billion bytes?
```
256 Billion Bytes = 2^8 * 2^30 = 2^38 bytes
16 G = 2^4 * 2^30  = 2^34 bytes
#chunks = 2^38/2^34 = 2^4 = 16
```

## How much integers can 16G hold?
```
1 32 bit integer = 4 bytes
16 G = 2^4 * 2^30 = 2^34
#intergers = 2^34/2^2 = 2^32 = 4* 2^30 = 4 Billion
```

## How would you reorder 9 TB of Google data in under 3 seconds using only 2 KB of memory?
```
source: https://www.quora.com/Google-Interview-Question-How-would-you-reorder-9-TB-of-Google-data-in-under-3-seconds-using-only-2-KB-of-memory

```

## How do you design a rand7 function using a rand5 function?
```
https://github.com/harishvc/challenges/blob/master/generate-rand7.py
```