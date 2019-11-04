import pycracka
import time
from termcolor import colored, cprint

# wait function
def wait(amount):
    time.sleep(amount)
    print()

#definitions
hash_ = ""
charset = ""
char_know = ""
chars = ""
min_length = ""
max_length = ""
combos = ""

#startup
print(colored("Welcome to Pycracka", "blue", attrs=['bold', 'underline', 'blink']))
cprint("")
print(colored("v1.0", "blue", attrs=['bold', 'underline', 'blink']))
cprint('https://github.com/SinisterGeico/Pycracka')
cprint("")
cprint("Made By Alex Haug", "yellow", attrs=['bold', 'underline', 'blink'])
cprint('')
cprint("Press Enter to begin", "red")
input()

# Hash input
cprint("Please Enter Your Hash", "cyan")
hash_ = input()
wait(0.5)

# Password character combination input
cprint("Do you know what characters the password contains", "cyan")
char_know = input()
if char_know == "yes" or char_know == "yeah" or char_know == "Yes" or char_know == "yup" or char_know == "yes papa" or char_know == "da":
    cprint("What Characters does it contain?")
    cprint("If only uppercase, type U.", "red")
    cprint("If only lowercase, type L", "green")
    cprint("If Only Digits, type D", "magenta")
    cprint("If it contains two types of characters, type their letters", "yellow")
    cprint("If Uppercase, Lowercase, and Digits, type All", "blue")
    chars = input()
    # only lowercase
    if chars == "L" or chars == "l":
        charset = pycracka.get_charset("L")
    # only uppercase
    elif chars == "U" or chars == "u":
        charset = pycracka.get_charset("U")
    # only digits
    elif chars == "D" or chars == "d":
        charset = pycracka.get_charset("D")
    # uppercase and lowercase
    elif chars == "LU" or chars == "lu" or chars == "UL" or chars == "ul":
        charset = pycracka.get_charset("LU")
    # uppercase and digits
    elif chars == "UD" or chars == "ud" or chars == "DU" or chars == "du":
        charset = pycracka.get_charset("DU")
    # lowercase and digits
    elif chars == "LD" or chars == "ld" or chars == "DL" or chars == "dl":
        charset = pycracka.get_charset("LD")
    # lowercase, uppercase, and digits
    elif chars == "LUD" or chars == "all" or chars == "All":
        charset = pycracka.get_charset("LUD")
    # if person doesn't know, assume all
else:
    charset = pycracka.get_charset("LUD")

# minimum length input
cprint("What is the Minimum length of the password?", "magenta")
min_length = int(input("-"))

# maximum length input
cprint("What is the Maximum length of the password?", "magenta")
max_length = int(input("-"))
wait(0.5)

# hash type selector
# prints hash types
print(colored("Please pick the number corresponding to your hash type", "blue"))
wait(0.5)
print(colored("1. MD-5", "green"))
time.sleep(0.25)
print(colored("2. SHA-1", "green"))
time.sleep(0.25)
print(colored("3. SHA-224", "green"))
time.sleep(0.25)
print(colored("4. SHA-256", "green"))
time.sleep(0.25)
print(colored("5. SHA-384", "green"))
time.sleep(0.25)
print(colored("6. SHA-512", "green"))
wait(0.5)
# Selector for hash types
print((colored("Please enter that number", "yellow")))
selection = int(input())
print()
if selection == 1:
    algo = pycracka.get_algorithm("md5")
elif selection == 2:
    algo = pycracka.get_algorithm("sha1")
elif selection == 3:
    algo = pycracka.get_algorithm("sha224")
elif selection == 4:
    algo = pycracka.get_algorithm("sha256")
elif selection == 5:
    algo = pycracka.get_algorithm("sha384")
elif selection == 6:
    algo = pycracka.get_algorithm("sha512")

#show attempts mode on or off
cprint("Do you want to show all attempts? It will make the program about 20x slower.", "red")
combos = input()
if combos == "yes" or combos == "Yes" or combos == "YES" or combos == "ye" or combos == "Ye" or combos == "ya" or combos == "Ya":
    r = pycracka.bruteforce(hash_, charset, min_length, max_length, algo, True)
else:
    r = pycracka.bruteforce(hash_, charset, min_length, max_length, algo, False)
cprint("Calculating. Please wait.", "green")
# cannot find hash
if r is None:
    print("No matches.")
# finds hash
else:
    print("Hash: ", colored(hash_, "grey"))
    print("Match:", "white", colored(r, "yellow", attrs=["bold"]))
print("")
cprint("Thanks For Using", "green", attrs=["bold"])
