#!/usr/bin/python
#Developed by Tiago Neves
#Github: https://github.com/TiagoANeves
#Version: 1.0
#All rights reserved

#Import necessary modules
import crypt
import sys
import os
from argparse import ArgumentParser

os.system("clear")

#Font format
class ff:
    END = '\033[0m'
    BOLD = '\033[1m'
    THIN = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'


    def bold(text):
        return ff.BOLD + str(text) + ff.END


    def thin(text):
        return ff.THIN + str(text) + ff.END


    def italic(text):
        return ff.ITALIC + str(text) + ff.END


    def underline(text):
        return ff.UNDERLINE + str(text) + ff.END


    def red(text):
        return ff.RED + str(text) + ff.END


    def green(text):
        return ff.GREEN + str(text) + ff.END


    def yellow(text):
        return ff.YELLOW + str(text) + ff.END


    def blue(text):
        return ff.BLUE + str(text) + ff.END


    def purple(text):
        return ff.PURPLE + str(text) + ff.END


#Create Banner
def banner():
    print("""
    %s
      _____   ____    _____   _       _                          ____   __        __  ____
     |_   _| |  _ \  |_   _| | |     (_)  _ __    _   _  __  __ |  _ \  \ \      / / |  _ \\
       | |   | | | |   | |   | |     | | | '_ \  | | | | \ \/ / | |_) |  \ \ /\ / /  | | | |
       | |   | |_| |   | |   | |___  | | | | | | | |_| |  >  <  |  __/    \ V  V /   | |_| |
       |_|   |____/    |_|   |_____| |_| |_| |_|  \__,_| /_/\_\ |_|        \_/\_/    |____/
    %s
    %s
     # Coded By Tiago Neves
     # Github https://github.com/TiagoANeves
    %s
    """ % (ff.BLUE, ff.END, ff.RED, ff.END))


# Main function
if __name__ == "__main__":
    try:
        banner()
        print("This program will check the users in the shadow file and use a wordlist to try crack the password hashes.")
        print("If wordlist not especified, it will use the wordlist.txt by default.")
        print()
        parser = ArgumentParser()
        parser.add_argument("-s", "--shadow", help="shadow file")
        parser.add_argument("-w", "--wordlist", default="wordlist.txt", help="wordlist file")
        args = parser.parse_args()
    except:
        sys.exit()

    if len(sys.argv) < 3:
        print(ff.yellow("Usage: python "+sys.argv[0]+" -s shadown -w wordlist.txt"))
        print(ff.yellow("Use "+sys.argv[0]+" -h or --help to print the help option"))
        sys.exit()

    try:
        fileshadow = open(args.shadow, 'r', encoding='latin-1')
    except:
        print(ff.red("Error trying to open shadow file"))
        sys.exit()

    users = list(filter(lambda user: '$' in user, fileshadow.read().split('\n')))
    usertotal = len(users)
    usercount = 0
    print(ff.purple("The shadow file has ") + ff.blue(len(users)) + ff.purple(" users"))

    try:
        filewordlist = open(args.wordlist, 'r', encoding='latin-1')
    except:
        print(ff.red("Error trying to open wordlist file"))
        sys.exit()

    passwords = list(filter(lambda password: password, filewordlist.read().split('\n')))
    passwordtotal = len(passwords)
    passwordcount = 0
    print(ff.purple("The wordlist file has ") + ff.blue(len(passwords)) + ff.purple(" passwords"))

    for user in users:
        usercount += 1
        userprogress = " " + ff.blue("(" + str(usercount) + "/" + str(usertotal) + ")") + " "
        fields = user.split(":")
        username = fields[0]
        hash = fields[1]
        hashes = hash.split("$")
        salt = "$" + hashes[1] + "$" + hashes[2]
        found = False

        print(ff.yellow("Cracking user") + userprogress + ff.bold(ff.green(username)))

        for password in passwords:
            passwordcount += 1
            passwordprogress = " " + ff.blue("(" + str(passwordcount) + "/" + str(passwordtotal) + ")") + " "
            print(ff.yellow("Trying password") + passwordprogress + ff.bold(ff.green(password)))
            sys.stdout.write("\033[F\033[K") # clear previous line

            try:
                result = crypt.crypt(password, salt)

                if result == hash:
                    found = True
                    break

            except KeyboardInterrupt:
                break


        if found:
            print(ff.yellow("Password cracked:") + " " + ff.bold(ff.green(password)))
        else:
            print(ff.red("Could not crack the password"))
