// Create a function that given a string returns the string's acronym (first letters only capitalized) Given "there's no free lunch - gotta pay yer way. " return TNFL-GPYW. Given "live from New York, it's Saturday Night!" return LFNYISN

string1 = " there's no free lunch - gotta pay yer way. "
string2 = "live from New York, it's Saturday Night!"
function getAcronym(str) {
    char = 0
    acronym = ""
    for (var i = 0; i < str.length; i++) {
        if (str.charAt(i) && str[i-1] === " " || str.charAt(i) && str[i-1] === undefined) {
            console.log(str[i]);
            acronym += str[i]
        }

    } return acronym.toUpperCase()
}

console.log(getAcronym(string1));
