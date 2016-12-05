function print_low_return_high(arr) {
    console.log(arr);
    console.log(Math.min(...arr));
    console.log(Math.max(...arr));
    return Math.max(...arr);
}
print_low_return_high([-900, 3, 5, 900])
