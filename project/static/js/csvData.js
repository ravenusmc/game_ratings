//This file will hold all of the javascript for the csv_data.html page 

function validateYear() {

    let year = 0;
    let message = '';

    year = document.getElementById("year").value;

    if (isNaN(year) || year < 1980  || year >= 2017) {
        message = "Year input is not valid";
        alert(message);
    }
}

//The functions below will deal with the jquery on the page 

//This function deals with the max ratings area
$(function() {

    var submit_form = function(e) {
        //The /_by_state is the method that you will use.
      $.getJSON($SCRIPT_ROOT + '/_by_max_rating', {
        year: $('input[name="year"]').val(),
        genre: $('#genre').val()
        // genre: $('input[name="genre"]').val()
      }, function(data) {
        //This is where the data will be displayed.
        $('#max_rating_results').text(data.result);
      });
      return false;
    };
    //This is what will submit the form when the user clicks the link.
    $('a#max_rating').bind('click', submit_form);
});

//This function deals with the max earnings area.
$(function() {

    var submit_form = function(e) {
        //The /_by_state is the method that you will use.
      $.getJSON($SCRIPT_ROOT + '/_by_max_earnings', {
        genre: $('#genre_max_earnings').val()
      }, function(data) {
        //This is where the data will be displayed.
        $('#max_earnings_results').text(data.result);
      });
      return false;
    };
    //This is what will submit the form when the user clicks the link.
    $('a#max_earnings').bind('click', submit_form);
});


