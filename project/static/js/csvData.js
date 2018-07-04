//This file will hold all of the javascript for the csv_data.html page 

function validateYear() {

    let year = 0;
    let message = '';

    year = document.getElementById("year").value;

    if (isNaN(year) || year < 1980  || year >= 2017) {
        message = "Input is not valid";
        alert(message);
    }

}