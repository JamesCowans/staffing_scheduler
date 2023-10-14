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


def daily_volume_general():
    """
    Asks the user to input the unit volume of delivery colleagues will be expected to process
    """


    general_vol = input("Please enter volumes for general merchandise deliveries for the the week: ")

    daily_vol_gen = general_vol.split(",")
    validate_data(daily_vol_gen)

def daily_volume_beauty():
    """
    Asks the user to input the unit volume of beauty specific delivery to be processed, this 
    follows a different path to general delivery.
    """

    
    beauty_vol = input("Please enter volumes for beauty deliveries for the the week: ")
 
    daily_vol_bty = beauty_vol.split(",")
    validate_data(daily_vol_bty)


def validate_data(values):
    """
    Inside the try, strings converted to integers and ValueError raised if the incorrect number of data
    is inputted or cannot be converted
    """
    try:
        [int(value) for value in values]
        if len(values) !=5:
            raise ValueError(
        f"The number of values entered must total 5, you entered{values}")
    except ValueError as e:
        print(f"Invalid date: {e}, please try again.\n")




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