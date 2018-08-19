# Fun with Permuation and Combination

## Permutation
* Combinations where **order matters** is a Permutation. Example: lock combination. A Permutation is an **ordered Combination**    
* Permutation result has same length are original string (no empty string and strings of different length)
* Permutation can be considered as a COMPLETE GRAPH TRAVERSAL problem without visiting any node twice
* Two type of Permutations  
  - Repetition **allowed**  
    #Permutations with repetition = **n^r**  
    n=total number of things to choose from, r=#slots/spots/openings
  - Repetition is **not allowed**  
    #Permutations without Repetition = **n!/(n-r)!**  
    n=total number of things to choose from, r=#slots/spots/openings  
* Problem #1: How many permutations are there in  `ABCD`  
  - 4 unique characters. 4!
* Problem #2: How many permutations are there in   `ABAD`  
  - 4 characters, `A` repeats 2 times 
  - 4!/2! = 4x3 = 12
* Problem #3: How many permutations are there in   `ABADBB`  
  - 6 characters, `A` repeats 2 times, `B` repeats 3 times 
  - 6!/(2! * 3!) = 60


## Combination
Combinations where **order does NOT matter** is a Combination. Example lottery ticket.
* Two types of Combinations  
  - Repetition is allowed  
  - Repetition is not allowed    
  - `n choose r`  
* Combinations with Repetition  
  - Example: Pick 3 scoops from 5 different ice-cream flavors. `(5+3-1)!/(3!*(5-1)!)`  
  - #combinations = **(n+r-1)!/r! * (n-1)!**  
* Combinations without Repetition  
  - Example: Lottery, Committee members   
  - #Combinations for getting 123 = 1   
  - Example: `150 choose 1 = 150!/(150-1)!*1!`
  - #combinations = **n!/(n-r)! * r!**  
    n=total number of things to choose from, r=#slots/spots/openings  
  

## References
* [Combinations and Permutations](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)
