import signs

print("""██╗  ██╗ ██████╗ ██████╗  ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ███████╗
██║  ██║██╔═══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
███████║██║   ██║██████╔╝██║   ██║███████╗██║     ██║   ██║██████╔╝█████╗  
██╔══██║██║   ██║██╔══██╗██║   ██║╚════██║██║     ██║   ██║██╔═══╝ ██╔══╝  
██║  ██║╚██████╔╝██║  ██║╚██████╔╝███████║╚██████╗╚██████╔╝██║     ███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝
                                                                           """)
print("\n\n\n")

sign = ""

def get_sign():
    global sign
    sign = input("Enter you sign to get your horoscope\n\n")
    give_answer(sign)

def give_answer(sign):
    if sign.lower() == "aries":
        quit = input("\n\n" + signs.aries_text + "\n\n")
        if quit == "":
            exit()
        else:
            print("\n\n")
            get_sign()

    elif sign.lower() == "taurus":
        quit = input("\n\n" + signs.taurus_text + "\n\n")
        if quit == "":
            exit()
        else:
            print("\n\n")
            get_sign()

def game():
    get_sign()

game()