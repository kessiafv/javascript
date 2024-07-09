function letterFinder(word, match) {
    var conditional1 = typeof(word) == 'string' && word.length >= 2
    var conditional2 = typeof(match) == 'string' && match.length == 1
    if (conditional1 && conditional2) {
        for(var i = 0; i < word.length; i++) {
            if(word[i] == match) {
                console.log('Found the', match, 'at', i)
            } else {
                console.log('---No match found at', i)
            }
        }
    } else {
        console.log("Please pass correct arguments to the function")
    }
}

letterFinder([],[])
letterFinder("cat", "c")
