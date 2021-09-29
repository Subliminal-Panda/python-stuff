# def lettercount(findv):
#     vowels = ['a','e','i','o','u']
#     consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
#     numbers = ['1','2','3','4','5','6','7','8','9','0']
#     vcount = 0
#     ccount = 0
#     numcount =0
#     othcount = 0
#     for char in findv:
#         if char in(vowels):
#             vcount += 1
#         elif char in(consonants):
#             ccount += 1
#         elif char in(numbers):
#             numcount += 1
#         else:
#             othcount += 1
#     return(f'The string you gave me contains {vcount} vowels, {ccount} consonants, {numcount} numbers and {othcount} other characters.')

# mystring = input()
# print(lettercount(mystring))

# TERRY'S WAY:
# def count(word):
#     vowels = ['a','e','i','o','u']
#     count = 0

#     for letter in word:
#         for vowel in vowels:
#             if letter == vowel:
#                 count += 1
#     return count

# print(count('here are some letters for you to tallyho!'))

# def capitalizer(stringy):
#     split = stringy.split(' ')
#     joined = ""
#     for word in split:
#         joined += str(word).capitalize() + ' '
#     joined = joined[:-1]

#     print(joined)


# capitalizer(input())

# TERRY'S WAY:
# def capitalizer(string):
#     return ' '.join(list(map(lambda word: word.capitalize(), string.split())))

# print(capitalizer(input()))

# def register(people):
#     registry = []
#     def categorize(age, handicap):
#         if age >= 55:
#             if handicap > 7:
#                 cat = "senior"
#             else: cat = "open"
#         else:
#             cat = "open"
#         return cat
#     for person in people:
#         name = person[0]
#         age = person[1]
#         handicap = person[2]
#         category = categorize(age,handicap)
#         selection = (f'{name.capitalize()} will play in the {category} tournament this year.')
#         registry.append(selection)
#     for string in registry:
#         print(string)
    
# folks = [
#     ['george',57,12],
#     ['richard',54,-1],
#     ['brian',69,25],
#     ['douglas',95,-3],
#     ['archibald',40,19],
#     ['frederico',42,7],
#     ['hirsute',56,3],
#     ['giuseppi',47,4]
#     ]

# register(folks)

# TERRY'S WAY:

# def open_senior(members):
#     memberships = []

#     for age, handicap in members:

#         if age >= 55 and handicap > 7:
#             memberships.append('Senior')
#         else:
#             memberships.append('Open')

#     return memberships

# print(open_senior([(45,12),(55,21),(19,-2),(104,20),(14,18),(55,8)]))