def palindrom (word):
    for i in range(len(word)//2 + 1):    
        if(word[i] != word[-(i+1)]):
            return False
    return True

slowo = "Ala"
print("Czy %s jest palindromem ?" %slowo)
if(palindrom(slowo.lower())):
    print("%s to jest palindrom" %slowo)
else:
    print("%s to nie jest palindrom" %slowo)
