

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