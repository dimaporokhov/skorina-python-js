//1. Если на главной диагонали стоят минимальные элементы столбцов, то ко всем элементам, 
//расположенным над главной диагональю добавить среднее арифметическое элементов стоящих 
//под главной диагональю. В противном случае матрицу оставить без изменения. 
function getResult(){
    let counter = 0;
    let counter1 = 0;
    let result = [];
    for(let i = 0; i < n; i++) result.push(arr[i].slice())

    for(let i = 0; i < n; i++)
        if (Math.min(...result[i]) == result[i][i])
            counter++;
    
    let arifm = "not all elements on the main diagonal";
    if (counter == n){
        arifm = 0;
        counter1 = 0;
        for(let i = 0; i < n; i++)
            for(let j = 0; j < n; j++)
                if (j < i){
                    arifm += result[i][j];
                    counter1 = counter1 + 1;
                }
        arifm /= counter1;


        for(let i = 0; i < n; i++)
            for(let j = 0; j < n; j++)
                if (j > i)
                    result[i][j] += arifm
    }
    

    return result
}
//2. Найти максимальный элемент среди элементов, меньших t.
// function getResult(){
//     let t = parseFloat(prompt("Input an element"));
//     let less_t = [];
//     for(let i = 0; i < n; i++)
//         for( let j = 0; j < n; j++) 
//             if (arr[i][j] < t)
//                 less_t.push(arr[i][j])
//     return Math.max(...less_t)
// }


var n = parseInt(prompt("Input size of matrix"));
let arr = [];
for( let i = 0; i < n; i++) {
    let vector = [];
    for( let j = 0; j < n; j++) 
        vector.push(parseFloat(prompt("array["+i+"]["+j+"]")));
    arr.push(vector)
}
//alert("array --> " + arr + "\nresult --> " + getResult());

let result = getResult();
let output = "";
for( let i = 0; i < n; i++)
    output += arr[i] + "    " + result[i] + "\n";

alert(output);   
