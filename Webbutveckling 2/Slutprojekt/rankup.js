
const ranks = [
    { name: "Beginner", criteria: { businesses: 0, money: 0 }, bonus: { incomeMultiplier: 1 } },
    { name: "Novice", criteria: { businesses: 10, money: 1000 }, bonus: { incomeMultiplier: 1.1 } },
    { name: "Pro", criteria: { businesses: 20, money: 10000 }, bonus: { incomeMultiplier: 1.25 } },
    { name: "Warren Buffet", criteria: { businesses: 30, money: 50000 }, bonus: { incomeMultiplier: 1.5 } },
    { name: "Elon Musk", criteria: { businesses: 50, money: 100000 }, bonus: { incomeMultiplier: 2 } },

];

let currentPlayerRankIndex = 0;

function meetsCriteria(playerStats) {
    const nextRank = ranks[currentPlayerRankIndex + 1];
    if (!nextRank) return false; // Player is at max rank.

    return playerStats.businesses >= nextRank.criteria.businesses && playerStats.money >= nextRank.criteria.money;
}

function rankUp(playerStats) {
    if (!meetsCriteria(playerStats)) return false; // Can't rank up.

    currentPlayerRankIndex++;
    const newRankBonus = ranks[currentPlayerRankIndex].bonus;

    incomeMultiplier *= newRankBonus.incomeMultiplier;

    resetGame();
    resetUpgrades();

    return true;
}

function displayRankInfo() {
    const currentRank = ranks[currentPlayerRankIndex];
    const nextRank = ranks[currentPlayerRankIndex + 1];

    // Display current rank
    document.getElementById("currentRank").textContent = currentRank.name;

    // Display next rank criteria if it exists
    if (nextRank) {
        document.getElementById("nextRankCriteria").textContent = `Businesses: ${nextRank.criteria.businesses}, Money: ${nextRank.criteria.money}`;
    } else {
        document.getElementById("nextRankCriteria").textContent = "Max Rank Reached!";
    }
}

// Call this function whenever the player's stats change to check if they can rank up
function checkForRankUp(playerStats) {
    if (meetsCriteria(playerStats)) {
        // Display a button or notification to the player to rank up
        document.getElementById("rankUpButton").style.display = "block";
    } else {
        document.getElementById("rankUpButton").style.display = "none";
    }
}

// Call this when the rank up button is clicked
function onRankUpButtonClick() {
    const playerStats = getPlayerStats(); // Assuming this function is available globally from main.js
    if (rankUp(playerStats)) {
        displayRankInfo();
    }
}




window.onload = displayRankInfo;