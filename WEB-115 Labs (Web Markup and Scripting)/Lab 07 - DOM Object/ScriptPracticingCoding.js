let myTable = document.getElementById("myTable");

let mainTable = document.createElement("table");
myTable.appendChild(mainTable);


// Heading
let mainHeading = document.createElement("tr");
mainTable.appendChild(mainHeading);

let headingCar = document.createElement("th");
mainHeading.appendChild(headingCar);
headingCar.textContent = "Car";

let headingSpeed = document.createElement("th");
mainHeading.appendChild(headingSpeed);
headingSpeed.textContent = "Top";

let headingPrice = document.createElement("th");
mainHeading.appendChild(headingPrice);
headingPrice.textContent = "Price";


// First Item
let firstItem = document.createElement("tr");
mainTable.appendChild(firstItem);

let item1Car = document.createElement("td");
firstItem.appendChild(item1Car);
item1Car.textContent = "Chevrolet";

let item1Speed = document.createElement("td");
firstItem.appendChild(item1Speed);
item1Speed.textContent = "120mph";

let item1Price = document.createElement("td");
firstItem.appendChild(item1Price);
item1Price.textContent = "10,000";


// Second Item
let secondItem = document.createElement("tr");
mainTable.appendChild(secondItem);

let item2Car = document.createElement("td");
secondItem.appendChild(item2Car);
item2Car.textContent = "Pontiac";

let item2Speed = document.createElement("td");
secondItem.appendChild(item2Speed);
item2Speed.textContent = "140mph";

let item2Price = document.createElement("td");
secondItem.appendChild(item2Price);
item2Price.textContent = "20,000";


// Styles using the style object
mainTable.style.border = "5px solid Bisque";
mainTable.style.borderCollapse = "collapse";
mainTable.style.backgroundColor = "Beige";


// Styles using setAttribute() method
mainTable.setAttribute("cellpadding", "10");
mainTable.setAttribute("cellspacing", "5");
