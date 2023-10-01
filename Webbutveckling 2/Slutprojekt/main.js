// Startkapital
let resources = 100000;

//Klick
document.getElementById("clickImage").addEventListener("click", function () {
    resources += 1;
    updateResources();
});

//Uppdaterar resurser
function updateResources() {
    const resourceElement = document.getElementById("resources");
    resourceElement.textContent = parseInt(resources); // Convert to integer
}

function updateIncome() {
    let totalIncome = 0;
    // Loopar igenom verksamheterna och räknar ut totala inkomsten
    for (const business of businesses) {
        totalIncome += business.income * business.level;
    }
    resources += totalIncome;
    updateResources();
}

// Klass för verksamheter
class Business {
    constructor(name, cost, income) {
        this.name = name;
        this.cost = cost;
        this.income = income;
        this.level = 0;
        this.element = null;
    }

    purchase() {
        if (resources >= this.cost) {
            resources -= this.cost;
            this.level += 1;
            this.cost *= 2; //Kan ändras(vet inte om jag vill ha exponetiell eller fast kostnad)
            this.income *= 1.2; //Kan ändras
            updateResources();
            this.updateDisplay();
        }
    }

    updateDisplay() {
        if (!this.element) {
            this.element = document.createElement("div");
            this.element.classList.add("business");
            document.getElementById("businesses").appendChild(this.element);
        }

        const businessIncome = (this.income * this.level).toFixed(1);

        //Uppdaterar infon
        this.element.innerHTML = `
            <p>${this.name} (Level ${this.level})</p>
            <p>Cost: ${this.cost} resources</p>
            <p>Income: ${businessIncome} per second</p>
            <button id="${this.name}Button">Purchase</button>
        `;

        document.getElementById(`${this.name}Button`).addEventListener("click", () => {
            this.purchase();
        });
    }
}





// VERKSAMHETER //
const primitiveFarm = new Business("Primitive Farm", 10, 1);
primitiveFarm.updateDisplay();

const Blacksmith = new Business("Blacksmith", 100, 10);
Blacksmith.updateDisplay();


// Array för verksamheter
const businesses = [primitiveFarm, Blacksmith];

// Uppdaterar inkomsten varje sekund
setInterval(updateIncome, 1000);


