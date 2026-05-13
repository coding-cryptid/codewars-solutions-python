# Solution: Even or Odd
number = 5

def even_or_odd(number):
    if number % 2 == 0:
        return("Even")
    else:
        return("Odd")
    
solutionOne = even_or_odd(number)
print(solutionOne)


# Solution: Convert a Number to a String!
num = 123

def number_to_string(num):
    return str(num)

solutionTwo = number_to_string(num)
print(solutionTwo)


#  Solution: Remove String Spaces
x = "Hello World"

def no_space(x):
    return x.replace(" ", "")

solutionThree = no_space(x)
print(solutionThree)


# Solution: Vowel Count
sentence = "Hello World"

def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

solutionFour = get_count(sentence)
print(solutionFour)