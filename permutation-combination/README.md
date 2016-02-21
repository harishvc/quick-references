#Fun with Permuation and Combination

##Permutation
* Combinations where **order does matter** is a Permutation. Example: lock combination  
  - A Permutation is an ordered Combination  
* Two type of Permutations  
  - Repetition is allowed  
  - Repetition is not allowed    
* Permutations with Repetition  
  Example: If the lock has a 3 digit (0...9) combination where digits can repeat. What is the # of permutations?
  - 10 digits can each take 1 of the 3 slots 
  - #permutations = 10^3 
  - #Permutations with Repetition = **n^r**  
    n=total number of things to choose from, r=#slots/spots/openings 
* Permutations without Repetition  
  Example: #permutations of choosing 3 pool balls (1...16) or P(16,3)? 
  - #permutations = 16x15x14
  - #Permutations without Repetition = **n!/(n-r)!**  
    n=total number of things to choose from, r=#slots/spots/openings  

##Combination
Combinations where **order does NOT matter** is a Combination. Example lottery ticket
* Two types of Combinations  
  - Repetition is allowed  
  - Repetition is not allowed    
* Combinations with Repetition  
  Example: Pick 3 scoops from 5 different ice-cream flavors. `(5+3-1)!/(3!*(5-1)!)  
  -#combinations = **(n+r-1)!/r! * (n-1)!**  
* Combinations without Repetition  
  Example: Lottery, Committee members   
  - #Combinations for getting 123 = 1 
  -`n choose r` , example 150 choose 1 = 150!/(150-1)!*1!
  - #combinations = **n!/(n-r)! * r!**  
    n=total number of things to choose from, r=#slots/spots/openings  
  




##References
* [Combinations and Permutations](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)