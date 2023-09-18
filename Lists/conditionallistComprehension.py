prevList= [-1, 1, -20, 2, -90, 60, 45, 20]
newlist = [number for number in prevList if number > 0]
print(newlist)
newlist2 = [number*number for number in prevList if number < 0]
print(newlist2)

sentence = 'My name is Elshad'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonants = [letter for letter in sentence if is_consonant(letter)]
print(consonants)

def get_number(number):
    return number if number > 0 else 'negative number'
newlist3 = [get_number(number) for number in prevList]
print(newlist3)

