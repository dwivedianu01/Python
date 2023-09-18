#Let's write program to revers Statement words.

statement = "Hello My name is python, enjoy your day"
listOfWords = statement.split(' ')
print(listOfWords)

listOfWords.reverse()
print(listOfWords)

reverse_statement = (' ').join(listOfWords)
print(reverse_statement)

