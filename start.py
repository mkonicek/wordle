from load import character_frequencies, load_words

top_internet = "eariotnslc"
# =>
# clean, riots
# react, lions
# coast, liner
# score, latin
# sonic, alert

top_our_data = "esarolitnd"
# =>
# clean, riots
# react, lions
# coast, liner
# score, latin
# sonic, alert

words = load_words()

#freq = character_frequencies(words)
#print({k: v for k, v in sorted(freq.items(), key=lambda item: item[1])})

for i in range(len(words)):
    for j in range(i):
        word1 = words[i]
        word2 = words[j]
        if set(word1 + word2) == set(top_our_data):
            print(f"{word1}, {word2}")

