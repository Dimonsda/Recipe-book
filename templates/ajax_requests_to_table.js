$(document).ready(function()
{
    var green_td;
    $('table.content').tablesorter({widgets: ['zebra']});

    $(this).on('change', '.TypeOfDish, .UnitOfMeasurement', function()
    {
        var selected_type_of_dish = $('option:selected', this).val();
        if ($(this).attr('class') == 'TypeOfDish')
            var attr_title = 'Type_Of_Dish';
        else
            var attr_title = 'Unit_of_measurement';
        var tr_for_update = $(this).parent().parent();
        var arg_id = $('td:first', $(tr_for_update)).text();
        var csrf_token = "{{csrf_token()}}";
        $.ajax
        ({
            url: '/update_from_db',
            method: "POST",
            contentType: 'application/json;charset=UTF-8',
            data : JSON.stringify({'value' : selected_type_of_dish, 'update_id' : arg_id, 'attr_title' : attr_title}),
            success: function()
            {
                $('table.content').trigger('update');
            },
            error: function(request, status, error)
            {
                alert(request.responseText);
            },
            beforeSend: function(xhr, settings)
            {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain)
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        });
    });

    $('#what_show').change(function()
    {
        var selected = $('#what_show option:selected').text();
        var csrf_token = "{{csrf_token()}}";
        $.ajax
        ({
            url: '/' + selected,
            method: 'GET',
            beforeSend: function(xhr, settings)
            {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain)
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        })
        .done(function(attributes)
        {
            var trs = $('tr', 'thead');
            $(trs).empty();
            $(attributes[0]).each(function()
            {
                $(trs[0]).append('<th>' + this);
                $(trs[1]).append('<td><input placeholder="фильтр">');
            });
            $('tbody').empty();
            var array_types_of_dish = ['Салаты и закуски', 'Бутерброды и сэндвичи',
                                                   'Блюда из мяса', 'Рыба и морепродукты',
                                                   'Соусы и маринады', 'Блюда из овощей',
                                                   'Молочные блюда', 'Крупы и макароны',
                                                   'Торты и выпечка', 'Блюда из фруктов',
                                                   'Постные блюда', 'Сладкие блюда и напитки'];
            var array_units_of_measurement = ['Грамм', 'Столовые ложки', 'Литры'];
            for (var i = 0; i < attributes[1].length; i++)
            {
                $('tbody').append('<tr class="data">');
                $(attributes[0]).each(function()
                {
                    if (this == 'Type_Of_Dish')
                    {
                        $('tr:last', 'tbody').append('<td class="item">' +
                                                        '<select class="TypeOfDish">');
                        var list_of_types = $('.TypeOfDish:last', 'tbody, tr:last, td:last');
                        $(array_types_of_dish).each(function()
                        {
                            if (this == attributes[1][i]['Type_Of_Dish'])
                                $(list_of_types).append('<option selected>' + this)
                            else
                                $(list_of_types).append('<option>' + this)
                        });
                    }
                    else if (this == 'Unit_of_measurement')
                    {
                        $('tr:last', 'tbody').append('<td class="item">' +
                                                        '<select class="UnitOfMeasurement">');
                        var list_of_units = $('.UnitOfMeasurement:last', 'tbody, tr:last, td:last');
                        $(array_units_of_measurement).each(function()
                        {
                            if (this == attributes[1][i]['Unit_of_measurement'])
                                $(list_of_units).append('<option selected>' + this)
                            else
                                $(list_of_units).append('<option>' + this)
                        });
                    }
                    else if (attributes[1][i][this] === undefined)
                        $('tr:last', 'tbody').append('<td class="item"> ');
                    else
                        $('tr:last', 'tbody').append('<td class="item">' + attributes[1][i][this]);
                });
            }
            $('table.content').tablesorter({widgets: ['zebra']});
        });
    });

    $('#apply').click(function()
    {
        if ($(green_td).text() == $('textarea.update').val())
            return;
        else
        {
            var textarea_value = $('textarea.update').val();
            var green_td_index = $(green_td).index();
            var attr_title = $($('thead th')[green_td_index]).text();
            var tr_for_update = $('td:first', $(green_td).parent());
            var arg_id = $(tr_for_update).text();
            var csrf_token = "{{csrf_token()}}";
            $.ajax
            ({
                url: '/update_from_db',
                method: "POST",
                contentType: 'application/json;charset=UTF-8',
                data : JSON.stringify({'value' : textarea_value, 'update_id' : arg_id, 'attr_title' : attr_title}),
                success: function()
                {
                    $(green_td).text(textarea_value);
                    $('table.content').trigger('update');
                    $('#apply').prop('disabled', true);
                },
                error: function(request, status, error)
                {
                    alert(request.responseText);
                },
                beforeSend: function(xhr, settings)
                {
                    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain)
                        xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
            });
        }
    });

    $('#delete').click(function()
    {
        if (!green_td)
            alert('Сначала выберите запись!');
        else if (confirm("Вы точно хотите удалить запись?"))
        {
            var tr_for_update = $('td:first', $(green_td).parent());
            var arg_id = $(tr_for_update).text();
            var csrf_token = "{{csrf_token()}}";
            $.ajax
            ({
                url: '/del_from_db',
                method: "POST",
                contentType: 'application/json;charset=UTF-8',
                data : JSON.stringify({'delete_id': arg_id}),
                success : function()
                {
                    $(green_td).parent().detach();
                    $('table.content').trigger('update');
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
        }
    });

    $('#add').click(function()
    {
        var csrf_token = "{{csrf_token()}}";
        $.ajax
        ({
            url: '/add_to_db',
            method: 'POST',
            success: function(new_id)
            {
                $('tbody').append('<tr>');
                last_tr = $('tr:last', 'tbody');
                var attr_count = $('thead tr:first th').length;
                for (var z = 0; z < attr_count; z++)
                {
                    if ($('thead tr:first th:last').text() == 'Type_Of_Dish' && z == attr_count - 1)
                        $(last_tr).append('<td class="item">' +
                                            '<select class="TypeOfDish">' +
                                                '<option selected>Салаты и закуски' +
                                                '<option>Бутерброды и сэндвичи' +
                                                '<option>Блюда из мяса' +
                                                '<option>Рыба и морепродукты' +
                                                '<option>Соусы и маринады' +
                                                '<option>Блюда из овощей' +
                                                '<option>Молочные блюда' +
                                                '<option>Крупы и макароны' +
                                                '<option>Торты и выпечка' +
                                                '<option>Блюда из фруктов' +
                                                '<option>Постные блюда' +
                                                '<option>Сладкие блюда и напитки');
                    else if ($('thead tr:first th:last').text() == 'Unit_of_measurement' && z == attr_count - 1)
                        $(last_tr).append('<td class="item">' +
                                            '<select class="UnitOfMeasurement">' +
                                                '<option selected>Грамм' +
                                                '<option>Столовые ложки' +
                                                '<option>Литры');
                    else
                        $(last_tr).append('<td class="item">');
                }
                $('td:first', last_tr).append(new_id);
                $('table.content').trigger('update');
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
    });

    $('table.content').click(function(e)
    {
        $(green_td).css("background", "");
        if ($('select', e.target).attr('class') != 'TypeOfDish' && $('select', e.target).attr('class') != 'UnitOfMeasurement')
        {
            if (e.target.className == 'item')
            {
                $(e.target).css("background", "green");
                green_td = e.target;
                $('textarea.update').text($(e.target).html());
            }
            else if (e.target.tagName == 'TH')
                $('textarea.update').empty();
        }
    });

    function filterTable(table)
    {
        var filters = $('.filters td', table);
        var rows = $('.data', table);
        $(rows).each(function(rowIndex)
        {
            var valid = true;
            $('td', this).each(function(colIndex)
            {
                if ($(filters).eq(colIndex).find('input').val())
                    if ($(this).html().toLowerCase().indexOf($(filters).eq(colIndex).find('input').val().toLowerCase()) == -1)
                        valid = valid && false;
            });
            if (valid === true)
                $(this).css('display', '');
            else
                $(this).css('display', 'none');
        });
    }

    $(this).on('input', '.filters input', function()
    {
        filterTable($(this).parents('table.content'));
        $('table.content').trigger('update');
    });

    $(this).on('input', 'textarea.update', function()
    {
        $('#apply').prop('disabled', false);
    });

    $('table.content').dblclick(function(e)
    {
        if ($('select', e.target).attr('class') != 'TypeOfDish' && $('select', e.target).attr('class') != 'UnitOfMeasurement')
        {
            $('textarea.update').prop('readonly', false);
            if (e.target.className == 'item')
                $('textarea.update').focus();
        }
    });
});