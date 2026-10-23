# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Hudson Dobbs
#               Ajay Palanisamy
#               Micah Kadiri
#               Benjamin Hatch
#               Mayu Kotwal
# Section:      508
# Assignment:   Lab Topic 9 (Team)
# Date:         19 October 2026

def print_puzzle(puzzle):
    """ Print puzzle as a long division problem. """
    puzzle = puzzle.split(",")
    for i in range(len(puzzle)):
        if i == 1:
            print(f"{len(puzzle[i].split('|')[1]) * '_': >16}")
        print(f"{puzzle[i]: >16}")
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(puzzle_string):
    """
    Takes in a puzzle string, extracts all alphabetic characters, 
    and returns a string of 10 unique letters in order of appearance.
    """
    valid_letters = ""
    for char in puzzle_string:
        # Check if the character is a letter and not already in our result string
        if char.isalpha() and char not in valid_letters:
            valid_letters += char
            
    return valid_letters
    
def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"
    print()
    print_puzzle(puzzle)

if __name__ == "__main__":
    main()
    
# Part 3: Check whether the equation is correct
def check_user_guess(dividend, quotient, divisor, remainder):
    if dividend == quotient * divisor + remainder:
        return True
    else:
        return False
