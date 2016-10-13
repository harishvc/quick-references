#Quick reference to JavaScript Functions


##Function Declaration
````javascript
function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
  }
var a = toCelsius(78) //() Operator invokes the function and refers to function result
console.log(a) //25.555555555555557
````

##Function Expression
* Stored in a variable
* Also referred to as **anonymous** function (a function without a name)
* Function expessions create anonymous fucntions adding debugging complexity
* It's a **closure!**
````javascript
var a = toCelsius //No () , refers to function definition
console.log(a(78)) //25.555555555555557
````


##Self-invoking Functions
Immediately invoke a function as soon as it's defined - **solution to avoid Closure**
````javascript
(function () {
    var x = "Hello from JavaScript!";      // I will invoke myself
    console.log(x)
})();
````

##First-class citizens
* JavaScript functions can be constructed at runtime, assigned to variables and returned by other functions. 
* JavaScript functions also have their own properties and methods
````javascript
//Source: http://www.sitepoint.com/javascript-closures-demystified/
var foo = function() {
  console.log("Hello World!");
};
var bar = function(arg) {
  return arg;
};

bar(foo)();
//Explanation
//Two functions are created at runtime and assigned to the variables foo and bar
//Function bar is executed with argument foo
//return arg returns a function reference to foo
//() in bar(foo)() executes the returned reference
//Hello World! is sent to console.log
````

##Nested Functions (Inner Functions)
* Nested functions are functions inside another (outer) functions
* Each time the outer function is called, an **instance** of the inner function is created
* Inner functions have **implicit access to the outer function’s scope**
````javascript
function add1(x,y) {
	z = 5;
	function add2() {
		return (x+y+z);  //access to x,y,z
	}
	return add2();		
}
var foo = add1(1,2);
console.log(foo);  //8
````


##References
* [JavaScript Function Definitions@W3 Schools](http://www.w3schools.com/js/js_function_definition.asp)
* [Closure discussion on Stack Overflow](http://stackoverflow.com/questions/111102/how-do-javascript-closures-work)
* [JavaScript Closures Demystified](http://www.sitepoint.com/javascript-closures-demystified/)

