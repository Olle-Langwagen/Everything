const CLIENT_ID = 'fb766b47b70a44018d9ef888f284d5bf';
const CLIENT_SECRET = 'svU5ftd1jUO9eVe226zbZi37DHzvHNYf';
const REALM = "1136";

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
    const access_token = data.access_token;
    const url = `https://us.api.blizzard.com/data/wow/connected-realm/${REALM}/auctions?namespace=dynamic-us&locale=en_US&access_token=${access_token}`;

    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText);
        }
        return response.json();
      })
      .then(data => {
        const auctions = data.auctions.slice(0, 50);

        if (auctions.length === 0) {
          const errorMessage = document.createElement('p');
          errorMessage.textContent = 'No auctions found.';
          document.getElementById('auctions-container').appendChild(errorMessage);
          return;
        }

        const itemIds = auctions.map(auction => auction.item.id);

        const itemPromises = itemIds.map(itemId =>
          fetch(`https://us.api.blizzard.com/data/wow/item/${itemId}?namespace=static-us&locale=en_US&access_token=${access_token}`)
            .then(response => {
              if (!response.ok) {
                throw new Error(response.statusText);
              }
              return response.json();
            })
        );

        Promise.all(itemPromises)
          .then(itemData => {
            const itemsById = {};
            itemData.forEach(item => {
              itemsById[item.id] = item.name;
            });





            const searchInput = document.getElementById('search-input');
            const searchButton = document.getElementById('search-button');
            let itemData = {};
            
            // Add a click event listener to the search button
searchButton.addEventListener('click', () => {
    const searchTerm = searchInput.value.toLowerCase();
  
    // Fetch auctions data for the realm
    fetch(`https://us.api.blizzard.com/data/wow/connected-realm/${REALM}/auctions?namespace=dynamic-us&locale=en_US&access_token=${access_token}`)
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText);
        }
        return response.json();
      })
      .then(data => {
        const auctions = data.auctions;
  
        // Fetch item data for all items in a single API request
        const itemIds = auctions.map(auction => auction.item.id);
        const itemDataUrl = `https://us.api.blizzard.com/data/wow/item?namespace=static-us&locale=en_US&access_token=${access_token}&ids=${itemIds.join(',')}`;
  
        fetch(itemDataUrl)
          .then(response => {
            if (!response.ok) {
              throw new Error(response.statusText);
            }
            return response.json();
          })
          .then(responseData => {
            console.log('Fetched item data:', responseData);
            itemData = responseData;
  
            // Filter the auctions based on the search term
            const filteredAuctions = auctions.filter(auction => {
              const itemName = itemData.find(item => item.id === auction.item.id)?.name;
              return itemName && itemName.toLowerCase().includes(searchTerm);
            });
  
            console.log('Filtered auctions:', filteredAuctions);
  
            // Display the filtered auctions
            displayAuctions(filteredAuctions);
          })
          .catch(error => {
            console.error(error);
            const errorMessage = document.createElement('p');
            errorMessage.textContent = 'An error occurred while retrieving item data. Please try again later.';
            document.getElementById('auctions-container').appendChild(errorMessage);
          });
      })
      .catch(error => {
        console.error(error);
        const errorMessage = document.createElement('p');
        errorMessage.textContent = 'An error occurred while retrieving auction data. Please try again later.';
        document.getElementById('auctions-container').appendChild(errorMessage);
      });
  });
  
  
  

function displayAuctions(auctions) {
    const auctionsContainer = document.getElementById('auctions-container');
    auctionsContainer.innerHTML = ''; // Clear the existing content
  
    if (auctions.length === 0) {
      const errorMessage = document.createElement('p');
      errorMessage.textContent = 'No auctions found.';
      auctionsContainer.appendChild(errorMessage);
      return;
    }

                auctions.forEach(auction => {
                  // Create the elements and populate them with auction data
                  // ...
                  const auctionDiv = document.createElement('div');
                  auctionDiv.className = 'auction';
                
                  const priceDiv = document.createElement('div');
                  priceDiv.className = 'price';
                  /*
                  const priceImg = document.createElement('img');
                  priceImg.src = 'https://wow.zamimg.com/images/icons/money-gold.gif';
                  priceImg.alt = 'gold coin icon';
                  */
                  const priceText = document.createTextNode((auction.buyout / auction.quantity / 10000).toFixed(2));
                  const goldText  = document.createElement('span');
                  goldText.className = 'goldText';
                  goldText.innerHTML = 'g'
                  /*priceDiv.appendChild(priceImg);*/
                  priceDiv.appendChild(priceText);
                  priceDiv.appendChild(goldText);
                  auctionDiv.appendChild(priceDiv);
                
                  const itemDiv = document.createElement('div');
                  itemDiv.className = 'item';
                  const imgDiv = document.createElement('div');
                  imgDiv.className = 'img';
                  const img = document.createElement('img');
                  img.alt = itemsById[auction.item.id];
                  const itemMediaUrl = `https://us.api.blizzard.com/data/wow/media/item/${auction.item.id}?namespace=static-us&locale=en_US&access_token=${access_token}`;
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
                  itemNameLink.textContent = itemsById[auction.item.id] || 'Unknown Item';
                  nameDiv.appendChild(itemNameLink);
                  itemDiv.appendChild(nameDiv);
                  auctionDiv.appendChild(itemDiv);
                
                  const quantityDiv = document.createElement('div');
                  quantityDiv.className = 'quantity';
                  const quantityText = document.createTextNode(auction.quantity || 1);
                  quantityDiv.appendChild(quantityText);
                  auctionDiv.appendChild(quantityDiv);
                
                  document.body.appendChild(auctionDiv);
                  // Append the elements to the auctions container
                  // ...
                });
              }

              // ...
            })
            .catch(error => {
              console.error(error);
              const errorMessage = document.createElement('p');
              errorMessage.textContent = 'An error occurred while retrieving item data. Please try again later.';
              document.getElementById('auctions-container').appendChild(errorMessage);
            });
        })
        .catch(error => {
          console.error(error);
          const errorMessage = document.createElement('p');
          errorMessage.textContent = 'An error occurred while retrieving auction data. Please try again later.';
          document.getElementById('auctions-container').appendChild(errorMessage);
        });
    })
    .catch(error => console.error(error));

