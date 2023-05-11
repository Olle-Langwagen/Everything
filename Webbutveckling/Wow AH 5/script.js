const CLIENT_ID = 'fb766b47b70a44018d9ef888f284d5bf';
const CLIENT_SECRET = 'svU5ftd1jUO9eVe226zbZi37DHzvHNYf';


// Fetch the access token
fetch('https://us.battle.net/oauth/token', {
  method: 'POST',
  body: 'grant_type=client_credentials',
  headers: {
    Authorization: `Basic ${btoa(`${CLIENT_ID}:${CLIENT_SECRET}`)}`,
    'Content-Type': 'application/x-www-form-urlencoded',
  },
})
  .then(response => response.json())
  .then(data => {
    const accessToken = data.access_token
    console.log(`Access token: ${accessToken}`);

    // Specify the item ID and realm ID
    const itemId = 163573;
    const realmId = '1136';

    // Make a request to the Blizzard API endpoint with the access token
    fetch(`https://us.api.blizzard.com/data/wow/connected-realm/${realmId}/auctions?namespace=dynamic-us&locale=en_US&access_token=${accessToken}`)
      .then(response => response.json())
      .then(data => {
        // Extract the auctions array from the response
        const auctions = data.auctions;

        // Filter auctions based on the searched item ID
        const filteredAuctions = auctions.filter(auction => {
          const item = auction.item;

          // Check if the item ID matches and additional properties if necessary
          if (item.id === itemId) {
            // Add additional conditions here if needed
            // For example:
            // if (item.context === YOUR_CONTEXT_VALUE) { ... }
            
            return true; // Return true to include the auction in the filtered results
          }

          return false; // Return false to exclude the auction from the filtered results
        });
        console.log(filteredAuctions)
        // Display the filtered auctions in the console
        filteredAuctions.forEach(auction => {
          const auctionId = auction.id;
          const buyoutPrice = auction.buyout;
          const quantity = auction.quantity;
          const timeLeft = auction.time_left;

          console.log(`Auction ID: ${auctionId}`);
          console.log(`Buyout Price: ${buyoutPrice}`);
          console.log(`Quantity: ${quantity}`);
          console.log(`Time Left: ${timeLeft}`);
          console.log('---');
        });
      })
      .catch(error => {
        console.error('Error:', error);
      });
  })
  .catch(error => {
    console.error('Error:', error);
  });