// from data.js
var tableData = data;

// Using the Charity Navigtaor data provided in the form of an array of JavaScript objects, write code that appends a table to your web page and then adds new rows of data for each charity.

var tbody = d3.select("tbody");
console.log(data);

data.forEach(function(charityOrg) {
  console.log(charityOrg);
  var row = tbody.append("tr");
  Object.entries(charityOrg).forEach(function([key, value]) {
    console.log(key, value);
    var cell = row.append("td");
    cell.text(value);
  });
});

// Use a text form in your HTML document and write JavaScript code that will listen for events and search through the charity cause, organization name, and location columns to find rows that match user input.
var instances = data;
var filterButton = d3.select("#filter-btn");

// Complete the click handler for the form
filterButton.on("click", function() {

    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");

    //Get the value property of the input Element
    var inputValue = inputElement.property("value");

    // Create a custom filtering function that filters dataset for user input
    function selectDate(instance) {
        return instance.datetime === inputValue;
    }

    //Use the form input to filter the data by user input
    var filteredData = instances.filter(selectDate);
    console.log(filteredData);

    // Remove table contents
    tbody.html("");

    // Only display filtered data in table
    filteredData.forEach(function(charityOrg) {
        var row = tbody.append("tr");
        Object.entries(charityOrg).forEach(function([key, value]) {
            var cell = row.append("td");
            cell.text(value);
        });
    });
});
