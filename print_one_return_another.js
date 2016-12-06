function print_one_return_another(arr) {
    console.log(arr[arr.length-2]);
    for (var x in arr) {
        if (arr[x] % 2 != 0) {
            console.log(arr[x]);
            break
        }
    }
}

print_one_return_another([13,5,7])
