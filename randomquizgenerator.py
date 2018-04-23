#!/usr/bin/python3
# Random Quiz Generator
# Create quizzes with questions and answers in random order, answer key too.

import random

# Quiz Data, Keys are Pokemon, Values are their types.

elementType = {'Bulbasaur': 'Grass/Poison', 'Charmander': 'Fire',
               'Squirtle': 'Water', 'Pidgey': 'Normal/Flying', 'Caterpie': 'Bug', 'Pikachu':
               'Electric', 'Abra': 'Psychic', 'Ekans': 'Poison', 'Clefairy': 'Fairy', 'Exeggcutor':
               'Grass/Psychic'}

# Generate 10 Quiz Files
for quizNum in range(10):
    # Create the quiz and answer key files.
    quizFile = open('pokemonquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('pokemonquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write Header for Quiz
    quizFile.write('Name:\n\nDate:\n\nClass:\n\n')
    quizFile.write(('' * 20) + 'Pokemon TYpes Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the pokemon.
    pokemon = list(elementType.keys())
    random.shuffle(pokemon)

    # Loop through all 10 pokemon, make question for each
    for questionNum in range(10):

        # Get right and wrong ansers.
        # Take values from randomized list of the corresponding question
        correctAns = elementType[pokemon[questionNum]]
        # List all the values from the original array
        wrongAns = list(elementType.values())
        # Delete the corresponding correct answer from the list
        del wrongAns[wrongAns.index(correctAns)]
        # Randomize the wrong answers and only take a sample of 3 from the list
        wrongAns = random.sample(wrongAns, 3)
        # Put the correct value and the 3 wrong values together
        answerOptions = wrongAns + [correctAns]
        # Randomize the options so the answer is not always the last one
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. %s is what type?\n' % (questionNum + 1,
                                                   pokemon[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i],
                                             answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAns)
        ]))
    quizFile.close()
    answerKeyFile.close()
