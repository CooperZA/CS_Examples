// Author: Zach Cooper
// Purpose: Class Demo
// Date: 6 February, 2020

/* Get the price of gold and multiply it by the input */
const goldPrice = 1574.70;

const goldCalc = (gold) => {
    return alert("Your gold is worth: $" + (gold * goldPrice).toFixed(2));
}

function myFunc(x, y){
    add = x + y;
    return add;
}

let twoNumbersAdded = myFunc(2, 3);

console.log(twoNumbersAdded); // result: 5


let len
const fence =300;