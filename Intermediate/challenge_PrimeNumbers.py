
def primeNumber(number):
    "Check if a number is prime or not"
    
    #check if is odd or even    
    if number % 2 == 0:
        #if the number is two
        if number == 2:
            return True
        return False
    else:
        
     if number == 1:
         return False   
        
     # the half of the number is enough   
     for i in range(3,number //2):
         
        if number % i == 0:
            return False
 
        else:
            continue

    return True

def primeList(number1,number2):
    "create a list of prime number within a range"
    
    primelist =[]
    for i in range(number1,number2):
         if primeNumber(i): 
          primelist.append(i)
    return primelist

def findPairs(primelist):
    "for every prime number create a list of pairs"
    
    dizionario = {}
    for i in primelist:
        dizionario[i] = []
        
        for x in range(primelist.index(i),len(primelist)):
            dizionario[i].append(primelist[x])
    return dizionario        


def prime_in_pairs(dizionario):
    conteggio = 0
    for x in dizionario:
        for i in range(len(dizionario[x])):
            numero =  x * dizionario[x][i]
            somma = 0
           
            for y in str(numero):
                somma += int(y)
               
            if primeNumber(somma):
                    
                    conteggio +=1
                    
    return conteggio
             
              
    



 



if __name__=='__main__':

     
 dictionary = findPairs(primeList(2,300))
 
 print(prime_in_pairs(dictionary))
     