const INITIAL_RATE = 50;
const TOTAL_RATE = 100;
const TIME_DELAY = 3000;

// runs when the document is ready
$(document).ready(function() {

    // acquiring the csrf_token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    let csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    // set the header of AJAX request
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    // method to reset the from values
    $('#reset_predict_button').on('click', function(event) {
        event.preventDefault();
        $('#predict_form').trigger('reset');

        drawChart(INITIAL_RATE, INITIAL_RATE, 'Favorable Prediction Data');
    });

    $('#reset_aggregate_button').on('click', function(event) {
        event.preventDefault();
        $('#aggregate_form').trigger('reset');

        drawChart(INITIAL_RATE, INITIAL_RATE, 'Favorable Aggregation Data')

    });

    $('#predict_button').on('click', function(event) {
        event.preventDefault();

        let dataArray = $('#predict_form').serializeArray();
        console.log(dataArray);

        $.ajax({
            url: '/predict',
            data: {
                'claims': dataArray[1].value,
                'appeal_category': dataArray[2].value,
                'medicare_part': dataArray[3].value,
                'requestor_type': dataArray[4].value,
                'state': dataArray[5].value,
                'psc_zpic': dataArray[6].value,
                'rac': dataArray[7].value,
                'procedure_code': dataArray[8].value,

            },
            type: 'POST',
            dataType: 'json'
        }).done(function(data) {
            let favorable = data.favorable;
            let unfavorable = data.unfavorable;

            console.log(favorable);
            console.log(unfavorable);

            drawChart(favorable, unfavorable, 'Favorable Prediction Data');

        });
    });

    $('#aggregate_button').on('click', function(event) {
        event.preventDefault();

        let data = {};
        $('select option:selected').each(function() {
            if ($(this).val() !== "") {
                let attribute = $(this).parent().attr('id');
                data[attribute] = $(this).text();
            }
        });

        console.log(data);

        $.ajax({
            url: '/aggregate',
            data: data,
            type: 'POST',
            dataType: 'json'
        }).done(function(data) {

            if (!data.is_empty) {
                let favorable = data.favorable;
                let unfavorable = data.unfavorable;

                drawChart(favorable, unfavorable, 'Favorable Aggregation Data');

            } else {
                alert("There are no cases meets the query.");
            }
        });

    });

    function drawChart(favorable, unfavorable, title) {
        let data = google.visualization.arrayToDataTable([
            ['Favorable', 'Predicted approve rate'],
            ['Favorable', favorable],
            ['Unfavorable', unfavorable]
        ]);

        let options = {
            title: title,
            pieHole: 0.4,
        };

        let chart = new google.visualization.PieChart(document.getElementById('pie_chart'));

        chart.draw(data, options);
    }
});
