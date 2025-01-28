s = input("Enter a sentence: ")#user inputs a sentence
word_list = s.split()#to split the sentence into words 
wcnt = {}# Initialize an empty dictionary to store word counts
for word in word_list:#iterates every word in the dictionary
    word = word.lower()  #to convert the word into lower case
    if word in wcnt:#Check if the word is already in the dictionary
        wcnt[word] += 1 #If the word is in the dictionary, increment its count
    else:
        wcnt[word] = 1# If the word is not in the dictionary, add it with count 1
print("Word Count:")# Print a heading for the word count output
# Loop through the dictionary to print each word and its count
for word, count in wcnt.items():
    print(f"{word}: {count}")
