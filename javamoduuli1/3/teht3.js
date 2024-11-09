const num1 = Number(prompt("integer 1:"));
const num2 = Number(prompt("integer 2:"));
const num3 = Number(prompt("integer 3:"));

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

document.querySelector('#sum').innerHTML = 'Sum: ' + sum;
document.querySelector('#product').innerHTML = 'Product: ' + product;
document.querySelector('#average').innerHTML = 'Average: ' + average;
