import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('dc_productivity')

department_prod = SHEET.worksheet('department_prod')

data = department_prod.get_all_values()
print(data)

def daily_volume_general():
    """
    Asks the user to input the unit volume of delivery colleagues will be expected to process
    """

    print("Please input the expected general merchandise delivery volumes: ")

    general_vol = input("Please enter volumes for general merchandise deliveries for the the week.")
    print(f'{general_vol}')
def daily_volume_beauty():
    """
    Asks the user to input the unit volume of beauty specific delivery to be processed, this 
    follows a different path to general delivery.
    """

    print("Please input the expected beauty product delivery volumes: ")
    beauty_vol = input("Please enter volumes for beauty deliveries for the the week....\n")
    print(f'{beauty_vol}')







def main():
    """
    runs the full program
    """
    print("Welcome to the DC staff schedule assistant...\n")
    print("When entering data please ensure you enter the full 5 days worth seperated by a comma..\n")
    print("Example: 14543, 34322, 23253, 23242, 23232")
    daily_volume_general()
    daily_volume_beauty()


main()