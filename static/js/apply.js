$(function () {
    $('main section .photo-box button').click(function () {
        let id = $(this).data('name');
        $('#' + id).click();
    });

    $('main section .photo-box input').change(function () {
        if (this.files.length == 0) {
            $(this).parent('.photo-box').css('background-image', '');
            $(this).parent('.photo-box').find('button').show();
            $(this).parent('.photo-box').find('.close').hide();
        } else {
            if (readURL(this)) {
                $(this).siblings('.form-group').find('button').hide();
                $(this).parent('.photo-box').find('.close').show();
            }
        }
    });

    $('main section .photo-box .close').click(function () {
        $(this).parent().siblings().val('').change();
    });

    $('main section .social').change(function () {
        let sib = getSibling(this);

        if ($(this).val() != '') {
            $(sib).prop('required', false)
        } else {
            $(sib).prop('required', true)
        }

        function getSibling(e) {
            if ($(e).attr('name') == 'fb') return $('main section .social[name=ig]');
            else return $('main section .social[name=fb]');
        }
    });

    function readURL(input) {
        if (input.files && input.files[0]) {
            if (input.files[0].size < 6000000) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    $(input).parent('.photo-box').css('background-image', 'url("' + e.target.result + '")');
                };
                reader.readAsDataURL(input.files[0]); // convert to base64 string
                return true;
            } else {
                alert('照片尺寸不得大於6MB');
                $(input).val('');
                return false;
            }
        }
    }
});