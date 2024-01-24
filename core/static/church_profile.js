

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
var edit_profile_button = document.getElementById('edit-button-label');
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




var learn_more_button = document.getElementById('learn-more-button');
var learn_more_menu = document.getElementById('learn-more-menu');
var x_button_2 = document.getElementById('x-button-2');

learn_more_button.addEventListener('click', function() {
    
    if (learn_more_menu.classList.contains('learn-more-hidden')) {

        learn_more_menu.classList.remove('learn-more-hidden');
        learn_more_menu.classList.add('learn-more-visible');

    } else {

        learn_more_menu.classList.remove('learn-more-visible');
        learn_more_menu.classList.add('learn-more-hidden');
    }

});

x_button_2.addEventListener('click', function() {

    if (learn_more_menu.classList.contains('learn-more-visible')) {
        learn_more_menu.classList.remove('learn-more-visible');
        learn_more_menu.classList.add('learn-more-hidden');
    } else {
        learn_more_menu.classList.remove('learn-more-hidden');
        learn_more_menu.classList.add('learn-more-visible');
    }
});

// Videos and Post toggle buttons

var videos_button = document.getElementById("video-toggle-id");
var posts_button = document.getElementById("post-toggle-id");

var videos_content = document.getElementById('videos-content-id');
var posts_content = document.getElementById('posts-content-id');

videos_button.addEventListener('click', function() {
    if (videos_content.classList.contains('videos-post-visible')) {
        videos_content.classList.remove('videos-posts-hidden');
        videos_content.classList.add('videos-post-visible');
        posts_content.classList.remove('videos-post-visible');
        posts_content.classList.add('videos-posts-hidden');

        videos_button.classList.remove('videos-posts-button');
        videos_button.classList.add('videos-posts-button-grey');

        posts_button.classList.remove('videos-posts-button-grey');
        posts_button.classList.add('videos-posts-button');

    } else {
        posts_content.classList.remove('videos-post-visible');
        posts_content.classList.add('videos-posts-hidden');
        videos_content.classList.remove('videos-posts-hidden');
        videos_content.classList.add('videos-post-visible');

        videos_button.classList.remove('videos-posts-button');
        videos_button.classList.add('videos-posts-button-grey');

        posts_button.classList.remove('videos-posts-button-grey');
        posts_button.classList.add('videos-posts-button');
    }


});

posts_button.addEventListener('click', function() {
    if (posts_content.classList.contains('videos-posts-hidden')) {
        posts_content.classList.remove('videos-posts-hidden');
        posts_content.classList.add('videos-post-visible');
        videos_content.classList.remove('videos-post-visible');
        videos_content.classList.add('videos-posts-hidden');

        posts_button.classList.remove('videos-posts-button');
        posts_button.classList.add('videos-posts-button-grey');

        videos_button.classList.remove('videos-posts-button-grey');
        videos_button.classList.add('videos-posts-button');
    } else {
        videos_content.classList.remove('videos-post-visible');
        videos_content.classList.add('videos-posts-hidden');
        posts_content.classList.remove('videos-posts-hidden');
        posts_content.classList.add('videos-post-visible');

        posts_button.classList.remove('videos-posts-button');
        posts_button.classList.add('videos-posts-button-grey');

        videos_button.classList.remove('videos-posts-button-grey');
        videos_button.classList.add('videos-posts-button');
        
    }
});





