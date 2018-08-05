# Quick reference to JavaScript functions


## Function Hoisting & Scope
 - Hoisting is JavaScript's default behavior of hoisting **declarations** to the top of the **current scope**
 - Hoisting applies to variable declarations and to function declarations

* Always declare your local variables before you use them
* JavaScript functions are **first class citizens** can be constructed at runtime, assigned to variables and returned by other functions. 

## How does `var` work? What happens if `var` not used?
 - If you use `var ` during variable declaration, the scope of the variable is **limited to the current scope** (e.g. function). 
 - If you `don't use var` the variable **scope bubbles up** until it encounters a variable by the given name or the global object (window, if you are doing it in the browser), where it then attaches. 
   *Traversing up the scope chain is a good thing, but adding it to the global scope if it doesn't find anything is a pitfall*.

## Difference between `var` and `let`
 - `let` is used to restrict scope to the block
 - `var` is also used to restrict scope but can become global (due to **hoisting**)
```javascript
for(let li=1;li<2;li++){li;}
1
for(var vi=1;vi<2;vi++){vi;}
1
vi  //can be referenced!
2
li
Uncaught ReferenceError: li is not defined    
```

## Hoisting (example 1)
```
function a() {
	v1 = 25   //global!
	console.log(v1);
}

function b(){
	console.log(v1)  //global v1
}
a();  //25
b();  //25
```

## Hoisting (example 2)
```javascript
//Example 1
console.log(a)         //ReferenceError: a not defined  (NOT in memory)

//Example 2
console.log(a)         //ReferenceError: a not defined  (NOT in memory)
a = "Hello World!"

//Example 3
console.log(a)         //undefined  (in memory and initialized to undefined, undefined is a special keyword)
var a = "Hello World!"

//Example 4
var a;
console.log(a)         //undefined (in memory and initialized to undefined, undefined is a special keyword)


//Example 5
b();  //Hello World!  - Entire function is stored in the memory

function b(){
	console.log("Hello World!");	
}
```

## Hoisting (example 3)
```javascript
//Example 1
function b() {
	var a1;
	console.log(a1);	
}

function a() {
	var a1 ="2";
	console.log(a1);
	b();
}

var a1 ="1";
console.log(a1);
a();
console.log(a1);

//output
1
2
undefined
1


//Example 2
function b() {
	var a1;  //local a1
	console.log(a1);	//a1 declared not not initalized!
}
function a() {
	//var a1 ="2";
	a1 = 2    //access global a1
	console.log(a1);
	b();
}
var a1 ="1";  //context is global inspite of using var!
console.log(a1);
a();
console.log(a1);
//output
1
2
undefined
2

//Example 3
function b(a1) {
	console.log(a1);	
	a1 = 4;
	console.log(a1);		
}

function a() {
	var a1 =2;   //scope inside a()
	console.log(a1);
	b(a1);
	console.log(a1);
}

a1 = 1;  //scope is global!
console.log(a1);
a();
console.log(a1);

//output
1
2
2
4
2
1
```

## Hoisting (example 4)
```
//example 1: Automatically Global
function test() {
	a = 5  //Automatically Global!
	console.log("a=",a);   //5
}
test();
console.log("a=",a);       //5

//example 2: Local
function test() {
	var a = 5  //Local
	console.log("a=",a);   //5
}
test();
console.log("a=",a);       //Error: a not defined

//example 3: Explict Global
var a = 5 //Explict Global
function test() {
	console.log("a=",a);   //5
}
test();
console.log("a=",a);       //5

//example 4: strict mode
"use strict";
a = 5   //Error: a is not defined
console.log("a=",a);
```


## Hoisting (example 5)
```javascript
//Access to global variables
var count = 3
for(i=1;i<count;i++){
  console.log(i)   //1,2
}
function newI() {
  console.log(i)  //3 since i  is GLOBAL
}
newI()
````

## Function definition & execution
```javascript
var a = toCelsius //No () , refers to function definition
console.log(a(78)) //execution

function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
  }
```

## Self-invoking functions
Immediately invoke a function as soon as it's defined - **solution to avoid Closure**
```javascript
(function () {
    var x = "Hello from JavaScript!";      // I will invoke myself
    console.log(x)
})();
```


##```undefined```
```javascript
//Variation 1
var text = 'outside';
   function logIt(){
     console.log(text);   //outside , scope of text follows up the scope chain 
     text = 'inside';
   };
   logIt();


//Variation 2
//https://www.interviewcake.com/question/python/js-scope
var text = 'outside';
function logIt(){
    console.log(text);   //undefined - text scope is local, hoisted to the top of the function and undefined by default
    var text = 'inside';
};
logIt();
```

## ```NaN```
```javascript
var a = 1;
function myadd(){
    console.log(a + b);   //NaN - Not a Number
    var b = 2;
};
myadd();
```

