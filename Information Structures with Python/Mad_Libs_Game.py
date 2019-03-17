# Mad lib game that prompts a user for a number and prints a statement.

# List that will store Mad libs upon their generation.
mad_lib_list = []

# Main while loop to allow user to play again at end of program.
while True:

    # Create lists of nouns, verbs, and adjectives, and sentences.
    nouns = ['car', 'Plato', 'motorcycle', 'computer', 'Draper']
    verbs = ['walk', 'pass', 'sit', 'call']
    adject = ['cold', 'camouflage', 'windy', 'professional', 'crooked', 'tasteful']
    sents = ["Does anyone know how to {0} on a {1} {2}?", "It's too {1} to {0} a {2}!"]

    # Prompt user to enter an integer, convert to integer if necessary and validate >0.
    while True:
        entry = (input("Please enter a positive integer: "))
        try:
            i = int(entry)
            if i < 1:
                print("That is not a positive integer, please try again.")
                continue
            break
        except ValueError:
            print("That is not an integer")

    # Use the mod function to scale the user input appropriate for each list.
    n = int(entry) % int(nouns.__len__())
    v = int(entry) % int(verbs.__len__())
    a = int(entry) % int(adject.__len__())
    s = int(entry) % int(sents.__len__())

    # Select sentence from 'sents' list from modified user input.
    sentence = sents[s]

    # generate Mad lib
    mad_lib = sentence.format(verbs[v],adject[a],nouns[n])

    # Check if mad lib has been used before. If mad lib is unique, add it to mad_lib_list.
    if mad_lib not in mad_lib_list:
        mad_lib_list += [mad_lib]
    elif mad_lib in mad_lib_list:
        print("Mad lib previously used.")
    # Print list of all mad libs.
    for elem in mad_lib_list:
        print(elem)

    # Ask user if they would like to play again "y" or "n".
    # Quit program if invalid input is entered.
    try_again = (input("Would you like to play again? "))
    print()
    if try_again == 'y':
        continue
    elif try_again == "Y":
        continue
    elif try_again == "yes":
        continue
    elif try_again == "Yes":
        continue
    elif try_again == "n":
        break
    elif try_again == "N":
        break
    elif try_again == "No":
        break
    elif try_again == "no":
        break
    else:
        print("Invalid input, program shut down.")
        break
