def odd_or_even(number):
    if number % 2 ==0:
        return "Even"
    else:
        return "Odd"  #defining odd or even number
def number_to_string(num):
    return str(num)
# converted a number to a string
def get_count(sentence):
    print(sentence)
    vowels = set("aeiou")
    count = 0
    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count
#gets a vowel count
