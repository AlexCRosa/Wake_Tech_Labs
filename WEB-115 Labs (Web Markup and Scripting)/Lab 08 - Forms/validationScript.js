    // JavaScript code for form validation
document.getElementById('myForm').addEventListener('submit', function(event) {
  inputValidation(event);
});

// Implement a function that validates the input value
function inputValidation(event) {

    // Retrieve the input field value  
    let inputValue = document.forms['myForm'].elements['inputField'].value;

    // Regular expression pattern for alphanumeric input
    let regex = /^[a-zA-Z0-9]*$/;

    // Check if the input value matches the pattern
    if (regex.test(inputValue)) {

        // Valid input: display confirmation and submit the form
        window.alert(`${inputValue} is a valid entry.`);    

    } else {

        // Invalid input: display error message
        window.alert("Invalid entry.");
        document.forms['myForm'].reset() // Reset the form to its initial state
        
        // Prevent form from submitting
        event.preventDefault();
    };  
};
