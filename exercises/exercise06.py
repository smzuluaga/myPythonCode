# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
# The marketing team is spending way too much time typing in hashtags. Let's help them with our own Hashtag Generator!
# Here's the deal:  t must start with a hashtag (#). // All words must have their first letter capitalized. // If the final result is longer than 140 chars it must return false. // If the input or the result is an empty string it must return false.
# Examples: " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata" // "    Hello     World   "  =>  "#HelloWorld" // ""   =>  false

def generate_hashtag(s):
    if len(s) > 140 or len(s) == 0:
        return False
    else:
        return f'#{s.title().replace(" ", "")}'

#Pruebas en consola / console test
print(generate_hashtag('Codewars'))
print(generate_hashtag('Codewars      '))
print(generate_hashtag('      Codewars'))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('codewars is nice'))
print(generate_hashtag('CoDeWaRs is niCe'))
print(generate_hashtag('c i n'))
print(generate_hashtag('codewars  is  nice'))
print(generate_hashtag(''))
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong'))