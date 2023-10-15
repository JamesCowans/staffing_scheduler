import math 
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

decant = SHEET.worksheet('decant')
inbound = SHEET.worksheet('inbound')
picking = SHEET.worksheet('picking')
putaway = SHEET.worksheet('putaway')
xdock = SHEET.worksheet('xdock')

#data = decant.get_all_values()


def daily_volume_general():
    """
    Asks the user to input the unit volume of delivery colleagues will be expected to process
    """
    while True:

        general_vol = input("Please enter volumes for general merchandise deliveries for the the week: ")

        daily_vol_gen = general_vol.split(",")
        validate_data(daily_vol_gen)

        if validate_data(daily_vol_gen):
            print("data is valid for general..")
            break
    return daily_vol_gen


def daily_volume_beauty():
    """
    Asks the user to input the unit volume of beauty specific delivery to be processed, this 
    follows a different path to general delivery.
    """

    while True:

        beauty_vol = input("Please enter volumes for beauty deliveries for the the week: ")
    
        daily_vol_bty = beauty_vol.split(",")
        validate_data(daily_vol_bty)

        if validate_data(daily_vol_bty):
            print("data is valid for beauty...")
            break
    return daily_vol_bty



def validate_data(values):
    """
    Inside the try, strings converted to integers and ValueError raised if the incorrect number of data
    is inputted or cannot be converted
    """
    try:
        [int(value) for value in values]
        if len(values) !=5:
            raise ValueError( f"The number of values entered must total 5, you entered{values}")
    except ValueError as e:
        print(f"Invalid date: {e}, please try again.\n")
        return False

    return True





def update_volumes_worksheet_general(data_g):
    """
    Adds the delivery volume to the general merchandise spreadsheet
    """
    print("Updating General Merchandise spreadsheet...\n")
    delivery_volumes_general_worksheet = SHEET.worksheet('delivery_volumes_general')
    delivery_volumes_general_worksheet.append_row(data_g)
    print("General Merchandise spreadsheet updated sucessfully...\n")

    
def update_volumes_worksheet_beauty(data_b):
    """
    Adds the delivery volume to the beauty products spreadsheet
    """
    print("Updating Beauty products spreadsheet...\n")
    delivery_volumes_beauty_worksheet = SHEET.worksheet('delivery_volumes_beauty')
    delivery_volumes_beauty_worksheet.append_row(data_b)
    print("Beauty products spreadsheet updated sucessfully...\n")

def calculate_staff_requirements_decant(data_g):
    """
    Calculates the staffing requirements of the decant department,
    all colleagues have a productivity target set within the decant spreadsheet by day
    and all work 8 hours per day.
    """
    

    decant = SHEET.worksheet("decant").get_all_values()
    decant_row = decant[-1]
   

    gen_requirements = []
    for volume, staffing in zip(data_g, decant_row):
        req_hours = int(volume) // int(staffing)
        req = (req_hours) // 8 
        gen_requirements.append(req)
    print(gen_requirements)

def calculate_staff_requirements_inbound(data_g):
    """
    Calculates the staffing requirements of the decant department,
    all colleagues have a productivity target set within the decant spreadsheet by day
    and all work 8 hours per day.
    """
    

    inbound = SHEET.worksheet("inbound").get_all_values()
    inbound_row = inbound[-1]
   

    gen_requirements = []
    for volume, staffing in zip(data_g, inbound_row):
        req_hours = int(volume) // int(staffing)
        req = (req_hours) // 8 
        gen_requirements.append(req)
    print(gen_requirements)

def calculate_staff_requirements_picking(data_g):
    """
    Calculates the staffing requirements of the decant department,
    all colleagues have a productivity target set within the decant spreadsheet by day
    and all work 8 hours per day.
    """
    

    picking = SHEET.worksheet("picking").get_all_values()
    picking_row = picking[-1]
  

    gen_requirements = []
    for volume, staffing in zip(data_g, picking_row):
        req_hours = int(volume) // int(staffing)
        req = (req_hours) // 8 
        gen_requirements.append(req)
    print(gen_requirements)

def calculate_staff_requirements_putaway(data_g):
    """
    Calculates the staffing requirements of the decant department,
    all colleagues have a productivity target set within the decant spreadsheet by day
    and all work 8 hours per day.
    """
    

    putaway = SHEET.worksheet("putaway").get_all_values()
    putaway_row = putaway[-1]
  
    #data_g_percentage = int(data_g) // 130
    gen_requirements = []
    for volume, staffing in zip(data_g, putaway_row):
        req_hours = int(volume) // int(staffing)
        req = (req_hours) // 8 
        gen_requirements.append(req)
    print(gen_requirements)


def calculate_staff_requirements_beauty(data_b):
    """
    Calculates the staffing requirements of the decant department,
    all colleagues have a productivity target set within the decant spreadsheet by day
    and all work 8 hours per day.
    """
    xdock = SHEET.worksheet("xdock").get_all_values()
    xdock_row = xdock[-1]
  
    staff_beauty = []
    for volume, staffing in zip(data_b, xdock_row):
        req_hours = int(volume) // int(staffing)
        req = (req_hours) // 8 
        staff_beauty.append(req)
    return staff_beauty

def update_volumes_worksheet_beauty_staff(staff_beauty):
    """
    Adds the delivery volume to the beauty products spreadsheet
    """
    print("Updating Beauty products spreadsheet...\n")
    staff_beauty_worksheet = SHEET.worksheet('staff_beauty')
    staff_beauty_worksheet.append_row(staff_beauty)
    print("Beauty products spreadsheet updated sucessfully...\n")



def main():
    """
    runs the full program
    """
    
    data_b = daily_volume_beauty()
   # data_g = daily_volume_general()
    update_volumes_worksheet_beauty(data_b)
    #update_volumes_worksheet_general(data_g)
    #decant_staff_req = calculate_staff_requirements_decant(data_g)
    #inbound_staff_req = calculate_staff_requirements_inbound(data_g)
    #picking_staff_req = calculate_staff_requirements_picking(data_g)
   # putaway_staff_req = calculate_staff_requirements_putaway(data_g)
    staff_beauty = calculate_staff_requirements_beauty(data_b)
    update_volumes_worksheet_beauty_staff(staff_beauty)
    
    
    
    
print("Welcome to the DC staff schedule assistant...\n")
print("Data will only be acccepted if it is doe full 5 seperated by a comma..\n")
print("Example: 14543, 34322, 23253, 23242, 23232")
    

main()