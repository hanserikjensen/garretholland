// Create a function that given a string returns teh integer made from the strings digits. Given "0s1a3y5w7h9a2t4?6!8?0" return number 1357924680
string = "0s1a3y5w7h9a2t4?6!8?0"
function returnDigits(str) {
    str2 = ""
    for (var i = 0; i < str.length; i++) {
        if (parseInt(str[i])) {
            console.log(str[i]);
            str2 += str[i]
        }
    }return str2

}

console.log(returnDigits(string))
