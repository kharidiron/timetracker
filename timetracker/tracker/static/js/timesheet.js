$('#id_start').timepicker();
$('#id_stop').timepicker();

$("#next_day").click(function(){
    var pathArray = window.location.pathname.split('/');
    var dateString = pathArray[3] + " " + pathArray[4] + " " + pathArray[2];
    var newDateString = Date.parse(dateString).add(1).days();
    var newPath = "/tracker/" + newDateString.getFullYear() + "/" + newDateString.getMonthName(3) + "/" + newDateString.getDate();
    window.location.href = newPath;
});
$("#prev_day").click(function(){
    var pathArray = window.location.pathname.split('/');
    var dateString = pathArray[3] + " " + pathArray[4] + " " + pathArray[2];
    var newDateString = Date.parse(dateString).add(-1).days();
    var newPath = "/tracker/" + newDateString.getFullYear() + "/" + newDateString.getMonthName(3) + "/" + newDateString.getDate();
    window.location.href = newPath;
});

$("#next_month").click(function(){
    var pathArray = window.location.pathname.split('/');
    var dateString = pathArray[3] + " " + pathArray[2] ;
    var newDateString = Date.parse(dateString).add(1).months();
    var newPath = "/tracker/" + newDateString.getFullYear() + "/" + newDateString.getMonthName(3);
    window.location.href = newPath;
});
$("#prev_month").click(function(){
    var pathArray = window.location.pathname.split('/');
    var dateString = pathArray[3] + " " + pathArray[2] ;
    var newDateString = Date.parse(dateString).add(-1).months();
    var newPath = "/tracker/" + newDateString.getFullYear() + "/" + newDateString.getMonthName(3);
    window.location.href = newPath;
});

$("#next_year").click(function(){
    var pathArray = window.location.pathname.split('/');
    var dateString = pathArray[2];
    var newDateString = Date.parse(dateString).add(1).years();
    var newPath = "/tracker/" + newDateString.getFullYear();
    window.location.href = newPath;
});
$("#prev_year").click(function(){
    var pathArray = window.location.pathname.split('/');
    var dateString = pathArray[2];
    var newDateString = Date.parse(dateString).add(-1).years();
    var newPath = "/tracker/" + newDateString.getFullYear();
    window.location.href = newPath;
});

$("#today").click(function(){
    var today = Date.today();
    var newPath = "/tracker/" + today.getFullYear() + "/" + today.getMonthName(3) + "/" + today.getDate();
    window.location.href = newPath;
});
