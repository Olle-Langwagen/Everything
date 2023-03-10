function fetchCharacterData() {
    const realm = document.getElementById('realm-input').value;
    const character = document.getElementById('character-input').value;
    const apikey = 'YOUR_API_KEY_HERE';
  
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `https://us.api.blizzard.com/profile/wow/character/${realm}/${character}?namespace=profile-us&locale=en_US&access_token=${apikey}`);
    xhr.onload = function() {
      if (xhr.status === 200) {
        const data = JSON.parse(xhr.responseText);
        console.log(data);
        // Display character data on the page
        document.getElementById('character-data').innerHTML = `
          <h2>${data.name}</h2>
          <p>Level: ${data.level}</p>
          <p>Realm: ${data.realm.name}</p>
          <p>Achievement Points: ${data.achievement_points}</p>
        `;
      } else {
        console.error(xhr.statusText);
      }
    };
    xhr.onerror = function() {
      console.error(xhr.statusText);
    };
    xhr.send();
  }
  