document.getElementById("myButton").addEventListener("click", function() {
    var firstName = document.getElementById("firstName").value;
    var lastName = document.getElementById("lastName").value;
    var course = document.getElementById("course").value;
    var section = document.getElementById("section").value;
    var role = document.getElementById("role").value.toLowerCase();

    if (role !== "student" && role !== "instructor") {
        window.alert("Only 'student' or 'instructor' is allowed for role.");

        firstName, lastName, course, section, role = "";
    } else {
        var person = {
            "firstName": `${firstName}`,
            "lastName": `${lastName}`,
            "course": `${course}`,
            "section": `${section}`,
            "role": `${role}`
        };

        console.log(person);  // JavaScript object

    //     var person = {
    //         "firstName": firstName,
    //         "lastName": lastName,
    //         "course": course,
    //         "section": section,
    //         "role": role
    //     };

    //     var myString = JSON.stringify(person);  // JSON string
    //     var myObject = JSON.parse(myString);  // JavaScript object
        
    //     console.log(myObject);
    };
});
