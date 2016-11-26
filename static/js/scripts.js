$(document).ready(function() {
    $('#settings #bb-style-cnt div.add-new a').click(function() {
        $('#settings #bb-style-cnt form').fadeIn(300);
    });

    $('#profile-link').click(function() {
       $('#settings-link').removeClass('active');
       $(this).addClass('active');
        $('#settings').fadeOut(300);
        setTimeout(function() {
            $('#profile').fadeIn(300);
        },200);        
    });

    $('#settings-link').click(function() {
        $('#profile-link').removeClass('active');
        $(this).addClass('active');
        $('#profile').fadeOut(300);
        setTimeout(function() {
            $('#settings').fadeIn(300);
        },200);        
    });
});

