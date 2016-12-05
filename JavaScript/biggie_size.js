function biggie_size(arr) {
    for (var i in arr) {
        if (arr[i] > 0) {
            arr[i] = "big";
        }
    } console.log(arr);
}


biggie_size([-1, 3, 5, -5])
