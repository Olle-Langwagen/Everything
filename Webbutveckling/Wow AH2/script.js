// Define clientId and clientSecret globally
const clientId = 'fb766b47b70a44018d9ef888f284d5bf';
const clientSecret = 'svU5ftd1jUO9eVe226zbZi37DHzvHNYf';

async function getRealmId(region, realm, access_token) {
    const realmIndexUrl = `https://${region}.api.blizzard.com/data/wow/realm/index?namespace=dynamic-${region}&locale=en_${region.toUpperCase()}&access_token=${access_token}`;
  
    try {
      const response = await fetch(realmIndexUrl);
      if (!response.ok) {
        throw new Error('Failed to fetch realm data');
      }
      const data = await response.json();
  
      console.log('Realm Index Data:', data); // Add this line to log the received data
  
      // Find the realm ID based on the realm name
      const foundRealm = data.realms.find(r => r.name && r.name.toLowerCase() === realm.toLowerCase());
      if (foundRealm) {
        return foundRealm.id;
      } else {
        console.error('Realm not found:', realm);
        throw new Error('Realm not found.');
      }
    } catch (error) {
      console.error(error);
      throw new Error('Failed to fetch realm ID');
    }
  }
// Function to handle form submission
function handleFormSubmit(event) {
  event.preventDefault();

  const region = document.getElementById('regionSelect').value;
  const realm = document.getElementById('realmInput').value;
  const item = document.getElementById('itemInput').value;

  // Call the API and fetch auctions based on the selected region, realm, item, and access token
  fetchOAuthToken(region, realm, item);
}

// Function to fetch OAuth token
function fetchOAuthToken(region, realm, item) {
    const CLIENT_ID = 'fb766b47b70a44018d9ef888f284d5bf';
    const CLIENT_SECRET = 'svU5ftd1jUO9eVe226zbZi37DHzvHNYf';
  
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
        const accessToken = data.access_token;
  
        // Call the fetchAuctions function with the obtained access token
        fetchAuctions(region, realm, item, accessToken);
      })
      .catch(error => console.error(error));
  }
  
  async function fetchAuctions(region, realm, item, access_token) {
    const realmId = await getRealmId(region, realm, access_token);
  
    const auctionsUrl = `https://${region}.api.blizzard.com/data/wow/connected-realm/${realmId}/auctions?namespace=dynamic-${region}&locale=en_${region.toUpperCase()}&access_token=${access_token}`;
  
    fetch(auctionsUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText);
        }
        return response.json();
      })
      .then(data => {
        // Log the complete auctions data for debugging
        console.log('Auctions Data:', data.auctions);
  
        // Filter auctions based on the item ID
const filteredAuctions = data.auctions.filter(auction => {
    // Check if the auction has an item and the item ID matches
    return auction.item && auction.item.id === parseInt(item);
  });
  
  // Log the filtered auctions for debugging
  console.log('Filtered Auctions:', filteredAuctions);
  
        // Display the filtered auctions
        displayAuctions(filteredAuctions);
      })
      .catch(error => {
        console.error(error);
        const errorMessage = document.createElement('p');
        errorMessage.textContent = 'An error occurred while retrieving auction data. Please try again later.';
        document.getElementById('auctionContainer').appendChild(errorMessage);
      });
  }

  // Event listener for form submission
document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
  
    const region = document.getElementById('regionSelect').value;
    const realm = document.getElementById('realmInput').value;
    const item = document.getElementById('itemInput').value;
  
    // Fetch OAuth token and initiate auction retrieval
    fetchOAuthToken(region, realm, item);
  });
// Function to display the auctions
function displayAuctions(auctions) {
    const auctionContainer = document.getElementById('auctionContainer');
    auctionContainer.innerHTML = ''; // Clear the previous results
  
    if (auctions.length === 0) {
      const errorMessage = document.createElement('p');
      errorMessage.textContent = 'No auctions found.';
      auctionContainer.appendChild(errorMessage);
      return;
    }
  
    auctions.forEach(auction => {
      // Create auction div and populate it with auction
      const auctionDiv = document.createElement('div');
      auctionDiv.className = 'auction';
  
      const priceDiv = document.createElement('div');
      priceDiv.className = 'price';
      const priceText = document.createTextNode((auction.buyout / auction.quantity / 10000).toFixed(2));
      const goldText = document.createElement('span');
      goldText.className = 'goldText';
      goldText.innerHTML = 'g';
      priceDiv.appendChild(priceText);
      priceDiv.appendChild(goldText);
      auctionDiv.appendChild(priceDiv);
  
      const itemDiv = document.createElement('div');
      itemDiv.className = 'item';
      const imgDiv = document.createElement('div');
      imgDiv.className = 'img';
      const img = document.createElement('img');
      img.alt = auction.item.name;
      const itemMediaUrl = `https://${region}.api.blizzard.com/data/wow/media/item/${auction.item.id}?namespace=static-${region}&locale=en_${region.toUpperCase()}&access_token=${accessToken}`;
      fetch(itemMediaUrl)
        .then(response => response.json())
        .then(mediaData => {
          const asset = mediaData.assets.find(a => a.key === 'icon');
          if (asset) {
            img.src = asset.value;
          }
        })
        .catch(error => {
          console.error(error);
          img.src = 'https://dummyimage.com/56x56/000/fff.png&text=No+Image';
        });
      imgDiv.appendChild(img);
      itemDiv.appendChild(imgDiv);
      const nameDiv = document.createElement('div');
      nameDiv.className = 'name';
      const itemNameLink = document.createElement('a');
      itemNameLink.href = `https://www.wowhead.com/item=${auction.item.id}`;
      itemNameLink.className = 'wowhead';
      itemNameLink.setAttribute('data-wowhead', `item=${auction.item.id}`);
      itemNameLink.textContent = auction.item.name || 'Unknown Item';
      nameDiv.appendChild(itemNameLink);
      itemDiv.appendChild(nameDiv);
      auctionDiv.appendChild(itemDiv);
  
      const quantityDiv = document.createElement('div');
      quantityDiv.className = 'quantity';
      const quantityText = document.createTextNode(auction.quantity || 1);
      quantityDiv.appendChild(quantityText);
      auctionDiv.appendChild(quantityDiv);
  
      auctionContainer.appendChild(auctionDiv);
    });
  
    // Initialize Wowhead tooltips
    WH.Tooltip.init();
  
    // Log the fetched auctions for debugging
    console.log('Fetched Auctions:', auctions);
  }

// Event listener for form submission
document.getElementById('searchForm').addEventListener('submit', handleFormSubmit);