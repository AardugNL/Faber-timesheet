odoo.define('website_portal', function(require) {
    'use strict';
    require('website.website');
    require('web.dom_ready');
//    $(".input-search input.myInputsearch").on("change", function () {
//          var input, filter, table, tr, td, i, date, name, project;
//          input = document.getElementById("myInput");
//          var vals = this.value;
//          filter = input.value.toUpperCase();
//          table = document.getElementById("timesheet_table");
//          tr = table.getElementsByTagName("tr");
//          for (i = 0; i < tr.length; i++) {
//            name = tr[i].getElementsByTagName("td")[1];
//            if (name) {
//              if (name.innerHTML.toUpperCase().indexOf(filter) > -1) {
//                tr[i].style.display = "";
//              } 
//              else {
//                tr[i].style.display = "none";
//              }
//            }
//          }   
//        });


    $(".input-search input.myInputsearch").on("change", function () {
          var input, filter, table, tr, td, i, date, name, project;
          input = document.getElementById("myInput");
          var vals = this.value;
          filter = input.value.toUpperCase();
          table = document.getElementById("timesheet_table");
          tr = table.getElementsByTagName("tr");
          for (i = 0; i < tr.length; i++) {
            date = tr[i].getElementsByTagName("td")[0];
            name = tr[i].getElementsByTagName("td")[1];
            if (date) {
              if (date.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
              } else if (name) {
                  if (name.innerHTML.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                  } else {
                    tr[i].style.display = "none";
                  }
            }
          }   
        }
    });


        

    if(!$('.o_website_portal_details').length) {
        return $.Deferred().reject("DOM doesn't contain '.o_website_portal_details'");
    }

    var state_options = $("select[name='task_id']:enabled option:not(:first)");
    $('.o_website_portal_details').on('change', "select[name='project_id']", function () {
        var select = $("select[name='task_id']");
        state_options.detach();
        var displayed_state = state_options.filter("[data-project_id="+($(this).val() || 0)+"]");
        var nb = displayed_state.appendTo(select).show().size();
        select.parent().toggle(nb>=0);
    });
    $('.o_website_portal_details').find("select[name='project_id']").change();
    
});
