#Quick reference to JavaScript Closures


##Closures
* Closures contain a function and a **reference to the environment in which the function was created**
* Closures **store function state** even after the function has returned
* Closure is formed when an outer function exposes an inner function
* Closures can be used to easily pass parameters to callback functions
* Private data can be emulated by using closures  


##Example 1
````javascript
//Motivation: http://stackoverflow.com/questions/111102/how-do-javascript-closures-work
function sayHello(name) {
	var a = 'Hello ';
    var text = a + name;
    var sayAlert = function() { console.log(text); }
	text ="Hello B" //new values :boom:
    return sayAlert;
}
var x = sayHello("A");
x();  //Hello B (not Hello A)
````
Explanation
* ````text``` value is changed after function ````var sayAlert```` is initialized
* Since the closure has a reference to the environment it was created, it picks up the new value of ````text````


##Example 2
````javascript
function add1(value1) {
  return function add2(value2) {
    return value1 + value2;
  };
}
var x = add1(1);
var y = x(2);
console.log(y); //3    
````
Explanation (source: http://www.sitepoint.com/javascript-closures-demystified/)
* add1() function returns its inner function add2(). By **returning a reference to an inner function, a closure is created**.
* “value1″ is a local variable of add1() and a non-local variable of add2()
* Non-local variables refer to variables that are **neither in the local nor the global scope**  
* “value2″ is a local variable of add2().
* When add(1) is called, a closure is created and stored in “x”. In the **closure’s referencing environment**, “value1″ is bound to the value 1
* **Variables that are bound are also said to be closed over. This is where the name closure comes from**
* When x(2) is called, the closure is entered. This means that add2() is called, with the “value1″ variable holding the value one - access to non-local variable


##Example 3
````javascript
window.addEventListener("load", function() {
    for (var i = 1; i < 4; i++) {
        var button = document.getElementById("button" + i);
        button.addEventListener("click", function() {
        console.log("Clicked button " + button.id); //"Clicked button button3" is displayed on console several times
        });
    }
});
//Solution: Decouple closure from the iteration
//by calling a new function, which in turn creates a new referencing environment
````javascript
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


##Closure Use-cases
* Configuring callback functions with parameters. For example Internet Explorer does support passing callback arguments via setInterval(). A closure function can be created.
* JavaScript is **not a pure object-oriented language** and **does not support private data**. But, it is possible to **emulate private data using closures**
````javascript
function Person(name) {
  var x = name;
  var getName = function() {
    return x;
  };
  return getName;
}
var person = new Person("Colin");
person.x = "Tom";        //changing name - no impact!!!
console.log(person());  //Colin
console.log(person.x);  //Tom
````
Explanation
* Now, when person() is called, it is guaranteed to return the value that was originally passed to the constructor (emulate private data) 
* It is still possible for someone to add a new “name” property to the object, **but the internal workings of the object will not be affected** 


##Callbacks
* Javascript interpreter in the browser is a single thread (does not support multithreading). 
* Callbacks are functions that are passed as arguments to be invoked when the ```callee`` has finished its job.
* Callback functions Are Closures



##Reference
* (JavaScript Function Definitions@W3 Schools)[http://www.w3schools.com/js/js_function_definition.asp]
* (Closure discussion on Stack Overflow)(http://stackoverflow.com/questions/111102/how-do-javascript-closures-work)
* (JavaScript Closures Demystified)[http://www.sitepoint.com/javascript-closures-demystified/]

