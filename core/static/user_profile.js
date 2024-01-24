

var dropdown_button = document.getElementById('dropdown-button')
var dropdown_menu = document.getElementById('dropdown-menu')

dropdown_button.addEventListener('click', function() {
    
    if (dropdown_menu.classList.contains('features-hidden')) {

        dropdown_menu.classList.remove('features-hidden');
        dropdown_menu.classList.add('features-visible')

    } else {

        dropdown_menu.classList.remove('features-visible');
        dropdown_menu.classList.add('features-hidden')
    }



})


// Edit Profile Javascript -vvvvvvv-
var edit_container = document.getElementById('edit-container');
var edit_profile_button = document.getElementById('edit-profile-button');
var x_button = document.getElementById('x-button');

edit_profile_button.addEventListener('click', function() {

    if (edit_container.classList.contains('edit-hidden')) {
        edit_container.classList.remove('edit-hidden');
        edit_container.classList.add('edit-visible');
    } else {
        edit_container.classList.remove('edit-visible');
        edit_container.classList.add('edit-hidden');
    }
});


x_button.addEventListener('click', function() {

    if (edit_container.classList.contains('edit-visible')) {
        edit_container.classList.remove('edit-visible');
        edit_container.classList.add('edit-hidden');
    } else {
        edit_container.classList.remove('edit-hidden');
        edit_container.classList.add('edit-visible');
    }
});




