// Startkapital
let resources = 100000000;
let incomeMultiplier = 1;

const clickSound = new Audio('clicksound.mp3');

//Klick
document.getElementById("clickImage").addEventListener("click", function () {
    resources += 1;
    clickSound.play();
    
    updateResources();
});
/*
document.getElementById('clickImage').addEventListener('click', function(event) {
    // Play the sound effect


    // Calculate resources generated (assuming a fixed value for this example, e.g., 10)
    // In a real game, you'd probably have some logic to determine this value
    const resourcesGenerated = 10;

    // Create a new element to display the number of resources
    const resourceElement = document.createElement('div');
    resourceElement.innerText = `+${resourcesGenerated}`;
    resourceElement.style.position = 'absolute';
    resourceElement.style.left = `${event.pageX}px`;
    resourceElement.style.top = `${event.pageY}px`;
    resourceElement.style.fontSize = '1.2rem';
    resourceElement.style.color = '#007BFF';
    resourceElement.style.transition = 'opacity 1s, transform 1s';
    resourceElement.style.pointerEvents = 'none';
    document.body.appendChild(resourceElement);

    // After a short delay, animate the element to fade out and move upwards
    setTimeout(() => {
        resourceElement.style.opacity = '0';
        resourceElement.style.transform = 'translateY(-30px)';
        
        // Remove the element from the DOM after the animation
        setTimeout(() => {
            document.body.removeChild(resourceElement);
        }, 1000);
    }, 100);
});
*/
function resetGame() {
    // Reset resources
    resources = 0;  // or whatever starting value you want

    // Reset businesses
    for (const business of businesses) {
        business.level = 0;
        // If you have initial costs and incomes defined somewhere, reset to those values.
        // For now, I'm assuming you might have them as properties in the Business class.
        business.cost = business.initialCost;
        business.income = business.initialIncome;
        business.updateDisplay();
    }
    updateResources();
    updateIncome();
}


function getPlayerStats() {
    let totalBusinesses = 0;
    for (const business of businesses) {
        totalBusinesses += business.level;
    }
    return {
        money: resources,
        businesses: totalBusinesses,
        incomeMultiplier: 1 // This is a placeholder. Modify as needed.
    };
}


//Uppdaterar resurser
function updateResources() {
    const resourceElement = document.getElementById("resources");
    resourceInt = parseInt(resources);
    resourceElement.textContent = "Resources: " + resourceInt;

    const playerStats = getPlayerStats();
    checkForRankUp(playerStats);
}

function updateIncome() {
    let totalIncome = 0;
    // Loopar igenom verksamheterna och räknar ut totala inkomsten
    for (const business of businesses) {
        totalIncome += business.income * business.level * incomeMultiplier;
    }
    resources += totalIncome;

    document.getElementById("totalIncome").textContent = "Total Income: " + totalIncome;
    updateResources();

    const playerStats = getPlayerStats();
    checkForRankUp(playerStats);
}

// Klass för verksamheter
class Business {
    constructor(name, cost, income) {
        this.name = name;
        this.cost = cost;
        this.income = income;
        this.level = 0;
        this.element = null;
        this.initialIncome = income;
        this.initialCost = cost;
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

        const playerStats = getPlayerStats();
        checkForRankUp(playerStats);
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
const PrimordialSoupLab = new Business("Primordial Soup Lab", 10, 0.1);
PrimordialSoupLab.updateDisplay();

const StoneAgeToolWorkshop = new Business("Stone Age Tool Workshop", 50, 0.5);
StoneAgeToolWorkshop.updateDisplay();

const AgriculturalRevolutionFarm = new Business("Agricultural Revolution Farm", 200, 2);
AgriculturalRevolutionFarm.updateDisplay();

const AncientMaritimeVentures = new Business("Ancient Maritime Ventures", 1000, 10);
AncientMaritimeVentures.updateDisplay();

const MedievalAlchemyShop = new Business("Medieval Alchemy Shop", 5000, 50);
MedievalAlchemyShop.updateDisplay();

const RenaissanceInventorsWorkshop = new Business("Renaissance Inventor's Workshop", 25000, 250);
RenaissanceInventorsWorkshop.updateDisplay();

const IndustrialAgeFactory = new Business("Industrial Age Factory", 125000, 1250);
IndustrialAgeFactory.updateDisplay();

const ModernTechStartUp = new Business("Modern Tech Start-Up", 625000, 6250);
ModernTechStartUp.updateDisplay();

const SpaceExplorationCompany = new Business("Space Exploration Company", 3125000, 31250);
SpaceExplorationCompany.updateDisplay();

const IntergalacticTradeHub = new Business("Intergalactic Trade Hub", 15625000, 156250);
IntergalacticTradeHub.updateDisplay();


// Array för verksamheter
const businesses = [PrimordialSoupLab, StoneAgeToolWorkshop, AgriculturalRevolutionFarm, AncientMaritimeVentures, MedievalAlchemyShop, RenaissanceInventorsWorkshop, IndustrialAgeFactory, ModernTechStartUp, SpaceExplorationCompany, IntergalacticTradeHub];

// Uppdaterar inkomsten varje sekund
setInterval(updateIncome, 1000);


