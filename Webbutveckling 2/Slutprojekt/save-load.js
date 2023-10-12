//Mycket kopierat från tidigare projekt i webb 1

window.saveGame = function() {
    const gameState = {
        resources: resources,
        incomeMultiplier: incomeMultiplier,
        currentPlayerRankIndex: currentPlayerRankIndex,
        businesses: businesses.map(b => ({
            name: b.name,
            cost: b.cost,
            income: b.income,
            level: b.level
        })),
        upgrades: upgrades.map(u => u.purchased)
    };

    localStorage.setItem('AEGameState', JSON.stringify(gameState));

    //Chatgpt hjälpte med detta
    const notification = document.getElementById('notification');
    notification.style.display = 'block';
    setTimeout(() => {
        notification.style.display = 'none';
    }, 2000);
    //Chatgpt hjälpte med detta
}

window.loadGame = function() {
    const savedGameState = localStorage.getItem('AEGameState');

    if (savedGameState) {
        const gameState = JSON.parse(savedGameState);

        resources = gameState.resources;
        incomeMultiplier = gameState.incomeMultiplier;
        currentPlayerRankIndex = gameState.currentPlayerRankIndex;

        for (let i = 0; i < businesses.length; i++) {
            businesses[i].cost = gameState.businesses[i].cost;
            businesses[i].income = gameState.businesses[i].income;
            businesses[i].level = gameState.businesses[i].level;
            businesses[i].updateDisplay();
        }

        for (let i = 0; i < upgrades.length; i++) {
            upgrades[i].purchased = gameState.upgrades[i];
            upgrades[i].updateDisplay();
        }

        updateResources();
        displayRankInfo();

        alert('Game loaded successfully!');
    } else {
        alert('No saved game found.');
    }
}


setInterval(() => {
    saveGame();
}, 100000); //Varje minut
