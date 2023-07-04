# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
#           spinWords( "This is a test") => returns "This is a test" 
#           spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    arr = sentence.split(' ')
    arr2 = []

    for word in arr:
        if len(word) < 5:
            arr2.append(word)
        else:
            rev = list(word)
            rev.reverse()
            arr2.append(''.join(rev))
    return ' '.join(arr2)

    

print (spin_words("Welcome"))
print (spin_words("Hey fellow warriors"))

array = ['hey', 'fellow', 'warriors']
string= 'hola'

for x in array:
   print (x[::2])

print(string[::-1])