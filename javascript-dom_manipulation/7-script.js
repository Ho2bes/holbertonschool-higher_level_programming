const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

const listMoviesElement = document.getElementById('list_movies');

fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Erreur réseau : ' + response.status);
        }
        return response.json();
    })
    .then(data => {
        data.results.forEach(film => {
            const listItem = document.createElement('li');
            listItem.textContent = film.title;
            listMoviesElement.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error('Il y a eu un problème avec la requête Fetch :', error);
        listMoviesElement.textContent = 'Erreur de chargement des films';
    });
