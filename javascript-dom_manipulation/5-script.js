const updateHeader = document.getElementById('update_header');
updateHeader.addEventListener('click', function() {
    let header = document.querySelector('header');
    header.textContent = 'New Header!!!';
});
