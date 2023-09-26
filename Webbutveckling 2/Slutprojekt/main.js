// Initial resource count
let resources = 0;

// Click event handler
document.getElementById("clickButton").addEventListener("click", function () {
    // Increase resources when clicked
    resources += 1;
    updateResources();
});

// Function to update the resource count in the HTML
function updateResources() {
    const resourceElement = document.getElementById("resources");
    resourceElement.textContent = parseInt(resources); // Convert to integer
}

function updateIncome() {
    let totalIncome = 0;
    // Loop through all businesses and calculate total income
    for (const business of businesses) {
        totalIncome += business.income * business.level;
    }
    resources += totalIncome;
    updateResources();
}

// Business example (you can expand this for more businesses)
class Business {
    constructor(name, cost, income) {
        this.name = name;
        this.cost = cost;
        this.income = income;
        this.level = 0;
        this.element = null; // Reference to the HTML element
    }

    purchase() {
        if (resources >= this.cost) {
            resources -= this.cost;
            this.level += 1;
            this.cost *= 2; // You can adjust the cost increase logic
            this.income *= 1.2; // You can adjust the income increase logic
            updateResources();
            this.updateDisplay();
        }
    }

    updateDisplay() {
        if (!this.element) {
            // If the HTML element doesn't exist, create it
            this.element = document.createElement("div");
            this.element.classList.add("business"); // Lägg till .business-klassen
            document.getElementById("businesses").appendChild(this.element);
        }

        // Calculate the income for this business based on its level
        const businessIncome = (this.income * this.level).toFixed(1);

        // Update the business information
        this.element.innerHTML = `
            <p>${this.name} (Level ${this.level})</p>
            <p>Cost: ${this.cost} resources</p>
            <p>Income: ${businessIncome} per second</p>
            <button id="${this.name}Button">Purchase</button>
        `;

        // Add click event for purchasing this business
        document.getElementById(`${this.name}Button`).addEventListener("click", () => {
            this.purchase();
        });
    }
}

// Create example businesses
const primitiveFarm = new Business("Primitive Farm", 10, 1);
primitiveFarm.updateDisplay();

const Blacksmith = new Business("Blacksmith", 100, 10);
Blacksmith.updateDisplay();
// Create an array to store all businesses
const businesses = [primitiveFarm, Blacksmith];

// Set up an interval to update income every second (adjust the interval as needed)
setInterval(updateIncome, 1000); // Income updates every second
