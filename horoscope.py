import os
import sys
import get_sign_text

# Just some cool text
print("""██╗  ██╗ ██████╗ ██████╗  ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ███████╗
██║  ██║██╔═══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
███████║██║   ██║██████╔╝██║   ██║███████╗██║     ██║   ██║██████╔╝█████╗  
██╔══██║██║   ██║██╔══██╗██║   ██║╚════██║██║     ██║   ██║██╔═══╝ ██╔══╝  
██║  ██║╚██████╔╝██║  ██║╚██████╔╝███████║╚██████╗╚██████╔╝██║     ███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝
                                                                           """)
print("\n\n\n")

# A list of all the signs
SIGNS = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra",
         "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]

# This function is used to get the user's sign
def get_sign():
    sign = input("Enter your sign to get your horoscope:\n\n")
    give_answer(sign)

# This function is used if the user wants to check another sign
def get_another_sign():
    sign = input("Enter another sign or press enter to exit.\n\n")
    give_answer(sign)

# This function gets called when there is a mis spelling in the user's input
def wrong_input():
    sign = input("Please check the spelling and try again.\n\n")
    give_answer(sign)


def give_answer(sign):
    # This gets the number (key) associated with the user's sign (value) inside the file "signs.json" which contains a dictionary
    num = get_sign_text.find_num(sign)
    try:
        # This will clear the terminal, just so it looks nicer
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal before printing answer
        if sign in SIGNS:
            print("\n\n" + get_sign_text.get_text(num) + "\n\n") # If the input matches one of the elements inside SIGNS, it uses the function "get_text()" from the file get_sign_text and then it prints out the result.
            get_another_sign()
        elif sign == "":
            exit() # If the input is empty, just pressing enter, the program will close
        else:
            wrong_input() # If the input does not match any of the elements inside SIGNS
    except:
        pass
        


def game():
    get_sign()

if __name__ == "__main__":
    game()