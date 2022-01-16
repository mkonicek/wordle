def load_words():
    words = []
    with open('words.txt') as f:
        for line in f:
            words.append(line.strip())
    return words

def character_frequencies(words):
    freq = {}
    for word in words:
        for char in word:
            if char in freq:
                freq[char] = freq[char] + 1
            else:
                freq[char] = 1
    return freq

# Characters at exact known positions. Example: [' ', 'a', ' ', ' ', 'c']
known = [' ', ' ', ' ', ' ', ' ']
# Chars present in the word
present = set()
# Chars we know never appear
banned = set()    

def is_possible(word, known, present, banned):
    for b in banned:
        if b in word:
            return False
    for p in present:
        if not p in word:
            return False
    for i in range(len(word)):
        if (known[i] != ' ') and known[i] != word[i]:
            return False
    return True

def find_possible(words, known, present, banned):
    return [word for word in words if is_possible(word, known, present, banned)]

# print(words)

# print(character_frequencies(words))

words = load_words()
freq = character_frequencies(words)

while True:
  guess = input("What word did you guess? ")
  for i in range(len(guess)):
      res = input(f"What was the colour of character {guess[i]} (b, y, g)? ")
      if res == 'b':
          banned.add(guess[i])
      if res == 'y':
          present.add(guess[i])
      if res == 'g':
          known[i] = guess[i]

  possible = find_possible(words, known, present, banned)      

  print('known', known)    
  print('present', present)
  print('banned', banned)
  print(f"OK, there are now {len(possible)} possible words:", possible)