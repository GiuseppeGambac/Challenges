import Foundation



var word = "prova vaporware"
var  vaporwave_word = String()



for i in word{
  var spaces = "  "
  spaces.append(i.uppercased())
  vaporwave_word += spaces

}

print(vaporwave_word)