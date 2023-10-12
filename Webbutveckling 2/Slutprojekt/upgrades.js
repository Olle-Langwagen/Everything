

// Uppgraderings-klassen
class Upgrade {
    constructor(name, cost, businessName, requiredLevel, effect) {
        this.name = name;
        this.cost = cost;
        this.businessName = businessName;
        this.requiredLevel = requiredLevel;
        this.effect = effect;
        this.purchased = false;
        this.element = null;
    }

    apply() {
        if (!this.purchased && resources >= this.cost) {
            resources -= this.cost;
            this.purchased = true;
            this.effect(this.businessName);
            updateResources();
            
            //tar biort uippgraeringen från skärmen
            if (this.element) {
                this.element.remove();
                this.element = null;
            }
        }
    }

    checkCriterion() {
        const business = businesses.find(b => b.name === this.businessName);
        return business && business.level >= this.requiredLevel;
    }

    updateDisplay() {
        //Denna kollar om uppgraderingen är köpt och om kritetrt är uppgfyllt-
        if (!this.purchased && this.checkCriterion()) {
            if (!this.element) {
                this.element = document.createElement("div");
                document.getElementById("upgradesContainer").appendChild(this.element);
            }
            
            this.element.innerHTML = `
                <p>${this.name}</p>
                <p>Cost: ${this.cost} resources</p>
                <button id="${this.name}UpgradeButton">Purchase</button>
            `;
            
            document.getElementById(`${this.name}UpgradeButton`).addEventListener("click", () => {
                this.apply();
            });
        }
    }
}





function resetUpgrades() {
    for (const upgrade of upgrades) {
        upgrade.purchased = false;
        // If there are specific effects that need to be undone when resetting, you can do that here.
        // For now, I assume just setting purchased to false is enough.

        // Remove existing display if any
        if (upgrade.element) {
            upgrade.element.remove();
            upgrade.element = null;
        }
    }
}










// UPGRADDERINGAR //


//Håller alla uppgraderingar så dom lätt kan uppdateras.
const upgrades = [];



const doubleFarmIncome = new Upgrade(
    "Double Farm Income", 
    200, 
    "Primitive Farm", 
    5, 
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);
const doubleFarmIncome2 = new Upgrade(
    "Double Farm Income", 
    5000, 
    "Primitive Farm", 
    10, 
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleBlacksmithIncome = new Upgrade(
    "Double Blacksmith Income", 
    5000, 
    "Blacksmith", 
    5, 
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleBlacksmithIncome2 = new Upgrade(
    "Double Blacksmith Income", 
    50000, 
    "Blacksmith", 
    10, 
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleResarchFacilityIncome = new Upgrade(
    "Double Research Facility Income", 
    500000, 
    "Research Facility", 
    2, 
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);






//Lägger till alla uppgraderingar i arrayen.
upgrades.push(doubleFarmIncome, doubleFarmIncome2, doubleBlacksmithIncome, doubleBlacksmithIncome2, doubleResarchFacilityIncome);


































//Uppdaterar displayen varje sekund så att nya uppgraderingar kan ses.
setInterval(() => {
    upgrades.forEach(upgrade => {
        upgrade.updateDisplay();
    });
}, 1000);
