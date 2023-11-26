
// Snippet 1
function hello() {
    console.log('hello');
}
hello();
console.log('Dojo');
/*
"hello"
"Dojo"
*/ 


// Snippet 2
function hello() {
    console.log('hello');
    return 15;
}
var result = hello();
console.log('result is', result);
/*
"hello"
"result is" 15
*/ 


// Snippet 3
function numPlus(num) {
    console.log('num is', num);
    return num+15;
}
var result = numPlus(3);
console.log('result is', result);
/*
"num is" 3
"results is" 18
*/ 


// Snippet 4
var num = 15;
console.log(num);
function logAndReturn(num){
   console.log(num);   
   return num;
}
var result = logAndReturn(10);
console.log(result);
console.log(num);
/*
15
10
10
15
*/ 


// Snippet 5
var num = 15;
console.log(num);

function timesTwo(num){
   console.log(num);   
   return num*2;
}
var result = timesTwo(10);
console.log(result);
console.log(num);
/*
15
10
20
15
*/ 


// Snippet 6
function timesTwoAgain(num) {
    console.log('num is', num);
    var y = num*2;
    return y;
}
var result = timesTwoAgain(3) + timesTwoAgain(5);
console.log('result is', result);
/*
"num is" 3
"num is" 5
"results is" 16

Im starting to undertand and get it now more or less but these are good ways to learn and pratice this and actully learn it!
*/ 


// Snippet 7
function sumNums(num1, num2) {  
    return num1+num2;
 }
 console.log(sumNums(2,3))
 console.log(sumNums(3,5))
/*
5
8
*/ 


// Snippet 8
function printSumNums(num1, num2) {
    console.log(num1);   
    return num1+num2;
 }
 console.log(printSumNums(2,3))
 console.log(printSumNums(3,5))
/*
I think it read it a line at a time? So first because it asking what is num1 because it is a 2 then it asked what is 2+3 is and  it is 5 the it repeats to the 2nd console and it is a 3 then it asked what is 3+5 and it is 8

2
5
3
8
*/ 


// Snippet 9
function sumNums(num1, num2) {
    var sum = num1 + num2;
    console.log('sum is', sum);
    return sum;
}
var result = sumNums(2,3) + sumNums(3,5);
console.log('result is', result);
/*
"sum is" 5
"sum is" 8
"results is" 13
*/ 


// Snippet 10
function sumNums(num1, num2) {
    var sum = num1 + num2;
    console.log('sum is', sum);
    return sum;
}
var result = sumNums(2,3) + sumNums(3,sumNums(2,1)) + sumNums(sumNums(2,1),sumNums(2,3));
console.log('result is', result);
/*
"sum is" 5

"sum is" 3
"sum is" 6
"sum is" 3
"sum is" 5
"sum is" 8
"results is" 19

This one was a bit of a brain teaser took me a while to understand what is going on but after looking up what was going on, on Trace 
I understood what was going on I was almost right Just missed a step but after seeing how everything worked it made sense!
After I reworked through it again this is what I got!
*/ 