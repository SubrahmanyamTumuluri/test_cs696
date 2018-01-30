"""
Exercise 1
Place this script inside a new folder in your github repository called "Exercises".
This will be the directory for all of your in-class exercises this semester.

By the end of class on Thursday 1/25, students should have:
    - Created a private github repo for this class
    - Added their information to this sheet:
        https://docs.google.com/spreadsheets/d/1EKNYOqTnxelmBT4jqotRbUer5eVvWYM9RloN5doScyo/edit?usp=sharing
    - Added my github account (kylelevi) as a collaborator for their private repository
    - Completed these definitions and pushed this script to a folder called "Exercises" in their repo

"""

def hello():
    """
    Prints "Hello World"
    :return: None
    """
    print('hello World')
    return
hello()

def percent_decimal(i):

    """
    Converts a percentage to a decimal or a decimal to a percentage depending on the input i
    :param i: a float between 0 and 100
    :return: a float between 0 and 100
    """
    i = float(input("Enter a number"))
    if i > 1:
        print('the percentage form is', i / 100)
    else:
        print('The value in percentage form is ', i * 100)
    return
percent_decimal(0.1)

def exponent(integer, power):
    """
    Using a loop (no imports!), raise the integer given to the power provided. (integer^power)
    :param integer: a positive, non zero, integer
    :param power: a positive, non zero, integer
    :return: an integer
    """
    #base = int(input('Enter base'))
    #exponent = int(input('enter exponent'))
    product = 1
    # Multiply base exponent times
    for i in range(power):
        product = product * integer
    print(integer, 'to the power of', power, 'is', product)
    return
exponent(2,5)

def complement(dna):
    """
    Returns the complement strand of DNA to the input.  C <--> G,  A <--> T
    :param dna: String containing only C, T, A, and G
    :return: String containing only C, T, A, and G
    """
    temp = ''
    for alp in dna:
        if alp == 'A':
            temp = temp + 'T';
        elif alp == 'T':
            temp = temp + 'A';
        elif alp == 'C':
            temp = temp + 'G';
        elif alp == 'G':
            temp = temp + 'C';
    print(temp)

complement('ABCD')