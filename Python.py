meme_dict = {
    "Word": "The description 1",
    "Word2": "The Description 2"
}

word = input("Write the Word: ")

if word in meme_dict.keys():
    definition = meme_dict[word]
    print(word, ":", definition)
else:
    print("Word", word, "not found.")
