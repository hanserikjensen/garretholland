function print_return(arr) {
  console.log(arr[0]);
  return arr[1];
}

var returned = print_return([2,10])
console.log(returned);
