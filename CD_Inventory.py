#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# AMorgan, 2022-Dec-04, edited file to finish assignment 08
#------------------------------------------#

import pickle

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        None

    """
    def __init__(self, cd_id, cd_title, cd_artist):
        self.cd_id = cd_id
        self.cd_title = cd_title
        self.cd_artist = cd_artist
        self.dicRow = {'ID': cd_id, 'Title': cd_title, 'Artist': cd_artist}


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        load_inventory(file_name, lst_Inventory): -> (a list of CD objects)
        save_inventory(file_name, lst_Inventory): -> None

    """
    # TODone Add code to process data from a file
    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from binary data file identified by file_name into a 2D table

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        """
        lst_Inventory.clear()  # this clears existing data and allows to load data from file
        try:
            with open(file_name, 'rb') as fileObj:
                lst_Inventory = pickle.load(fileObj)
            return lst_Inventory
        except FileNotFoundError as e:
            print('File does not exist!')
            print(e)
            lst_Inventory = []
            return lst_Inventory
        except Exception as e:
            print('There was a general error!')
            print(e)
            lst_Inventory = []
            return lst_Inventory
      # TODone Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
       """Function to write the CD inventory data in memory to a binary data file, replacing what is already in the file.

       Writes the data from the list of dicts table in memory into a binary data file.

       Args:
           file_name (string): name of file to write the data to
           lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime

       Returns:
           None.
       """
       with open(file_name, 'wb') as fileObj:
           pickle.dump(lst_Inventory, fileObj)
    

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """Handling Input / Output
    
    properties:

    methods:
        print_menu(): -> None
        menu_choice(): -> choice
        show_inventory(table): -> None
        add_inventory_menu(): -> cdObject

    
    """
    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        try:
           print('======= The Current Inventory: =======')
           print('ID\tCD Title (by: Artist)\n')
           for row in table:
               print('{}\t{} (by:{})'.format(*row.values()))
           print('======================================')
        except:
            print("No data to display")
    # TODone add code to get CD data from user
    @staticmethod
    def add_inventory_menu():
        """Gets user inputs to add a CD to the inventory table


        Args:
            None.

        Returns:
            cdObject: an object from class CD that contains the CD's ID, title, and artist

        """
        while True:
            strID = input('Enter ID: ').strip()
            try:
                intID = int(strID)
                break
            except ValueError as e:
                print('ID must be an integer!')
                print(e)
            except Exception as e:
                print('There was a general error!')
                print(e)
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        cdObject = CD(intID, strTitle, strArtist)
        return cdObject
    

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
try:
    lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
except FileNotFoundError as e:
    print('File does not exist!')
    print(e) 
    pass
except Exception as e:
    print('There was a general error!')
    print(e)
    pass

# Display menu to user
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    # show user current inventory
    if strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user add data to the inventory
    elif strChoice == 'a':
        newCD = IO.add_inventory_menu()
        lstOfCDObjects.append(newCD.dicRow)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # let user load inventory from file
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user exit program
    elif strChoice == 'x':
        break
    else:
        print('General Error')

