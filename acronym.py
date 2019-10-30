# Program allows the user to type a phrase and then outputs the acronym for that phrase

def acronym(phrase):

    # split the phrase into individual words
    words = phrase.split()

    # initialize acronym as an empty string
    acronym = ""

    # Loop through each word to obtain the first letter
    for word in words:
        acronym += word[0].upper() # gets first letter in each word, capitalizes and assigned to acronym variable

    return acronym

def main():

    print("This program generates acronyms from phrases input\n")

    phrase = input("Enter the desired phrase: ").title()

    print("The acronym for the phrase {0}, is {1}".format(phrase,acronym(phrase)))

main()
    