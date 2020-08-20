
var app = angular.module("myApp", []);
app.controller("myCtrl", function($scope) {
    $scope.myTxt = "You have not yet clicked submit";

    $scope.submit = function($event) {
      $scope.myTxt = "You clicked submit!";

    }
    $scope.items = [
      { id: 1, age: 18 },
      { id: 2, age: 19},
      { id: 3, age: 20 },
      { id: 4, age: 21 },
      { id: 5, age: 22 },
      { id: 6, age: 23 },
      { id: 7, age: 24 },
      { id: 8, age: 25 },
      { id: 9, age: 26 },
      { id: 10, age: 27 },
      { id: 11, age: 28 },
      { id: 12, age: 29 },
      { id: 13, age: 30 },
      { id: 14, age: 31 },
      { id: 15, age: 32 },
      { id: 16, age: 33 },
      { id: 17, age: 34 },
      { id: 18, age: 35 },
      { id: 19, age: 36 },
      { id: 20, age: 37 },
      { id: 21, age: 38 },
      { id: 22, age: 39 },
      { id: 23, age: 40 },
      { id: 24, age: 41 },
      { id: 25, age: 42 },
      { id: 26, age: 43 },
      { id: 27, age: 44 },
      { id: 28, age: 45 },
      { id: 29, age: 46 },
      { id: 30, age: 47 },
      { id: 31, age: 48 },
      { id: 32, age: 49 },
      { id: 33, age: 50 },
      { id: 34, age: 51 },
      { id: 35, age: 52 }
    ];
});

function validateForm(email) {
    var a = document.forms["myForm"]["fname"].value;
    var b = document.forms["myForm"]["lname"].value;
    var c = document.forms["myForm"]["email"].value;
    var d = document.forms["myForm"]["city"].value;
    var e = document.forms["myForm"]["country"].value;
    var f = document.forms["myForm"]["age"].value;
    // regex for email validation
    var re = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$/;

    // check all validation like size of characters and valid email adress code
    if (a == "") {
        alert("First name must be filled out");
        document.getElementById("fname").className += " formInvalid";
        return false;
    }
    else if (b == "") {
        alert("Last name must be filled out");
        document.getElementById("lname").className += " formInvalid";
        return false;
    }
    else if (c == "") {
        alert("Email must be filled out");
        document.getElementById("email").className += " formInvalid";
        return false;
    }
    else if (d == "") {
        alert("City must be filled out");
        document.getElementById("city").className += " formInvalid";
        return false;
    }
    else if (e == "") {
        alert("Country must be chosen");
        document.getElementById("country").className += " formInvalid";
        return false;
    }
    else if (f == "") {
        alert("Country must be chosen");
        document.getElementById("age").className += " formInvalid";
        return false;
    }
    var email_validation = re.test(c);
    if (email_validation){
      return true;
    }
    else {
      alert("Invalid Email Address");
      document.getElementById("email").className += " formInvalid";
      return false;
    }
}
