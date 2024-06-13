let randomNumber = Math.floor(Math.random() * 10) + 1;
let userGuess;
let attempts = 0;

// Prompt user for a number between 1 and 10, or type 999 to exit.
userGuess = Number(prompt("Guess a number between 1 and 10:")); 

// Create while loop that continues for as long as the user guesses are incorrect.
while (userGuess != randomNumber) {
    // Loop should count the number of guesses.
    attempts += 1;

    // Loop should exit if user enters 999 and not display "Too high!"
    if (userGuess == 999) {
        break;

    // If the guess is too high, the user should be promped 'Too high!" and be able to guess again.    
    } else if (userGuess > randomNumber) {
        userGuess = Number(prompt("Too high! Guess again:"));
        
    // If the guess is too low, the user should be promped "Too low!" and be able to guess again.    
    } else if (userGuess < randomNumber) {
        userGuess = Number(prompt("Too low! Guess again:")); 

    // If anything else is entered, the user should be prompted that their input is invalid and 
    // to guess again.
    } else {
        userGuess = Number(prompt("Please enter a valid input:"));
    };
};

// If the guess is correct, the user should be alerted of their win and 
    // be told the number of guesses they made.
if (userGuess == randomNumber) {
    window.alert(`Congratulations, you've guessed it in ${attempts} tries!`);
};
