let g_urls = {
    'login': location.origin + '/api/v1/login/',
    'logout': location.origin + '/api/v1/logout/',
};

let getCookie = function (name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

let g_csrftoken = getCookie('csrftoken');
let initLogin = function () {
    if (is_authenticated) {
        $('#non-logged-in').hide();
        $('#logged-in').show();
        // $('#span-username').html(g_auth.email);
    } else {
        $('#non-logged-in').show();
        $('#logged-in').hide();
        // $('#span-username').html('');
    }
};
$(function () {
    initLogin();
    <!--
    $('#loginButton').click(function () {
        $('#login-modal').show();
    });

    $('.close').click(function () {
        $('#modalLoginForm').removeClass('show');
    });
    -->

    $('#loginOkButton').click(function () {
        let email = $('#defaultForm-email').val();
        let password = $('#defaultForm-pass').val();
        let remember_me = $('#input-remember').prop('checked');
        if (email && password) {
            $('#modal-error').addClass('invisible');
            $.ajax({
                url: g_urls.login,
                method: "POST",
                data: {
                    email: email,
                    password: password,
                    remember_me: remember_me
                }
            }).done(function (data) {
                $('.close').click();
                // $('#modalLoginForm').hide();
                is_authenticated = true;
                initLogin();
                g_csrftoken = getCookie('csrftoken');
            }).fail(function () {
                $('#modal-error').removeClass('invisible');
            });
        } else {
            $('#modal-error').removeClass('invisible');
        }
    });
    $('#logged-in').click(function () {
        $.ajax({
            url: g_urls.logout,
            method: "POST",
            data: {
                csrfmiddlewaretoken: g_csrftoken
            }
        }).done(function () {
            is_authenticated = false;
            initLogin();
        }).fail(function () {
            console.log("FAIL");
        });
    });

});