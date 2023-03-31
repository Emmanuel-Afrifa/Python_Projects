# This code validates whether two words are anagrams (i.e. one can be rearranged to form the other)

def validator(word1,word2):
    """ This function checks whether the two arguments provided are anagrams.
        If the two words are anagrams, the function returns a True value otherwise False.
    """
    word1.lower()
    word2.lower()

    return sorted(word1) == sorted(word1)
    
if __name__ == "__main__":
    w1 = "cinema"
    w2 = "iceman"
    print(validator(w1,w2))
    print(validator("cool", "loco"))
    print(validator("men", "women"))