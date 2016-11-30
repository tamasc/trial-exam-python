# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

def count_a(filename):
    sum_of_a = 0
    try:
        fr = open(filename, 'r')
    except NameError:
        return sum_of_a
    for line in fr:
        for character in line:
            if character == 'a':
                sum_of_a += 1
    fr.close()
    return sum_of_a
