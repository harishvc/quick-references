#Quick reference to JavaScript ````this````


##````this````
* ````this```` keyword refers to the object in the **current context**
* ````this```` is used in JavaScript similar to the way we use **pronouns in natural languages**
* ````this```` keyword is used for precision and makes the code **unambiguous**, just as the *pronouns*



##Examples 
````javascript

var box = {outerWidth: 50};
function width(){
    console.log(this.outerWidth);
    //console.log(window.outerWidth);
}
width.apply(box);  //50
width(); //1200 - window.outerWidth


var person = {
    firstName: "Harish",
    lastName: "Chakravarthy",
    fullName: function () {
    console.log(this.firstName + " " + this.lastName);      //#1        
    console.log(person.firstName + " " + person.lastName);  //#2
  }
}

//Example 1
person.fullName(); //Harish Chakravarthy printed twice on console


//Example 2
var a = person.fullName; 
a();              //#1 undefined , #2 Harish Chakravarthy   


//Example 3
var a = person;
a.firstName = "Hello";
a.lastName  = "World"; 
a.fullName();    //Hello World printed twice on console

//Example 4
function Person (name) {
    this.name = name;
    this.sayHello = function () {
        console.log ("Hello", this.name);
    }
}
var x = new Person("Harish");
x.sayHello();   //Hello Harish
````


##Future Reading
* [The this keyword](http://www.quirksmode.org/js/this.html)
* [Understand JavaScript’s “this” With Clarity, and Master It](http://javascriptissexy.com/understand-javascripts-this-with-clarity-and-master-it/)
* [How does the “this” keyword work?](http://stackoverflow.com/questions/3127429/how-does-the-this-keyword-work)
* [Scope in JavaScript](http://web.archive.org/web/20110725013125/http://www.digital-web.com/articles/scope_in_javascript/) :boom:
