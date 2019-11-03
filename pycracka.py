import hashlib
from termcolor import colored, cprint
from sys import argv
from time import time
from itertools import product
from string import ascii_lowercase, ascii_uppercase, digits


# character set function
def get_charset(arg_charset):
    charset = ""
    charsets = {"L": ascii_lowercase,
                "U": ascii_uppercase,
                "D": digits}

    for key in arg_charset:
        # Supply charset argument as list or str if imported
        # Only str accepted from command line prompt.
        charset += charsets[key]
    return charset


# hash algorithm possibilities function
def get_algorithm(arg_algo):
    algorithms = {"md5": hashlib.md5,
                  "sha1": hashlib.sha1,
                  "sha224": hashlib.sha224,
                  "sha256": hashlib.sha256,
                  "sha384": hashlib.sha384,
                  "sha512": hashlib.sha512,
                  "sha3_224": hashlib.sha3_224,
                  "sha3_256": hashlib.sha3_256,
                  "sha3_384": hashlib.sha3_384,
                  "sha3_512": hashlib.sha3_512}
    return algorithms[arg_algo]


# timer function
def timer(func):
    def wrapper(*args, **kwargs):
        timer_start = time()
        timer_return = func(*args, **kwargs)
        timer_diff = int(time() - timer_start)

        # print end of bruteforce
        cprint("BRUTEFORCE DONE", "cyan", attrs=['underline'])
        print()
        print(colored("Statistics", "red"))
        print(colored("_________________________________________", "cyan"))
        # print calc time
        cprint("Calculation time: ", "white", end="")
        cprint(timer_diff, "yellow", end="")
        cprint(" seconds", "white")
        print(colored("_________________________________________", "cyan"))

        return timer_return

    return wrapper


# nested for loop that iterates through permutations
@timer
def bruteforce(hash_, charset, min_length, max_length, algo, debug):
    for length in range(int(min_length), int(max_length) + 1):
        for attempt in product(charset, repeat=length):
            hashed = "".join(attempt).encode("utf-8")
            # Calling this hashed because otherwise statistics would
            # show  - found b"<<original>>" - which is ugly
            hashed = algo(hashed).hexdigest()

            if hashed != hash_:
                if debug:
                    print(colored({''.join(attempt)}, "magenta"))
            else:
                if debug:
                    print(colored({''.join(attempt)}, "green"))
                return "".join(attempt)


# define main function variables
def main():
    hash__, charset_, min_length_, max_length_, algo_, debug_ = argv[1:7]
    charset = get_charset(charset_)
    algo = get_algorithm(algo_)
    res = bruteforce(hash__, charset, min_length_, max_length_, algo, debug_)
    # if no matches found
    if res is None:
        print(colored("No matches found.", "green"))
    print(colored('none', "red"))


if __name__ == "__main__":
    print("\n" * 90)
    main()
