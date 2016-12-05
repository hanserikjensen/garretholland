function countdown(num) {
  var arr = [];
  for ( ; num >= 0; num--){
    arr.push(num)
  }
  console.log(arr);
  console.log("length = " + arr.length);
}

countdown(20)
