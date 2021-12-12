import time
import requests


def print_info_cyber():

        print("\033[92m|$$$$$$$|  |$$____     ______ ____    ______    ____| $$")
        print("|$$__|$$|  |$$    \   |      \    \   |     \   /      $$")
        print("|$$   $$|  |$$$$$$$\  |$$$$$$\$$$$\   |$$$$$$\  | $$$$$$$")
        print("|$$$$$$$|  |$$  | $$  |$$ | $$$ |$$|  |$$    $\ | $$  | $$")
        print("|$$|  |$$| |$$  | $$  |$$ | $$$ |$$|  |$$$$$$$$ | $$__| $$")
        print("|$$|  |$$| |$$  | $$  |$$ | $$$ |$$|  |$$       |$$$    $$")
        print("|$$|  |$$| |$$  | $$  |$$ | $$$ |$$|  |$$$$$$$  |$$$$$$$$$")

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~ Version 1.0 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("            _                                          _ _")
        print("           | |                                        (_) |")
        print("  ___ _   _| |__   ___ _ __   ___  ___  ___ _   _ _ __ _| |_ _   _")
        print(" / __| | | | '_ \ / _ \ '__| / __|/ _ \/ __| | | | '__| | __| | | |")
        print("| (__| |_| | |_) |  __/ |    \__ \  __/ (__| |_| | |  | | |_| |_| |")
        print(" \___|\__, |_.__/ \___|_|    |___/\___|\___|\__,_|_|  |_|\__|\__, |")
        print("       __/ |                                                  __/ |")
        print("      |___/                                                   |___/")
        print("\nDeveloper information\n"
              "^^^^^^^^^^^^^^^^^^^^^\n"
              "Ethical hacking Test lab Web Site\n"
              "Bug Bounty lab\n"
              "I am a programmer in python and javaScript\n"
              "\nBit\n"
              "\n If they say it is impossible.\n Remember,\n it's impossible for them, not for you,\n some people will never clap for you,\n but you have to win... \n good luck\n")


def UserName_info():
        username = input('Enter account User Name info: ')

        print('\nLoding info account snapchat...\n' + username)

        snapchat = requests.get(f'https://story.snapchat.com/add/{username}')
        if snapchat.status_code == 200:
            print('OK FOUND! account snapchat\n', requests.URLRequired(f'https://story.snapchat.com/add/{username}'))
        elif snapchat.status_code == 404:
            print('Not FOUND account snapchat\n' + username)
        elif snapchat.status_code == 429:
            print('error Domain web server No sarceh account\n' + username)
        print(snapchat)

        print('Loding info account instagram...\n' + username)

        instagram = requests.get(f'https://www.instagram.com/{username}')
        if instagram.status_code == 200:
            print('OK FOUND! account instagram\n', requests.URLRequired(f'https://www.instagram.com/{username}'))
        elif instagram.status_code == 404:
            print('Not FOUND account instagram\n' + username)
        elif instagram.status_code == 429:
            print('error Domain web server No sarceh account\n' + username)
        print(instagram)

        print('Loding info account facebook...\n' + username)

        facebook = requests.get(f'https://www.facebook.com/{username}')
        if facebook.status_code == 200:
            print('OK FOUND! account facebook\n', requests.URLRequired(f'https://www.facebook.com/{username}'))
        elif facebook.status_code == 404:
            print('Not FOUND account facebook\n' + username)
        elif instagram.status_code == 429:
            print('error Domain web server No sarceh account\n' + username)
        print(facebook)

        print('Loding info account twitter...\n' + username)

        twitter = requests.get(f'https://www.twitter.com/{username}')
        if twitter.status_code == 200:
            print('OK FOUND! account twitter\n', requests.URLRequired(f'https://www.twitter.com/{username}'))
        elif twitter.status_code == 404:
            print('Not FOUND account twitter\n' + username)
        elif instagram.status_code == 429:
            print('error Domain web server No sarceh account\n' + username)
        print(twitter)

        print('Loding info account tiktok...\n' + username)

        tiktok = requests.get(f'https://www.tiktok.com/@{username}')
        if tiktok.status_code == 200:
            print('OK FOUND! account tiktok\n', requests.URLRequired(f'https://www.tiktok.com/@{username}'))
        elif tiktok.status_code == 404:
            print('Not FOUND account tiktok\n' + username)
        elif instagram.status_code == 404:
            print('error Domain web server No sarceh account\n' + username)
        print(tiktok)

        print('Loding info account youtube...\n' + username)

        youtube = requests.get(f'https://www.youtube.com/{username}')
        if youtube.status_code == 200:
            print('OK FOUND! account youtube\n', requests.URLRequired(f'https://www.youtube.com/{username}'))
        elif youtube.status_code == 404:
            print('Not FOUND account youtube\n' + username)
        elif youtube.status_code == 404:
            print('error Domain web server No sarceh account\n' + username)
        print(youtube)

