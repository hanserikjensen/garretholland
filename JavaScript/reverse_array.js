function reverse_array(arr) {
    // for (var i = arr.length-1; i >=0; i--) {
    //     var temp = arr.pop(arr[i]);
    // }
    for (var i = 0; i <=arr.length; i++) {
        var temp = arr.pop(arr[i]);
        arr.push(arr[temp]);
    }
}

    // for (var i = 0; i <= arr.length/2; i++) {
    //     arr.splice(arr[i])
    // } return arr




console.log(reverse_array([1,2,3,4,5,6,7,8,9,10]));


// function reverse_array(arr) {
//     var temp = [];
//     var len = arr.length;
//     for (var i = (len - 1); i !== 0; i--) {
//         temp.push(arr[i]);
//     }
//     return arr;
// }
//
// console.log(reverse_array([1,2,3,4,5,6,7,8,9,10]));
