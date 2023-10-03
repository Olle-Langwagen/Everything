<<<<<<< HEAD
let resources = 0;
let currentRank = 0;
document.getElementById("clickButton").addEventListener("click", function () {
=======
// Startkapital
let resources = 100000;

//Klick
document.getElementById("clickImage").addEventListener("click", function () {
>>>>>>> 4767879e17d910af06558135e5c0f26352660216
    resources += 1;
    updateResources();
});

<<<<<<< HEAD
=======
//Uppdaterar resurser
>>>>>>> 4767879e17d910af06558135e5c0f26352660216
function updateResources() {
    const resourceElement = document.getElementById("resources");
    resourceElement.textContent = parseInt(resources);
}

function updateIncome() {
    let totalIncome = 0;
<<<<<<< HEAD
=======
    // Loopar igenom verksamheterna och räknar ut totala inkomsten
>>>>>>> 4767879e17d910af06558135e5c0f26352660216
    for (const business of businesses) {
        totalIncome += business.income * business.level;
    }
    resources += totalIncome;
    updateResources();
}

<<<<<<< HEAD
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

=======
// Klass för verksamheter
>>>>>>> 4767879e17d910af06558135e5c0f26352660216
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
<<<<<<< HEAD
            this.cost *= 2;
            this.income *= 1.2;
=======
            this.cost *= 2; //Kan ändras(vet inte om jag vill ha exponetiell eller fast kostnad)
            this.income *= 1.2; //Kan ändras
>>>>>>> 4767879e17d910af06558135e5c0f26352660216
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

<<<<<<< HEAD
=======
        //Uppdaterar infon
>>>>>>> 4767879e17d910af06558135e5c0f26352660216
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



<<<<<<< HEAD
=======


// VERKSAMHETER //
>>>>>>> 4767879e17d910af06558135e5c0f26352660216
const primitiveFarm = new Business("Primitive Farm", 10, 1);
primitiveFarm.updateDisplay();

const Blacksmith = new Business("Blacksmith", 100, 10);
Blacksmith.updateDisplay();
<<<<<<< HEAD

const ResarchFac = new Business("Reaserch Facility", 1000, 100);
ResarchFac.updateDisplay();

const businesses = [primitiveFarm, Blacksmith, ResarchFac];

setInterval(updateIncome, 1000);

setInterval(prestigeToNextRank, 1000);
=======


// Array för verksamheter
const businesses = [primitiveFarm, Blacksmith];

// Uppdaterar inkomsten varje sekund
setInterval(updateIncome, 1000);


>>>>>>> 4767879e17d910af06558135e5c0f26352660216
