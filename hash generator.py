import hashlib
import time

from termcolor import colored, cprint


def wait(amount):
    time.sleep(amount)
    print()


password = ""
algo = ""

print(colored("Welcome to Hasher","cyan"))
cprint("Made By Alex Haug", "green", attrs=['bold', 'underline', 'blink'])
wait(0.5)
print("Please enter the password to hash")
password = input()
print()
print(colored("Please pick the number corresponding to your desired hash algorithm", "magenta"))
wait(1)
print(colored("1. MD-5", "green"))
time.sleep(0.5)
print(colored("2. SHA-1", "green"))
time.sleep(0.5)
print(colored("3. SHA-224", "green"))
time.sleep(0.5)
print(colored("4. SHA-256", "green"))
time.sleep(0.5)
print(colored("5. SHA-384", "green"))
time.sleep(0.5)
print(colored("6. SHA-512", "green"))
wait(1)
print((colored("Please enter that number", "yellow")))
selection = int(input())
print()
if selection == 1:
    hash_object = hashlib.md5(password .encode('utf-8'))
    algo = "MD-5"
elif selection == 2:
    hash_object = hashlib.sha1(password .encode('utf-8'))
    algo = "SHA-1"
elif selection == 3:
    hash_object = hashlib.sha224(password .encode('utf-8'))
    algo = "SHA-224"
elif selection == 4:
    hash_object = hashlib.sha256(password .encode('utf-8'))
    algo = "SHA-256"
elif selection == 5:
    hash_object = hashlib.sha384(password .encode('utf-8'))
    algo = "SHA-384"
elif selection == 6:
    hash_object = hashlib.sha512(password .encode('utf-8'))
    algo = "SHA-512"

hex_dig = hash_object.hexdigest()

print("The " + algo + " hash for " + password + " is ", colored(hex_dig, "red"))
print("Have a Nice Day. Bye.")
