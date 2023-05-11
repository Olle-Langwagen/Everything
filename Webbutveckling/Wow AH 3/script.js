const CLIENT_ID = 'fb766b47b70a44018d9ef888f284d5bf';
const CLIENT_SECRET = 'svU5ftd1jUO9eVe226zbZi37DHzvHNYf';
const REALM = "us";

// Step 1: Retrieve an access token
function getAccessToken() {
    return fetch('https://us.battle.net/oauth/token', {
      method: 'POST',
      body: 'grant_type=client_credentials',
      headers: {
        Authorization: `Basic ${btoa(`${CLIENT_ID}:${CLIENT_SECRET}`)}`,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    })
      .then(response => response.json())
      .then(data => data.access_token);
  }
  
  // Step 2: Search for an item by name
  function searchItem(itemName, accessToken) {
    const encodedItemName = encodeURIComponent(itemName);
    const url = `https://${REALM}.api.blizzard.com/data/wow/search/item?namespace=static-${REALM}&locale=en_${REALM.toUpperCase()}&name.en_US=${encodedItemName}&orderby=price&page=1`;
  
    return fetch(url, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText);
        }
        return response.json();
      })
      .then(data => data?.results || []);
  }
  
  // Step 3: Get auctions for an item on the specified realm
  function getAuctionsForItem(itemId, accessToken) {
    const url = `https://${REALM}.api.blizzard.com/data/wow/item/${itemId}/auctions?namespace=dynamic-${REALM}&locale=en_${REALM.toUpperCase()}&realms.slug=${REALM}`;
  
    return fetch(url, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText);
        }
        return response.json();
      })
      .then(data => data?.auctions || []);
  }
  
  // Step 4: Perform the search and retrieve auctions for the item
  function searchAuctionsByItemName(itemName) {
    getAccessToken()
      .then(accessToken => searchItem(itemName, accessToken))
      .then(results => {
        if (results.length === 0) {
          console.log('No auctions found for the item.');
          return;
        }
  
        const itemId = results[0]?.data?.id;
  
        if (!itemId) {
          console.log('Item ID not found.');
          return;
        }
  
        return Promise.all([
          getAuctionsForItem(itemId),
        ]);
      })
      .then(([auctions]) => {
        console.log('Auctions:', auctions);
      })
      .catch(error => {
        console.error('An error occurred while searching for the item:', error);
      });
  }
  
  // Example usage: Search auctions for an item by name
  searchAuctionsByItemName('Wildercloth Bag');