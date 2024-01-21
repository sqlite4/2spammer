import requests
import time
from colorama import Fore, Style, init

init(autoreset=True)

def send2Spammer():
    whatIs2Spammer = """
    
    ██████╗░░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
    ╚════██╗██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
    ░░███╔═╝╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
    ██╔══╝░░░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
    ███████╗██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
    ╚══════╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═

    """

    print(Fore.LIGHTMAGENTA_EX + whatIs2Spammer)

def launch2Spammer():

    send2Spammer()

    webhook2url = input("Specify the webhook link: ")

    webhook2name = input("Specify the webhook name: ")

    message = input("Specify the message to send: ")

    send2speed = float(input("Enter the sending speed (in seconds, you might get status 429.): "))

    confirm = input(f"\nDo you confirm? (Type 'Y'.): ").lower()

    if confirm == 'y':
        send2Webhook(webhook2url, webhook2name, message, send2speed)
        print(Fore.GREEN + "Successfully!")
    else:
        print(Fore.YELLOW + "Cancelled.")

def send2Webhook(webhook2url, webhook2name, message, send2speed):
    failed = 0
    cooldownCounter = 0
    cooldownDuration = 10
    defaultSpeed = send2speed

    while True:
        try:
            colored_prefix = f"{Fore.MAGENTA}[{Fore.CYAN}2SPAMMER{Fore.MAGENTA}]{Style.RESET_ALL} "
            payload = {"content": f"{message}", "username": webhook2name}
            response = requests.post(webhook2url, json=payload)

            if response.status_code == 204:
                print(colored_prefix + Fore.GREEN + f"Message sent: {Fore.LIGHTGREEN_EX}{message}{Fore.GREEN} as {Fore.WHITE}{webhook2name}{Fore.GREEN}.")
            else:
                failed += 1
                print(colored_prefix + Fore.RED + f"An error occurred, it may be related to the Discord API: {Fore.WHITE}{response.status_code}")

            if failed % 5 == 0 and failed != 0:
                cooldownCounter = cooldownDuration
                send2speed *= 5
                print(colored_prefix + Fore.RED + f"Cooldown activated. Slowing down for {cooldownDuration} seconds." + Fore.LIGHTMAGENTA_EX + " (Discord API)")
            
            if cooldownCounter > 0:
                time.sleep(5)
                cooldownCounter -= 1
            else:
                time.sleep(defaultSpeed)

        except Exception as e:
            print(colored_prefix + Fore.RED + f"An error occurred: {Fore.WHITE}{e}")

if __name__ == "__main__":
    launch2Spammer()
