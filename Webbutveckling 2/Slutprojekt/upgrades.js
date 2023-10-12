

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
        if (upgrade.element) {
            upgrade.element.remove();
            upgrade.element = null;
        }
    }
}
// UPGRADDERINGAR //


//Håller alla uppgraderingar så dom lätt kan uppdateras.
const upgrades = [];



const doublePrimordialSoupLabIncome = new Upgrade(
    "Double Primordial Soup Lab Income",
    200,
    "Primordial Soup Lab",
    5,
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleStoneAgeToolWorkshopIncome = new Upgrade(
    "Double Stone Age Tool Workshop Income",
    1000,
    "Stone Age Tool Workshop",
    5,
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleAgriculturalRevolutionFarmIncome = new Upgrade(
    "Double Agricultural Revolution Farm Income",
    4000,
    "Agricultural Revolution Farm",
    5,
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleAncientMaritimeVenturesIncome = new Upgrade(
    "Double Ancient Maritime Ventures Income",
    20000,
    "Ancient Maritime Ventures",
    5,
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleMedievalAlchemyShopIncome = new Upgrade(
    "Double Medieval Alchemy Shop Income",
    100000,
    "Medieval Alchemy Shop",
    5,
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleRenaissanceInventorsWorkshopIncome = new Upgrade(
    "Double Renaissance Inventor's Workshop Income",
    500000,
    "Renaissance Inventor's Workshop",
    5,
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleIndustrialAgeFactoryIncome = new Upgrade(
    "Double Industrial Age Factory Income",
    2500000,
    "Industrial Age Factory",
    5,
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleModernTechStartUpIncome = new Upgrade(
    "Double Modern Tech Start-Up Income",
    12500000,
    "Modern Tech Start-Up",
    5,
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleSpaceExplorationCompanyIncome = new Upgrade(
    "Double Space Exploration Company Income",
    62500000,
    "Space Exploration Company",
    5,
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);

const doubleIntergalacticTradeHubIncome = new Upgrade(
    "Double Intergalactic Trade Hub Income",
    312500000,
    "Intergalactic Trade Hub",
    5,
    (businessName) => {
        const business = businesses.find(b => b.name === businessName);
        if (business) {
            business.income *= 2;
            business.updateDisplay();
        }
    }
);







//Lägger till alla uppgraderingar i arrayen.
upgrades.push(doublePrimordialSoupLabIncome, doubleStoneAgeToolWorkshopIncome, doubleAgriculturalRevolutionFarmIncome, doubleAncientMaritimeVenturesIncome, doubleMedievalAlchemyShopIncome, doubleRenaissanceInventorsWorkshopIncome, doubleIndustrialAgeFactoryIncome, doubleModernTechStartUpIncome, doubleSpaceExplorationCompanyIncome, doubleIntergalacticTradeHubIncome);



































//Uppdaterar displayen varje sekund så att nya uppgraderingar kan ses.
setInterval(() => {
    upgrades.forEach(upgrade => {
        upgrade.updateDisplay();
    });
}, 1000);
