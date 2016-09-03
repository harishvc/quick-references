#Quick reference to JavaScript Functions


##Function Hoisting & Scope
* Hoisting is JavaScript's default behavior of hoisting **declarations** to the top of the **current scope**
* Hoisting applies to variable declarations and to function declarations
* Always declare your local variables before you use them
* Variable scope is either **global or local** function since Java Script **does not have block-level scope** 
* JavaScript functions are **first class citizens** can be constructed at runtime, assigned to variables and returned by other functions. 


##Example 1
````javascript
var a = toCelsius //No () , refers to function definition
console.log(a(78))

function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
  }
````

##Example 2: Self-invoking Functions
Immediately invoke a function as soon as it's defined - **solution to avoid Closure**
````javascript
(function () {
    var x = "Hello from JavaScript!";      // I will invoke myself
    console.log(x)
})();
````

##Example 3: Access to global variables
````javascript
var count = 3
for(i=1;i<count;i++){
  console.log(i)   //1,2
}
function newI() {
  console.log(i)  //3 since i  is GLOBAL
}
newI()
````

##Eample 4: ````undefined````
````javascript
//https://www.interviewcake.com/question/python/js-scope
var text = 'outside';
function logIt(){
    console.log(text);   //undefined - local text is hoisted but no value
    var text = 'inside';
};
logIt();
````

##Example 5: ````NaN````
````javascript
var a = 1;
function myadd(){
    console.log(a + b);   //NaN - Not a Number
    var b = 2;
};
myadd();
````

