let resources = 0;
let currentRank = 0;
document.getElementById("clickButton").addEventListener("click", function () {
    resources += 1;
    updateResources();
});

function updateResources() {
    const resourceElement = document.getElementById("resources");
    resourceElement.textContent = parseInt(resources);
}

function updateIncome() {
    let totalIncome = 0;
    for (const business of businesses) {
        totalIncome += business.income * business.level;
    }
    resources += totalIncome;
    updateResources();
}

function prestigeToNextRank() {
    if (resources >= 10) {
        alert("You have reached the next rank!");
        resources = 0;
        currentRank += 1;
        const Rankelement = document.getElementById("currentRank");
        Rankelement.textContent = currentRank;
        updateResources();
    }
}

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
            this.cost *= 2;
            this.income *= 1.2;
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



const primitiveFarm = new Business("Primitive Farm", 10, 1);
primitiveFarm.updateDisplay();

const Blacksmith = new Business("Blacksmith", 100, 10);
Blacksmith.updateDisplay();

const ResarchFac = new Business("Reaserch Facility", 1000, 100);
ResarchFac.updateDisplay();

const businesses = [primitiveFarm, Blacksmith, ResarchFac];

setInterval(updateIncome, 1000);

setInterval(prestigeToNextRank, 1000);
