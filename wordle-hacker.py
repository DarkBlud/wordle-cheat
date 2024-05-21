try:
    import platform
    import os
    from datetime import datetime 
    import requests 
    from colorama import init, Fore, Style
except ModuleNotFoundError: 
    sys = platform.system()
    if "mac" not in sys: 
        os.system("pip install requests colorama")
    else: 
        print(Fore.RED + "No module named requests or colorama (install the missing modules then restart the script)")

# Initialize colorama
init(autoreset=True)
sys = platform.system()
if sys == "Linux" : 
    os.system("clear")
elif sys == "Windows":
    os.system("cls")
else:
    os.system("clear")
def checker(date_str):
    try:
        # Try to parse the input string to a datetime object
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
        # Check if the formatted string matches the original string to catch invalid dates like '2020-13-01'
        return parsed_date.strftime("%Y-%m-%d") == date_str
    except ValueError:
        return False

def main(): 
    try:
        url = "https://www.nytimes.com/svc/wordle/v2/"
        print(Fore.CYAN + "Do you want today's answer or a specific date?")
        option = int(input(Fore.GREEN + "(1: today, 2: specific date): "))
        if option == 1:
            date = str(datetime.now().date())
            url += date + ".json"
            try:
                response = requests.get(url).json()
                answer = response['solution']
                print(Fore.MAGENTA + f"Found the answer for today's Wordle: {Fore.GREEN}{answer}")
            except Exception as e:
                print(Fore.RED + f"Error fetching today's Wordle answer: {e}")
        elif option == 2:
            date = input(Fore.CYAN + "Enter the date you want (ex: 2020-09-09): \n")
            if checker(date):
                url = f"https://www.nytimes.com/svc/wordle/v2/{date}.json"
                try:
                    response = requests.get(url).json()
                    if "solution" in response:
                        answer = response['solution']
                        print(Fore.MAGENTA + f"Found the answer for the date you wanted: {Fore.GREEN}{answer}")
                    else:
                        print(Fore.RED + "Couldn't get the answer for that date...")
                except Exception as e:
                    print(Fore.RED + f"Error fetching the Wordle answer for {date}: {e}")
            else:
                print(Fore.RED + "You entered the date in the wrong format.\nExample of what you must enter: year-month-day (2020-09-09)")
        else:
            print(Fore.RED + "Wrong option chosen")
    except KeyError as error : 
        print(f"{Fore.BLUE} This error has been happened : \n {Fore.RED}{error}")

if __name__ == "__main__":
    main()
# made with love by DarkBlud 
# TG : @DarkBlud