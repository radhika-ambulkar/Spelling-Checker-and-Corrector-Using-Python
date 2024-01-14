#Spelling checker and corrector

from textblob import TextBlob

from textblob import Word

import enchant

p = input("Enter sentence you want to check : ")           

print("Original words : ",p)
    
op1=input("Do you want corrrect spellings (yes/no): ")

dict = enchant.Dict("en_US")

if op1=="yes" or op1=="Yes":
    words=p.split()
    misspelled =[]
    for word in words:
        if dict.check(word) == False:
            misspelled.append(word)
    print("The misspelled words are : " + str(misspelled))
    b = TextBlob(p)
    msg=b.correct()
    print("Corrected text: ",end="")
    print(msg)
    op2=input("Do you want more sugestions (yes/no): ")

    if op2=="yes" or op2=="Yes":
        for word in misspelled:
            print("Suggestion for " + word + " : " + str(dict.suggest(word)))
            
    elif op2=="no" or op2=="No":
        print("Ok!!") 

elif op1=="no" or op1=="No":
    print("Ok!!")

else:
    print("Something went wrong!!")
