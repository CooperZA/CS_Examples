/* 
Pricing Scheme:
Wooden fencing costs $35 per foot
Chainlink fencing costs $25 per foot
Gates cost $165 each and 1, 2, or 3 can be purchased
Tax rate is 9%
*/

let length;
let width;
let fence_type;
let gates;

// price variables
const wood_p = 35;
const chain_p = 25;
const gate_p = 165;
const tRate = 0.09;

const fence_function = (length, width, type, gates) => {
    // total var
    let total;
    // calculate perimeter
    let perimeter = double(length) + double(width);

    // check fence type
    type = type.toLowerCase();

    if (type === 'chainlink') {
        total = chain_p * perimeter;
    } else if (type === 'wooden') {
        total = wood_p * perimeter;
    } 

    // add gates to total
    total += (gates * gate_p);

    // apply tax rate
    total *= (1 + tRate);

    // ouput alert
    alert('The price is $' + total.toFixed(2));
}

const double = (x) => {
    return x * 2;
}


