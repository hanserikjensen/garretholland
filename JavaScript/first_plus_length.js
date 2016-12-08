function functionName(arr) {
    for (var x in arr) {
        if (arr[x] > arr[1]) {
            console.log(arr[x]);
        }
    }
}

functionName(1,3,5,7,9,13)
