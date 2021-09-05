import Foundation



var word = "prova vaporware"
var  carattere = String()



for i in word{
  var spazio = "  "
  spazio.append(i.uppercased())
  carattere += spazio

}

print(carattere)