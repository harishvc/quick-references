#Quick reference to JavaScript
Scope, Lifetime, Strict mode, Data types, ````typeof```` & Hoisting

##JavaScript is case sensitive
````javascript
var a = 5;
console.log(A); //Uncaught ReferenceError
````


##Data types
* JavaScript has one complex data type, the **Object data type**. 
  * Object data types are **mutable (can be changed) and they are addressed by reference** 
* JavaScript has **five simple data types: Number, String, Boolean, Undefined, and Null**. 
  * Simple (primitive) data types are **immutable (cannot be changed) and they are addressed by value**  
````javascript
var x = 5
var y = x;
x = 1;
console.log(x,y); //1,5  reference by value

var people = {Name:"Harish", Height:6}
var y = people;
people.Name = "test";
console.log(people.Name,y.Name);   // test test   , reference by address
````

##Simple data types &amp; `typeof`
````javascript
var a = 5.001
console.log("a type =", typeof a)  //number
a = "Harish"
console.log("a type =", typeof a)  //string
a = ["a", "b", "c"]
console.log("a type =", typeof a)  //Object
a = {name: "a"};
console.log("a type =", typeof a)  //Object
a = true;
console.log("a type =", typeof a)  //boolean
var a = function () {console.log("Hello World!")}
console.log (typeof a)             //function
a  = "Harish " + 5
console.log(a, "a type =", typeof a)  //Harish 5 , a type=String :boom:
````

##Scope, Lifetime &amp; Strict mode
* If you assign a value to a variable that has *not been declared*, it will **automatically become a global variable**
* Lifetime of a JavaScript variable starts when it is **declared**.
  * Local variables are deleted when the function is completed
  * Global variables are deleted when you **close the page**
* Strict mode will trigger code execution in strict mode. Variables need to declared before using
````javascript
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
````

##Comparison && Logical operators
* ````==```` compare by value
* ```===``` compare by value and type
* When comparing a string with a number, JavaScript will convert the string to a number
  * An empty string converts to 0
  * A non-numeric string converts to NaN which is always false
````javascript
var a = 5   
console.log(a==5);     //true
console.log(a=="5");   //true convert string to number  :boom:
console.log(a==="5");  //false
````

##Bitwise Operations
````javascript
console.log(5 & 1);      //0101 & 0001 = 1  AND
console.log(5 | 1);      //0101 | 0001 = 5  OR
console.log(~5);        //~0101 = 10        NOT
console.log( 5 ^ 1);    //0101 ^ 0001 = 4   XOR
console.log( 5 >> 1);   //0010 = 2          Right Shift discarding bits shifted off.
console.log( 5 >>> 1);   //0010 = 2         Right Shift discarding bits shifted off and shifting in zeros from the left
console.log( 5 << 1);   //1010 = 10         Left Shift shifting in zeros from the right 
````

##Hoisting
* Hoisting is JavaScript's default behavior of **moving declarations to the top of the current scope**  
* Hoisting applies to variable declarations and to function declarations
````javascript
console.log("x=",x);  //undefined  , Hoisting in action!
var x;
x = 5
console.log("x=",x);  //5
console.log("x+y=",x+y); //Error: NaN (non-configurable and non-writable property)
var y=5;
````

##Asynchronous module definition (AMD) 
AMD is a JavaScript specification that defines an API for defining code modules and their dependencies so modules can be loaded asynchronously if desired.
Major benefit is **performance**  - only loading modules when needed. Interested? Check out [AMD versus CJS. What’s the best format?](http://unscriptable.com/2011/09/30/amd-versus-cjs-whats-the-best-format/)



##References
* [W3 Schools](http://www.w3schools.com/js/)
* [JavaScript shift operator](http://stackoverflow.com/questions/1822350/what-is-the-javascript-operator-and-how-do-you-use-it)
* [JavaScript operators](http://web.eecs.umich.edu/~bartlett/jsops.html)
* [JavaScript Objects in Detail](http://javascriptissexy.com/javascript-objects-in-detail/)
