//2. Напишите функцию, которая переворачивает цифры заданного десятичного числа. Например: 256 652
//let number = prompt("Input a number");

// function reverseString(str) {
//     let reverse = "";
//     for (let i = str.length - 1; i >= 0; i--) {
//         reverse += str[i];
//     }
//     return reverse;
// }

// document.write(reverseString(number))


//1. Напишите функцию, которая возвращает последнюю цифру заданного целого числа в 
//виде английского слова. Примеры: 512  "two", 1024 "four", 12309 " nine"

let number = parseFloat(prompt("Input a number"));
const digitsText = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];

const getLastDigitAsText = (number) => digitsText[number % 10];

document.write(getLastDigitAsText(number));