let myDiv = document.getElementById("myDiv");

let timerDisplay = document.createElement("h1");
timerDisplay.innerHTML = "0";
myDiv.appendChild(timerDisplay);

// Created three variables to handle the timer
let time;
let timeValue = 0;
let isRunning = false;



// Start button
let startButton = document.createElement("button");
startButton.id = "startTimer";
startButton.value = "Start Timer";
startButton.textContent = "Start Timer";
myDiv.appendChild(startButton);

startButton.addEventListener("click", function () {
    if (!isRunning) {
        isRunning = true;
        time = setInterval(function() {
            timeValue++;
            timerDisplay.innerHTML = timeValue;
        }, 1000);
    }
});

myDiv.appendChild(document.createElement("br"))



// Stop button
let stopButton = document.createElement("button");
stopButton.id = "stopTimer";
stopButton.value = "Stop Timer";
stopButton.textContent = "Stop Timer";
myDiv.appendChild(stopButton);

stopButton.addEventListener("click", function() {
    if (isRunning) {
        clearInterval(time);
        isRunning = false;
    };
});

myDiv.appendChild(document.createElement("br"))



// Reset button
let resetButton = document.createElement("button");
resetButton.id = "resetTimer";
resetButton.value = "Reset Timer";
resetButton.textContent = "Reset Timer";
myDiv.appendChild(resetButton);

resetButton.addEventListener("click", function() {
    clearInterval(time);
    isRunning = false;
    timeValue = 0;
    timerDisplay.innerHTML = "0";
});

myDiv.appendChild(document.createElement("br"))
