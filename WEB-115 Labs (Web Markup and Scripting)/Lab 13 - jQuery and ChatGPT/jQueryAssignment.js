$(document).ready(function() {
    // Paragraph content
    const paragraph = document.createElement('p');
    paragraph.id = 'myParagraph';
    paragraph.innerText = 
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor \
        incididunt ut labore et dolore magna aliqua. Diam in arcu cursus euismod quis \
        viverra nibh. Nunc aliquet bibendum enim facilisis gravida neque convallis a cras. \
        Sagittis purus sit amet volutpat Consequat mauris. Duis ultricies lacus sed turpis \
        tincidunt id. Consequat interdum varius sit amet mattis vulputate. Enim sed \
        faucibus turpis in eu. Ridiculus mus mauris vitae ultricies leo integer malesuada \
        nunc vel. Nulla pharetra diam sit amet nisl suscipit. Lobortis elementum nibh \
        tellus molestie nunc non blandit massa enim. Dis parturient montes nascetur \
        ridiculus mus. Justo nec ultrices dui sapien eget. Enim tortor at auctor urna \
        nunc. Dictumst quisque sagittis purus sit amet volutpat consequat mauris nunc.";

    // Hide button
    const hideBtn = document.createElement('button');
    hideBtn.type = 'button';
    hideBtn.id = 'hideBtn';
    hideBtn.innerText = 'Hide';

    // Show button
    const showBtn = document.createElement('button');
    showBtn.type = 'button';
    showBtn.id = 'showBtn';
    showBtn.innerText = 'Show';

    // Placing elements into the div
    const contentDiv = document.getElementById('myDiv');
    contentDiv.appendChild(paragraph);
    contentDiv.appendChild(hideBtn);
    contentDiv.appendChild(showBtn);

    // Actions for buttons
    $("#hideBtn").click(function() {
        $("#myParagraph").hide();
    });
    $("#showBtn").click(function() {
        $("#myParagraph").show();
    });
});
