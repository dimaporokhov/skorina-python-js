var n = parseInt(prompt("Input size of matrix"));
let arr = [];


//1) Дана целочисленный вектор А(n). Найти количество положительных элементов, стоящих
//между минимальным и максимальным элементами вектора.
//for( let i = 0; i < n; i++) arr.push(parseInt(prompt("array["+i+"]")));
// let max_i = 0,
//     min_i = 0,
//     max = arr[0],
//     min = arr[0];

// for( let i = 0; i < n; i++){
//     if (arr[i] >= max){
//         max = arr[i]
//         max_i = i
//     }
//     if (arr[i] <= min){
//         min = arr[i]
//         min_i = i
//     }
// }

// let begin = Math.min(max_i, min_i)
// let end = Math.max(max_i, min_i)

// let result = 0;
// if (end - begin > 1)
//     for(let i = begin; i < end; i++)
//         if (arr[i] > 0 && i != begin) 
//             result = result + 1;

// alert("arr -->" + arr + " result --> " + result);


//2) Если у вещественного вектора A(n) хотя бы один элемент меньше, чем 2, 
//то все отрицательные компоненты заменить их квадратами, оставив все остальные без изменения. В противном
//случае вектор A умножить на 0.5. На печать выдавать исходный и полученный вектора.


for( let i = 0; i < n; i++) arr.push(parseFloat(prompt("array["+i+"]")));
let finish_arr = arr.slice();

min = Math.min(...finish_arr)
if (min < 2)
    for(let i = 0; i < n; i++)
        if (i % 2 == 0)
            finish_arr[i] *= finish_arr[i];

if (min >= 2)
    for(let i = 0; i < n; i++)
        finish_arr[i] *= 0.5;

alert("sorce --> " + arr + "\nresult --> " + finish_arr)
