#Quick reference to JavaScript Closures


##Closures
* **Inner function** has access to **outer function** variables and arguments
even **after** the outer function has returned. 
* A powerful feature than can be harnessed in creative ways


##Example 1
````javascript
//Motivation: http://stackoverflow.com/questions/111102/how-do-javascript-closures-work
function InitMessage(firstName) {
  var msg1 = "Hello ";
  var msg2 = function(lastName) { 
  return msg1 + firstName + " " + lastName;
  }
  firstName = "Ryan"  //value changes after inner function declaration
  return msg2;
}
var m1 = InitMessage("Harish");
console.log(m1("Chakravarthy"));  //Ryan Chakravarthy not Harish Chakravarthy
````

##Example 2: Unintended consequence
````javascript

function mysum1(a) {
  var b = 5
  var myreturn = function () { return a + b};
  b = 15 //changed!
  return myreturn;
}
var findsum1 = mysum1(5)
console.log(findsum1())  //20  when 10 is expected!
````

##Example 3: Fixing example 2
````javascript
//Immediately Invoke Function Expression - IIFE
function mysum2(a) {
  var b = 5
  var myreturn = (function () { return a + b}());
  b = 15 //changed!
  return myreturn;
}
var findsum2 = mysum2(5)
console.log(findsum2);  //10 , fixed!
````

##Example 4: Adding Event Listeners
````javascript
window.addEventListener("load", function() {
    for (var i = 1; i < 4; i++) {
        var button = document.getElementById("button" + i);
        button.addEventListener("click", function() {
        console.log("Clicked button " + button.id); 
        //"Clicked button button3" is displayed on console several times
        });
    }
});
````

##Example 5: Fixing example 4
````javascript
//Solution: Decouple closure from the iteration
//by calling a new function, which in turn creates a new referencing environment
function addListener(button) {
    return function () {
    console.log("Clicked button " + button); //Clicked button button3 is displayed on console several times
    };
}
window.addEventListener("load", function() {
    for (var i = 1; i < 4; i++) {
        var button = document.getElementById("button" + i);
        button.addEventListener("click",addListener(button.id));
    }
});
````

##Example 6: Using Closure to create **private variables**
````javascript
function ContactInformation(){
  var location = "123 Elm Street"
  return { 
    getLocation:function() { return location;},
    setLocation:function(newlocation) {location = newlocation;}
  } 
}
var ci = ContactInformation();
console.log(ci.getLocation());  //123 Elm Street
ci.setLocation("100 Woods");
console.log(ci.getLocation());  //100 Woods
````

##Callbacks
* Javascript interpreter in the browser is a single thread (does not support multithreading). 
* Callbacks are functions that are passed as arguments to be invoked when the ```callee``` has finished its job.
* Callback functions are Closures



##Reference
* [JavaScript Function Definitions@W3 Schools](http://www.w3schools.com/js/js_function_definition.asp)
* [Closure discussion on Stack Overflow](http://stackoverflow.com/questions/111102/how-do-javascript-closures-work)
* [JavaScript Closures Demystified](http://www.sitepoint.com/javascript-closures-demystified/)

