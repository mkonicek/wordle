def is_possible(word, allowed, must_appear):
    for i in range(len(word)):
        if word[i] not in allowed[i]:
            return False
    for m in must_appear:
        if m not in word:
            return False
    return True

def find_possible(words, allowed, must_appear):
    return [word for word in words if is_possible(word, allowed, must_appear)]

def try_guess(guess, hidden_word):    
    if len(guess) != len(hidden_word):
        raise "Guess and hidden word must have the same length"
    res = ""
    for i in range(len(guess)):
        if guess[i] == hidden_word[i]:
            res = res + "g"
        elif guess[i] in hidden_word:
            res = res + "y"
        else:
            res = res + "b"
    return res     