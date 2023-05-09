const CLIENT_ID = 'fb766b47b70a44018d9ef888f284d5bf';
const CLIENT_SECRET = 'svU5ftd1jUO9eVe226zbZi37DHzvHNYf';

let accessToken = null;

// Fetch realms based on the selected region
async function fetchRealms(region) {
  try {
    const response = await fetch(
      `https://${region.toLowerCase()}.api.blizzard.com/data/wow/realm/index?namespace=dynamic-${region.toLowerCase()}&locale=en_${region.toUpperCase()}&access_token=${accessToken}`
    );
    const data = await response.json();

    const realmSelect = document.getElementById('realm');
    realmSelect.innerHTML = '';
    console.log(accessToken, data);
    data.realms.forEach(function (realm) {
      const option = document.createElement('option');
      option.value = realm.slug;
      option.textContent = realm.name;
      realmSelect.appendChild(option);
    });
  } catch (error) {
    console.error('Error fetching realms:', error);
  }
}

// Fetch item auction data
async function fetchItemAuction(region, realm, itemName) {
  try {
    // Get realm ID from the realm list API
    const realmListResponse = await fetch(`https://${region.toLowerCase()}.api.blizzard.com/data/wow/realm/index?namespace=dynamic-${region.toLowerCase()}&locale=en_${region.toUpperCase()}&access_token=${accessToken}`);
    const realmListData = await realmListResponse.json();

    console.log('Realm List Data:', realmListData);

    const targetRealm = realmListData.realms.find((r) => r.name.toLowerCase() === realm.toLowerCase());

    if (targetRealm) {
      const realmId = targetRealm.id;

      // Search for item data
      const itemSearchResponse = await fetch(`https://${region.toLowerCase()}.api.blizzard.com/data/wow/search/item?namespace=static-${region.toLowerCase()}&locale=en_${region.toUpperCase()}&name.en_US=${itemName}&access_token=${accessToken}`);
      const itemSearchData = await itemSearchResponse.json();

      console.log('Item Search Data:', itemSearchData);

      if (itemSearchData.results && itemSearchData.results.length > 0) {
        const itemId = itemSearchData.results[0].data.id;

        // Fetch connected realm ID for the specified realm
        const connectedRealmResponse = await fetch(`https://${region.toLowerCase()}.api.blizzard.com/data/wow/realm/${realmId}?namespace=dynamic-${region.toLowerCase()}&locale=en_${region.toUpperCase()}&access_token=${accessToken}`);
        const connectedRealmData = await connectedRealmResponse.json();

        console.log('Connected Realm Data:', connectedRealmData);

        if (connectedRealmData.connected_realm && connectedRealmData.connected_realm.href) {
          const connectedRealmId = connectedRealmData.connected_realm.href.split('/').pop();

          // Fetch auction data for the connected realm
          const auctionResponse = await fetch(`https://${region.toLowerCase()}.api.blizzard.com/data/wow/connected-realm/${connectedRealmId}/auctions?namespace=dynamic-${region.toLowerCase()}&locale=en_${region.toUpperCase()}&access_token=${accessToken}`);
          if (auctionResponse.status === 404) {
            throw new Error('Auction data not found');
          }
          const auctionData = await auctionResponse.json();

          console.log('Auction Data:', auctionData);

          // Filter the auction data to find the specific item
          const itemAuctions = auctionData.auctions.filter((auction) => auction.item.id === itemId);

          if (itemAuctions.length > 0) {
            const auctionPrice = itemAuctions[0].buyout / 10000; // Convert copper to gold
            const itemResult = document.getElementById('itemResult');
            itemResult.innerHTML = `Item: ${itemName}<br>Price: ${auctionPrice} gold<br>Realm ID: ${connectedRealmId}`;
            return;
          }
        } else {
          throw new Error('Connected realm not found');
        }
      } else {
        throw new Error('Item not found');
      }
    } else {
      throw new Error('Realm not found');
    }

    const itemResult = document.getElementById('itemResult');
    itemResult.innerHTML = 'Item not found or no auctions available.';
  } catch (error) {
    console.error('Error fetching item auction:', error);
    const itemResult = document.getElementById('itemResult');
    itemResult.innerHTML = 'Error fetching item auction.Please try again later.';
  }
}



// Request access token using client ID and client secret
async function requestAccessToken() {
  try {
    const response = await fetch('https://us.battle.net/oauth/token', {
      method: 'POST',
      body: 'grant_type=client_credentials',
      headers: {
        Authorization: `Basic ${btoa(`${CLIENT_ID}:${CLIENT_SECRET}`)}`,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });

    const data = await response.json();
    accessToken = data.access_token;
  } catch (error) {
    console.error('Error requesting access token:', error);
  }
}

// Handle form submission
function handleFormSubmit(event) {
  event.preventDefault();

  const region = document.getElementById('region').value;
  const realm = document.getElementById('realm').value;
  const itemName = document.getElementById('itemName').value;

  fetchItemAuction(region, realm, itemName);
}

// Populate realms when the region selection changes
document.getElementById('region').addEventListener('change', function () {
  const selectedRegion = this.value;
  fetchRealms(selectedRegion);
});
// Add form submit event listener
document.getElementById('itemLookupForm').addEventListener('submit', handleFormSubmit);

// Request access token when the page loads
window.addEventListener('DOMContentLoaded', requestAccessToken);

// Request access token when the page loads
window.addEventListener('DOMContentLoaded', async () => {
    try {
      const tokenResponse = await fetch('https://us.battle.net/oauth/token', {
        method: 'POST',
        body: 'grant_type=client_credentials',
        headers: {
          Authorization: `Basic ${btoa(`${CLIENT_ID}:${CLIENT_SECRET}`)}`,
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });
  
      const tokenData = await tokenResponse.json();
      accessToken = tokenData.access_token;
  
      // Fetch realms for the initial region selection
      const initialRegion = document.getElementById('region').value;
      fetchRealms(initialRegion);
    } catch (error) {
      console.error('Error requesting access token:', error);
    }
  });