const redHeader = document.getElementById('red_header');
redHeader.addEventListener('click', function() {
    let header = document.querySelector('header');
    header.classList.add('red');
});
