# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ajay Palanisamy
# Section:      508
# Assignment:   Lab 9 team
# Date:         23 10 2026

def print_puzzle(puzzle):
    """ Print puzzle as a long division problem. """
    # Print each row with the division lines aligned on the right.
    puzzle = puzzle.split(",")
    for i in range(len(puzzle)):
        if i == 1:
            print(f"{len(puzzle[i].split('|')[1]) * '_': >16}")
        print(f"{puzzle[i]: >16}")
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(S1):
    # Keep each puzzle letter once, skipping spaces and punctuation.
    unique = ""
    for i in S1:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" and i not in unique:
            unique+=i
    return unique

def is_valid_guess(S1,S2):
    # A guess must use all ten puzzle letters exactly once.
    if len(S2) != 10:
        return False
    unique = ""
    for i in S2:
        if i not in S1 or i in unique:
            return False
        unique+=i
    for i in S1:
        if i not in S2:
            return False
    return True

def check_user_guess(i1,i2,i3,i4):
    # Check dividend = quotient * divisor + remainder.
    if i1 == i2*i3+i4:
        return True
    return False

def make_number(S1,S2):
    # Each letter's position in the guess gives its digit.
    number = ""
    for i in S1:
        number += str(S2.index(i))
    return (int(number))

def make_numbers(S1,S2):
    # Extract the dividend, quotient, divisor, and remainder in that order.
    Arr1 = S1.split(',')
    Arr2 = Arr1[1].split('|')
    return (make_number(Arr2[1].strip(),S2),make_number(Arr1[0].strip(),S2),make_number(Arr2[0].strip(),S2),make_number(Arr1[-1].strip(),S2))



def main():
    # Read one puzzle and one guess, then display the result.
    puzzle_String = input("Enter a word arithmetic puzzle: \n")
    print_puzzle(puzzle_String)
    print()
    guess = input("Enter your guess, for example ABCDEFGHIJ: ")
    unique_letters = get_valid_letters(puzzle_String)
    if not is_valid_guess(unique_letters,guess):
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
        return
    tuple1 = make_numbers(puzzle_String,guess)
    if check_user_guess(tuple1[0],tuple1[1],tuple1[2],tuple1[3]):
        print("Good job!")
    else:
        print("Try again!")


if __name__ == "__main__":
    main()
  

