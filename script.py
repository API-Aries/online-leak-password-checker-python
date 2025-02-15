import requests
from colorama import Fore, Style, init
from datetime import datetime


init()


def check_password(password, api_token):
    url = f'https://api.api-aries.com/v1/checkers/pwned-password/?password={password}'
    headers = {'APITOKEN': api_token}
    response = requests.get(url, headers=headers)
    return response.json()


def read_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    return [password.strip() for password in passwords]


def write_results(file_path, results):
    with open(file_path, 'w') as file:
        for result in results:
            file.write(result + '\n')


def main(password_file_path, api_token, output_file_path):
    passwords = read_passwords(password_file_path)
    results = []
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    for password in passwords:
        result = check_password(password, api_token)
        if 'found' in result and result['found']:
            output = f"Password: {password} - Found: {result['found']} - Used Times: {result['used_times']}"
            print(f"{Fore.RED}{output}{Style.RESET_ALL}")
        elif 'error' in result:
            output = f"Password: {password} - Error: {result['error']}"
            print(f"{Fore.YELLOW}{output}{Style.RESET_ALL}")
        else:
            output = f"Password: {password} - Not found in database"
            print(f"{Fore.GREEN}{output}{Style.RESET_ALL}")
        results.append(f"{current_date} - {output}")
    
    write_results(output_file_path, results)

if __name__ == "__main__":
    password_file_path = 'passwords.txt' #check password list
    api_token = '111-111-111-111' # API Token here ##### find here: https://panel.api-aries.com/
    output_file_path = 'checked.txt' # output file name
    main(password_file_path, api_token, output_file_path)
