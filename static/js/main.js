$(document).ready(function(){
    $('.header').height($(window).height());

    $("#back-top").hide();
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('#back-top').fadeIn();
        } else {
            $('#back-top').fadeOut();
        }
    });

    $('#back-top').click(function () {
        $('body, html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });


    $(function() {
        $('.animate').on('mouseenter', function(e) {
			var parentOffset = $(this).offset(),
      		relX = e.pageX - parentOffset.left,
      		relY = e.pageY - parentOffset.top;
			$(this).find('span').css({top:relY, left:relX})
        })
        .on('mouseout', function(e) {
			var parentOffset = $(this).offset(),
      		relX = e.pageX - parentOffset.left,
      		relY = e.pageY - parentOffset.top;
    	    $(this).find('span').css({top:relY, left:relX})
        });
        $('[href=#]').click(function(){return false});
    });

    $(function(){
        $('[data-toggle="tooltip"]').tooltip();
    });

    var buttons_for_delete = $('.fa-trash').parent();
    var buttons_for_update = $('.fa-pencil').parent();

    $(buttons_for_delete).on('click', function() {
        var self = this;
        $.confirm({
            title: 'Удаление блюда',
            content: 'Вы действительно хотите удалить это блюдо?',
            buttons: {
                Yes: function() {
                    var csrf_token = "{{csrf_token()}}";
                    var dish_name = $(self).siblings('p:first').text();
                    $.ajax
                    ({
                        url: '/delete',
                        method: "POST",
                        contentType: 'application/json;charset=UTF-8',
                        data : JSON.stringify({'dish_name': dish_name}),
                        success : function()
                        {
                            $(self).closest('.row').remove();
                        },
                        error : function(request, status, error)
                        {
                            alert(request.responseText);
                        },
                        beforeSend: function(xhr, settings)
                        {
                            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain)
                                xhr.setRequestHeader("X-CSRFToken", csrf_token);
                        }
                    });
                },
                No: function() { }
            }
        });
    });

    $(buttons_for_update).on('click', function() {
        $.confirm({
            title: 'Редактирование блюда',
            content: 'Вы действительно хотите отредактировать данные об этом блюде?',
            buttons: {
                confirm: function () {
                    $.alert('Confirmed!');
                },
                cancel: function () {
                    $.alert('Canceled!');
                }
            }
        });
    });
});