// Predict 1

function myBirthYearFunc(){
    console.log("I was born in" + 1980);
}
myBirthYearFunc();
// The console.log will state "I was born in 1980"

// Predict 2

function myBirthYearFunc(birthYearInput){
    console.log("I was born in" + birthYearInput);
}
myBirthYearFunc(1980);
// The console.log will "state I was born in1980"

// Predict 3

function add(num1, num2){
    console.log("Summing Numbers!");
    console.log("num1 is: " + num1);
    console.log("num2 is: " + num2);
    var sum = num1 + num2;
    console.log(sum);
}
add(10, 20);
/* 
"Suming Numbers!"
"num1 is: 10"
"num2 is: 20"
30
*/