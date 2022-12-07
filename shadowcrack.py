
import crypt
import sys
import os
from argparse import ArgumentParser

class ff:
    END = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"


    def bold(text):
        return ff.BOLD + str(text) + ff.END


    def red(text):
        return ff.RED + str(text) + ff.END


    def green(text):
        return ff.GREEN + str(text) + ff.END


    def yellow(text):
        return ff.YELLOW + str(text) + ff.END


    def blue(text):
        return ff.BLUE + str(text) + ff.END


    def clear():
        sys.stdout.write("\033[F\033[K")


if __name__ == "__main__":
    try:
        parser = ArgumentParser()
        parser.add_argument("-s", "--shadow", default="shadow.txt", help="Shadow file")
        parser.add_argument("-w", "--wordlist", default="wordlist.txt", help="Wordlist file")
        parser.add_argument("-e", "--encoding", default="latin-1", help="File encoding")
        args = parser.parse_args()
    except:
        sys.exit()

    print(ff.blue("Reading users..."))

    try:
        fileshadow = open(args.shadow, "r", encoding=args.encoding)
    except:
        print(ff.red("Error trying to open shadow file"))
        sys.exit()

    users = list(filter(lambda user: "$" in user, fileshadow.read().split("\n")))
    usertotal = len(users)
    usercount = 0

    ff.clear()

    print(ff.blue("Reading passwords..."))

    try:
        filewordlist = open(args.wordlist, "r", encoding=args.encoding)
    except:
        print(ff.red("Error trying to open wordlist file"))
        sys.exit()

    passwords = list(filter(lambda password: password, filewordlist.read().split("\n")))
    passwordtotal = len(passwords)
    passwordcount = 0

    ff.clear()

    for user in users:
        usercount += 1
        userprogress = ff.yellow("(" + str(usercount) + "/" + str(usertotal) + ")") + " "
        fields = user.split(":")
        username = fields[0]
        hash = fields[1]
        hashes = hash.split("$")
        salt = "$" + hashes[1] + "$" + hashes[2]
        found = False

        print(ff.blue("Cracking user: ") + userprogress + ff.bold(ff.green(username)))

        for password in passwords:
            passwordcount += 1
            passwordprogress = ff.yellow("(" + str(passwordcount) + "/" + str(passwordtotal) + ")") + " "
            print(ff.blue("Trying password: ") + passwordprogress + ff.bold(ff.green(password)))
            ff.clear()

            try:
                result = crypt.crypt(password, salt)
            except KeyboardInterrupt:
                break

            if result == hash:
                found = True
                break

        if found:
            print(ff.blue("Password cracked: ") + ff.bold(ff.green(password)))
        else:
            print(ff.red("Could not crack the password"))
