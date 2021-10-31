def count_letter_occurences(word):
    old_list = []
    for letter in word:
        if letter not in old_list:
            print(letter + " => " + str(word.count(letter)))
        old_list.append(letter)
word = input("WORD: ")
count_letter_occurences(word=word)