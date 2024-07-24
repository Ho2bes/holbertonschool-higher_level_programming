document.addEventListener('DOMContentLoaded', function() {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  const helloElement = document.getElementById('hello');

  fetch(url)
      .then(response => {
          if (!response.ok) {
              throw new Error('Erreur réseau : ' + response.status);
          }
          return response.json();
      })
      .then(data => {
          helloElement.textContent = data.hello;
      })
      .catch(error => {
          console.error('Il y a eu un problème avec la requête Fetch :', error);
          helloElement.textContent = 'Erreur de chargement';
      });
});
