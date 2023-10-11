import random
import string


CHAR_SET = "AĂÂBCDEFGHIÎJKLMNOPQRSŞTȚUVWXYZ"
SPACING = " | "


def get_random_char():
    pos = random.randint(0, len(CHAR_SET)-1)
    return CHAR_SET[pos]


def tabula_recta_generator():
    alphabet = list(string.ascii_uppercase)  
    # print header
    print(4*" ",end="")   
    print(" | ".join(alphabet))
    # print password-table
    for row in range(0, len(alphabet)):
        print(alphabet[row],  end=SPACING) 
        print(" | ".join([get_random_char() for _ in range(len(alphabet))])) 


if __name__ == '__main__':
    personal_seed = input("Set your private seed (or leave blank for random): \n")
    if personal_seed:
        random.seed(personal_seed)
    tabula_recta_generator()