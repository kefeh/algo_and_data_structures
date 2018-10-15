def getPosition(letter):
    """This function takes a letter as input and return its postion
    It checks if the letter is lowercase, it returns its position with respect to lowercase a
    else with respect to uppercase a. 
    it uses the python ord() function which takes a character as input and returns an interger: its ascii value"""
    if (ord(letter) not in range(ord('A'), ord('Z')+1)) and (ord(letter) not in range(ord('a'), ord('z')+1)):
         #making sure that any other input not a letter raises a an error
        raise Exception('Your Input: {} is not a letter'.format(letter))
    else:
        if ord(letter) >= ord('a'):
            first = ord('a') - 1
        else:
            first = ord('A') - 1
        position = ord(letter) - first
        return position
def printPoints(number):
    """This function takes a number and prints '·' number times"""
    for i in range(number):
        print('·', end='')

def printLetter(letter, distance):
    """This function takes a letter and a  distance and prints a computed letter without going to a new line"""
    printedLetter = chr(ord(letter) - distance)
    print(printedLetter, end='')

def getMidDist(number):
    """This function takes a number and return the odd number at that position"""
    return (number-1)*2 + 1

def diamond(letter):
    """This function takes a letter as an input and prints out a diamond shape
        Requirements
        The first row contains one 'A'.
        The last row contains one 'A'.
        All rows, except the first and last, have exactly two identical letters.
        All rows have as many trailing spaces as leading spaces. (This might be 0).
        The diamond is horizontally symmetric.
        The diamond is vertically symmetric.
        The diamond has a square shape (width equals height).
        The letters form a diamond shape.
        The top half has the letters in ascending order.
        The bottom half has the letters in descending order.
        The four corners (containing the spaces) are triangles.
        Examples
        In the following examples, spaces are indicated by · characters.
        Diamond for letter 'A':
        A
        Diamond for letter 'C':
        ··A··
        ·B·B·
        C···C
        ·B·B·
        ··A··
        Diamond for letter 'E':
        ····A····
        ···B·B···
        ··C···C··
        ·D·····D·
        E·······E
        ·D·····D·
        ··C···C··"""

    position = getPosition(letter) #position is the position of the letter in the ascii table
    i = 1
    check = False #asserts if i(the iterator) has reached the value of position. "This helps in printing the other half of the diamond"
    while i:
        preDistance = (position) - i #preDistance is used to print the dots in fron and behind the characters
        distance = getMidDist(i-1) #distance is used to print the dots between the characters
        if i == 1:
            printPoints(preDistance)
            printLetter(letter, position-1)
            printPoints(preDistance)
            print()
        else:
            printPoints(preDistance)
            printLetter(letter, preDistance)
            printPoints(distance)
            printLetter(letter, preDistance)
            printPoints(preDistance)
            print()
        if i == position:
            check = True
        if check:
            i -= 1
        else:
            i += 1


def main():
    letter = input("Enter Letter: ")
    diamond(letter)

if __name__ == "__main__":
    main()