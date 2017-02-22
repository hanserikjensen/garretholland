// Remove blanks
// Create a function that given a string returns all of that strings contents but without blanks if given the string " Pl   ayTha  tF   u  nkyM  usi    c  " return "PlayThatFunkyMusic"
var str = ' Pl   ayTha  tF   u  nkyM  usi    c  '
function removeBlanks(str) {
    // var strArray = [str]
    var str2 = ''
    // console.log("this is str-->",str);
    for (var i = 0; i < str.length; i++) {
        // console.log("this is index--->", i);
        if ( str[i] !== " " ) {
            // console.log(str[i]);
            str2 = str2 + str[i]
            // console.log(str2);

        }
    }
    // console.log(str2);
    return str2

}

// function removeBlanks(str) {
//     var str = [str]
//      console.log("this is str-->",str);
//     for (var i in str) {
//         console.log("this is index--->", i);
//         if ( str[i] === " " ) {
//             console.log("string[i] is---->");
//             str.pop(i)
//             str(console.log(str));
//         }
//     }
// }


console.log(removeBlanks(str))
