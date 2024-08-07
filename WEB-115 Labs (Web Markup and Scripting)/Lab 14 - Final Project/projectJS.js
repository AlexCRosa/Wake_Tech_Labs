function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
};

function generateMealPlan() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const goal = document.getElementById("goal").value;

    if (!validateEmail(email)) {
        alert("Please enter a valid email address.");
        return;
    };

    const newWindow = window.open("", "_blank");

    const doc = newWindow.document;  // Defined the new window within a variable
    doc.open();
    doc.write(`<!DOCTYPE html>
        <html>
        <head>
        <title>Weekly Meal Plan</title>
        <script src="projectJS.js" defer></script>

        <style>
            body { font-family: Arial, sans-serif; } 
            table { width: 100%; border-collapse: collapse; } 
            th, td { border: 1px solid black; padding: 8px; text-align: left; } 
            th { background-color: #d5cde3; }
            button { margin: 10px 5px; padding: 12px 24px; border: none;
                    background-color: #b19cd9; color: #ffffff; cursor: pointer;
                    border-radius: 5px; font-size: 16px; text-transform: uppercase;
                    transition: background-color 0.3s ease; }
            button:hover { background-color: #7ba9d3; }
        </style>
        </head>
        <body></body>
        <footer>
            <button type="button" onclick="printPlanner()">Print Planner</button>
            <button type="button" onclick="downloadPlanner()">Download Planner</button>
        </footer>
        </html>`);
    doc.close();

    // 

    const body = doc.body;

    const h1 = doc.createElement('h1');
    h1.textContent = `Weekly Meal Plan for ${name}`;
    body.appendChild(h1);

    const p = doc.createElement('p');
    p.textContent = `Goal for the week: ${goal}`;
    body.appendChild(p);

    const table = doc.createElement('table');
    table.className = "table";
    const thead = doc.createElement('thead');
    thead.className = "thead";
    const trHead = doc.createElement('tr');
    trHead.className = "trHead";

    const headers = ['Day', 'Breakfast', 'Snack 1', 'Lunch', 'Snack 2', 'Dinner'];
    for (let i = 0; i < headers.length; i++) {
        const th = doc.createElement('th');
        th.textContent = headers[i];
        trHead.appendChild(th);
    };

    thead.appendChild(trHead);
    table.appendChild(thead);

    const tbody = doc.createElement('tbody');

    const days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"];
    const meals = ['breakfast', 'snack1', 'lunch', 'snack2', 'dinner'];

    for (let i = 0; i < days.length; i++) {
        const tr = doc.createElement('tr');

        const dayCell = doc.createElement('td');
        dayCell.textContent = days[i].charAt(0).toUpperCase() + days[i].slice(1);
        tr.appendChild(dayCell);

        for (let j = 0; j < meals.length; j++) {
            const mealCell = doc.createElement('td');
            const mealValue = document.getElementById(days[i] + meals[j]).value;
            mealCell.textContent = mealValue;
            tr.appendChild(mealCell);
        }

        tbody.appendChild(tr);
    };

    table.appendChild(tbody);
    body.appendChild(table);

};

function printPlanner() {
    window.print();
};

function downloadPlanner() {
    const element = document.createElement('a');
    const mealPlanHTML = document.documentElement.outerHTML;
    const file = new Blob([mealPlanHTML], { type: 'text/html' });
    element.href = URL.createObjectURL(file);
    element.download = 'mealPlan.html';
    document.body.appendChild(element);
    element.click();
};
