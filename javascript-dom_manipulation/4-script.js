const addItem = document.getElementById('add_item');

addItem.addEventListener('click', function() {
    let newLi = document.createElement('li');
    newLi.textContent = 'Item';

    let myList = document.querySelector('ul.my_list');

    myList.appendChild(newLi);
});
