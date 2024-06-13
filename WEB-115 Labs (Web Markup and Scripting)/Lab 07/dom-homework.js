// My div container
let myDiv = document.getElementById("myDiv");

// Parts of myDiv
let mdHeading = document.createElement("h1");
let mdParagraph = document.createElement("p");
let mdList = document.createElement("ul");
let mdButton = document.createElement("button");

// Design the container
myDiv.appendChild(mdHeading);
mdHeading.className = "highlight"
mdHeading.textContent = "Welcome to DOM homework";

myDiv.appendChild(mdParagraph);
mdParagraph.textContent = "This is your first DOM homework assignment";

myDiv.appendChild(mdList);

// Add three items to the unordered list (ul)
let itemList = []
for (i = 1; i <= 3; i++) {
    let mdListItem = document.createElement("li");
    mdList.appendChild(mdListItem);
    mdListItem.textContent = `Item ${i}`;
    itemList.push(i);
};

myDiv.appendChild(mdButton);
mdButton.textContent = "Add new list item"

// Create a random list for picking colors for text and background
let colorsList = ["red", "blue", "green", "yellow", "pink"]

mdButton.addEventListener("click", function() {
    // Create a new item and append it to the unordered list (ul)
    let newListItem = document.createElement("li");
    mdList.appendChild(newListItem);

    // Display item text and choose a random color
    newListItem.textContent = `New List Item ${itemList.length + 1}`;
    let randomTextColor = Math.floor(Math.random() * 5);
    newListItem.style.color = colorsList[randomTextColor];

    // Change the background color for the myDiv container
    let randomBackgroundColor = Math.floor(Math.random() * 5);
    myDiv.style.background = colorsList[randomBackgroundColor];

    // Update the item within the list 
    itemList.push(itemList.length + 1);
    });
