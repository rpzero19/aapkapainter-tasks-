

def check_anagrams(s1, s2):
    ''' function to check if two words anagrams '''
    assert len(s1) == len(s2), 'The strings are not of same length'
    ab = list(s1);bc = list(s2)
    countT = [i in bc for i in ab]
    countTf = [i in ab for i in bc]

    if sum(countT) == sum(countTf):
        print(f"The strings '{s1}' and '{s2}' are anagrams.")
    else:
        print(f"The strings  '{s1}' and '{s2}' are not anagrams.")


if __name__ == '__main__':
    check_anagrams('state', 'taste')


