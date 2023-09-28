str = input("enter the string:")
vowels = ["A","a","E","e","I","i","O","o","U","u"]
count_vowels = ""
for i in str:
    if i in vowels:
        count_vowels = count_vowels + i
print("Number of vowels is:",len(count_vowels))
    