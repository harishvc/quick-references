#Quick reference to JavaScript &amp; DOM Elements

##Example 1
````
<a id="demo" class="aaaa" style="font-size:15px" href="#">Click me!</a>
<script>
document.getElementById("demo").addEventListener("click", process);  
function process() {
    tmp = document.getElementById('demo');
    tmp.innerHTML = "Hello JavaScript!";
    tmp.className = "bbb";
    tmp.style.fontSize = "25px";
    tmp.style.textDecoration = "none";
}
</script>
````
Explanation
* Add listiner on `id=demo` on action `click`
* Replace  HTML text
* Replace `class` name
* Change `font size`
* Remove `underline`  - still using `a href`

##Example 2
````
//Source: http://www.w3schools.com/js/js_htmldom_nodes.asp
<div id="div1">
<p id="p1">This is a paragraph.</p>
<p id="p2">This is another paragraph.</p>
</div>

<script>
var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);

var element = document.getElementById("div1");
var child = document.getElementById("p1");
element.insertBefore(para,child);
</script>

//Output
This is new.
This is a paragraph.
This is another paragraph.
````
Explanation
* A new node is created and stored in `para`
* New node is inserted before `child`


##Future Reading
* [JavaScript HTML DOM Elements](http://www.w3schools.com/js/js_htmldom_elements.asp)
