// Create a function called validatePhoneNumbers
function validatePhoneNumbers(phoneNumbers) {
  
  var validNumbers = [];

  // Iterate over each phone number in phoneNumbers array
  for(let i = 0; i < phoneNumbers.length; i++) {

    // Use regular expression and .replace method to remove spaces, dashes, and parentheses
    let newNumber = phoneNumbers[i].replace(/[ \-()]/g, "");

    // Check if the cleaned number has 10 digits
    if (newNumber.length == 10) {

      // Push valid numbers to validNumbers array
      validNumbers.push(newNumber);

    };

  };    

  // return validNumbers;  
  return validNumbers;

};

// Array of phone numbers
const phoneNumbers = [
  "123-456-7890",
  "(123) 456-7890",
  "1234567890",
  "123 456 789",
  "12-345-6789",
  "123456789",
  "12345678901"
];

// Call the validatePhoneNumbers function and store the result in validNumbers array
const validNumbers = validatePhoneNumbers(phoneNumbers);

// Display the valid phone numbers in the console
console.log(validNumbers);