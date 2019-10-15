import random
import string


def RandomString(separator, strlength=20):
    """Generate a string of random characters of length 6
    """
    
    strlength = strlength * 3
    
    # make list of possible characters for the string
    characters = string.ascii_letters + string.digits #+ string.punctuation

    # add some set character types
    rnd_str = random.choice(string.ascii_lowercase)
    rnd_str += random.choice(string.ascii_uppercase)
    rnd_str += random.choice(string.digits)
    rnd_str += random.choice(['£', '$', '%', '&', '*', '@', '#'])
    rnd_str += random.choice(['£', '$', '%', '&', '*', '@', '#'])

    # add random characters to get the correct length string
    for i in range(strlength-len(rnd_str)):
        rnd_str += random.choice(characters)

    # shuffle the characters for the string and convert to a string    
    rnd_lst = list(rnd_str)
    random.SystemRandom().shuffle(rnd_lst)
    rnd_str = ''.join(rnd_lst)

    # if an underscore in string replace as used as separator
    while separator in rnd_str:
        rnd_str = rnd_str.replace(separator, random.choice(characters))
        
    return rnd_str


def build_id(str_length, segments, separator):
    """Create a string with the given length and the number of segments
    """

    id_str = ''
    
    for i in range(segments):
        id_str += RandomString(separator, str_length)[:str_length] + separator

    return id_str[:-1]


def main(length_of_string=10, number_of_segments=1, separator='_'):
    """Generate a random string with a defined length
    
    """
    return build_id(length_of_string, number_of_segments, separator)
