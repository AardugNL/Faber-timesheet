odoo.define('appointment_management', function (require) {
'use strict';

var website = require('website.website');
require('web.dom_ready'); 
$("div.input-group span.fa-calendar").on('click', function(e) {
        $(e.currentTarget).closest("div.date").datetimepicker({
            useSeconds: true,
            icons : {
                time: 'fa fa-clock-o',
                date: 'fa fa-calendar',
                up: 'fa fa-chevron-up',
                down: 'fa fa-chevron-down'
            },
        });
    });
       });
