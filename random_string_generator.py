import random
import string


def RandomString(separator, string_length=20, symbols=False):
    """Generate a string of random characters of length 6
    """
    
    strlength = string_length * 3
    possible_symbols = ['$', '%', '&', '*', '@', '#']

    # make list of possible characters for the string
    if symbols is True:
        characters = string.ascii_letters + string.digits
        for sym in possible_symbols:
            characters += sym
    else:
        characters = string.ascii_letters + string.digits

    # add some set character types
    rnd_str = random.choice(string.ascii_lowercase)
    rnd_str += random.choice(string.ascii_uppercase)
    rnd_str += random.choice(string.digits)
    if symbols:
        rnd_str += random.choice(possible_symbols)
        rnd_str += random.choice(possible_symbols)

    # add random characters to get the correct length string
    for i in range(strlength-len(rnd_str)):
        rnd_str += random.choice(characters)

    # shuffle the characters for the string and convert to a string    
    rnd_lst = list(rnd_str)
    random.SystemRandom().shuffle(rnd_lst)
    rnd_str = ''.join(rnd_lst)

    # if defined separator in string replace
    while separator in rnd_str:
        rnd_str = rnd_str.replace(separator, random.choice(characters))
        
    return rnd_str[:string_length] + separator


def build_id(str_length, segments, separator, symbols):
    """Create a string with the given length and the number of segments
    """

    id_str = ''
    
    for i in range(segments):
        id_str += RandomString(separator, str_length, symbols)

    return id_str[:-1]


def main(length_of_string=10, number_of_segments=1, separator='_', symbols=False):
    """Generate a random string with a defined length
    
    """
    return build_id(length_of_string, number_of_segments, separator, symbols)
