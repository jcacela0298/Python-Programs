"""
Program: cacela_sentences.py
Author: Jack Cacela
Generates and displays sentences using simple grammar 
and vocabulary. Words are chosen at random.
"""

import random

# Vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("TIGER", "DOG", "CAT", "FLAMINGO")
verbs = ("CLIMBED", "PUNCHED", "JUMPED")
prepositions = ("WITH", "BY")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase"""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()