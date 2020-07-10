$(function () {
    $('main section .player button, #profile .vote-button').click(function () {
        FB.getLoginStatus((response) => {
            if (response.status == "connected") {
                let userID = FB.getUserID();
                let accessToken = FB.getAccessToken();
                let vote = $(this).data('vote');
                let csrf = $('input[name=csrfmiddlewaretoken]').val();
                // let vote = $(this
                if (userID) {
                    let formdata = new FormData();
                    formdata.append('user_id', userID);
                    formdata.append('vote', vote);
                    formdata.append('access_token', accessToken);
                    formdata.append('csrfmiddlewaretoken', csrf);
                    $.ajax({
                        type: "POST",
                        processData: false,
                        contentType: false,
                        data: formdata,
                        success: function (data) {
                            alert("投票成功~");
                            if (data == "duplicated") {
                                alert('不能重複投票在同一位參賽者上。')
                            } else {
                                if (data['voted'] == 5) {
                                    alert('今日投票額度已用完。')
                                }
                            }
                        },
                    })
                }
            } else {
                FB.login(function () {
                }, {scope: "public_profile,email"});
            }
        });
    })

    $('.bg-overlay').click(closeProfile);

    $('.owl-carousel').owlCarousel({
        loop: false,
        margin: 10,
        // nav: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        },
        autoHeight: true
    })
});

function showProfile(id) {
    var name = $('.player[data-player='+id+'] .name').text();
    var video = $('.player[data-player='+id+'] .video').text();
    var intro = $('.player[data-player='+id+'] .intro').text();
    var photoHalf = $('.player[data-player='+id+'] .photo-half').text();
    var photoWhole = $('.player[data-player='+id+'] .photo-whole').text();
    var ig = $('.player[data-player='+id+'] .ig-link').attr('href');
    var fb = $('.player[data-player='+id+'] .fb-link').attr('href');
    var youtube = $('.player[data-player='+id+'] .youtube-link').attr('href');

    console.log(video);
    $('#profile .name').text(name);
    $('#profile .into-text').text(intro);
    $('#profile .photo-half').attr('src', photoHalf);
    $('#profile .photo-whole').attr('src', photoWhole);
    $('#profile iframe').attr('src', 'https://www.youtube.com/embed/'+video);
    $('#profile .vote-button').attr('data-vote', id);
    if(fb) {
        $('#profile .fb').parent('a').attr('href', fb);
        $('#profile .fb').css('display', 'inline-block');
    }
    if(ig) {
        $('#profile .ig').parent('a').attr('href', ig);
        $('#profile .ig').css('display', 'inline-block');
    }
    if(youtube) {
        $('#profile .youtube').parent('a').attr('href', youtube);
        $('#profile .youtube').css('display', 'inline-block');
    }

    console.log(name, video, ig, fb, youtube, intro);

    var windowHeight = $(window).innerHeight() - 40;
    $('#profile').show();
    $('.bg-overlay').show();
    $('body').css('overflow', 'hidden');
    $('#profile').css('height', windowHeight);
    $('#profile').css('overflow', 'scroll');
}

function closeProfile() {
    $('#profile iframe').attr('src', '');
    $('#profile').hide();
    $('.bg-overlay').hide();
    $('body').css('overflow', 'auto');
    $('#profile .no-circle').css('display', 'none');
}
