# Quick reference to JavaScript
Scope, Lifetime, Strict mode, Data types, ````typeof```` & Hoisting

## Is JavaScript **case sensitive**?
Yes, JavaScript is case-sensitive.
````javascript
var a = 5;
console.log(A); //Uncaught ReferenceError
````

## Is JavaScript single threaded and asynchronous?
Javascript is **single threaded and synchronous by default however asynchronous behaviour can be achieved** (using nested callback, promises). 
Web Browsers are asynchronous and they maintain an event queue. JavaScript processes the next command in the event queue after it current stack is empty!  
 

## Explain Data types
* JavaScript has one complex data type, the **Object data type** (example:date, array, regular expression, functions). 
  * Object data types are **mutable (can be changed) and they are addressed by reference. Example array** 
* JavaScript has **six simple data types: Number, String, Boolean, Undefined, Null and Symbol**. 
  * Simple (primitive) data types are **immutable (cannot be changed) and they are addressed by value**
  * Number is of type float by default

## Is JavaScript pass by value or reference?
  - Both! Javascript **always passes primitive data types (example:string, numbers) by value** and Arrays and objects as reference. Example:

```javascript
#source: http://stackoverflow.com/questions/6605640/javascript-by-reference-vs-by-value
var a = [1, 2, {foo:"bar"}];
var b = a[1]; //b=2
a[1]  = 10;
print b      //b=2
print a      //[1, 10, {foo:"bar"}];

z = a[2]     //z = {foo:"bar"}
x = a[2]     //x = {foo:"bar"}     
a[2] = 3 
print a      //[1, 10, 3];
z.foo = "BAR"
print z      //{foo:"BAR"}
print x      //{foo:"BAR"}
```

## How do you achieve block level scope?
Since ES6 block level scope is achieved by using `let` in addition to global and function level scope


## Is JavaScript loosely typed? Explain.
Yes, Javascript is a dynamic loosely typed language.
````javascript
// Dynamic - variable names can be used to refer to different data types
a = "123";
a = True;

//Loosely typed - variable type not needed explicitly
a = 1 + 2;
console.log(a); //3   JS figures out the values are number

a = "123" + 4
consolve.log(a) //1234 JS figures out the values are strings and concatenates them!
````

## Explain prototypal Inheritance?
  - JavaScript is classless and does not support classical inheritance.
  - Each object is a prototype of another object, and inherits the properties defined in the prototype
```
var dog = {legs:4};
var spot = Object.create(dog);
console.log(spot.legs);  //4
```  

## What is Coercion?
Converting a value from one type to another is often called "type casting," when done **explicitly**, 
and "coercion" when done **implicitly** (forced by the rules of how a value is used).
````javascript
var a = 10
typeof(a)  //number
var b = a + "20"
console.log(b) //"1020"
typeof(b) //string

Reference:
 - https://github.com/getify/You-Dont-Know-JS/blob/master/types%20%26%20grammar/ch4.md
````


## What are Anonymous functions?
An anonymous function is a function that was declared without a name identifier to refer to it. One common use 
for anonymous functions is as arguments to other functions. Another common use is as a closure
```
var anon = function() {
  alert('I am anonymous');
};
anon();
```


## Simple data types &amp; `typeof`
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

## Scope, Lifetime &amp; Strict mode
* If you assign a value to a variable that has *not been declared*, it will **automatically become a global variable**
* Lifetime of a JavaScript variable starts when it is **declared**.
  * Local variables are deleted when the function is completed
  * Global variables are deleted when you **close the page**
* Strict mode will trigger code execution in strict mode. Variables need to declared before using
* More examples on [Hoisting & Scope](https://github.com/harishvc/quick-references/blob/master/javascript/javascript-functions-part6.md)


## Comparison && Logical operators
* ````==```` compare by value
* ```===``` compare by value and type
* JavaScript has two sets of equality operators: === and !==, and their **evil twins == and !=**
  * The evil twins do the right thing when the operands are of the same type, but if they are of different types, they attempt to coerce the values[5]
````javascript
>0 == '0'
true
>0 === '0'
false
````

## `null` vs `undefined`
- `null` can be **manually** to a value 
- `undefined` will be the default value (Hosting)


## Bitwise Operations
````javascript
console.log(5 & 1);      //0101 & 0001 = 1  AND
console.log(5 | 1);      //0101 | 0001 = 5  OR
console.log(~5);        //~0101 = 10        NOT
console.log( 5 ^ 1);    //0101 ^ 0001 = 4   XOR
console.log( 5 >> 1);   //101 becomes 010 = 2    Right Shift
console.log( 5 << 1);   //101 becomes 1010 = 10  Left Shift 
````

## What is the  difference between `$(document).ready()` and `body.onload()`?
 - `$(document).ready()` is a `jQuery` event that is fired as soon as the document (including all the elements) are loaded and accessible. Safest now to bind listiners, functions, callbacks to DOM. Here not all page contents (example: images) are loaded. You can have **multiple document ready** event handlers. 
 - `body.onload()` is a native JavaScript event that is tirggers `window.load` after the entire page including the douments are loaded


## Asynchronous module definition (AMD) 
AMD is a JavaScript specification that defines an API for defining code modules and their dependencies so modules can be loaded asynchronously if desired.
Major benefit is **performance**  - only loading modules when needed. Interested? Check out [AMD versus CJS. What’s the best format?](http://unscriptable.com/2011/09/30/amd-versus-cjs-whats-the-best-format/)



## References
1. [W3 Schools](http://www.w3schools.com/js/)
2. [JavaScript shift operator](http://stackoverflow.com/questions/1822350/what-is-the-javascript-operator-and-how-do-you-use-it)
3. [JavaScript operators](http://web.eecs.umich.edu/~bartlett/jsops.html)
4. [JavaScript Objects in Detail](http://javascriptissexy.com/javascript-objects-in-detail/)
5. https://stackoverflow.com/questions/359494/which-equals-operator-vs-should-be-used-in-javascript-comparisons