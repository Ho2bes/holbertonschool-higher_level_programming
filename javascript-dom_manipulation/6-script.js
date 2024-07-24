const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

const characterElement = document.getElementById('character');

fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Erreur réseau : ' + response.status);
        }
        return response.json(); 
    })
    .then(data => {
        characterElement.textContent = data.name;
    })
    .catch(error => {
        console.error('Il y a eu un problème avec la requête Fetch :', error);
        characterElement.textContent = 'Erreur de chargement du personnage';
    });
