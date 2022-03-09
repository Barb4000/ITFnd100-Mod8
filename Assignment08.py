# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# BSpadavecchia,03.06.2022,Added properties and methods to complete assignment 8
# BSpadavecchia,03.07.2022,Added error handling in the setter for product name and price
# BSpadavecchia,03-08-2022,Added error handling, comments
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ""
strProductName = ""
fltProductPrice = None
objProduct = None

class Product:
    """Stores data about a product:

    constructor:
        __product_name:  private attribute
        __Product_price:  private attribute

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price

    methods:
        __str__(self):  comma separated for printing or storing
        product_add_to_lst(obj, list_Of_Product_Obj): ->list_Of_Product_Obj
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        BSpadavecchia,03.06.2022,Modified code to complete assignment 8
    """
    # Constructor
    def __init__(self, product_name, product_price):
        # Attributes
        self.__product_name = product_name
        self.__product_price = product_price

        # Properties
    @property
    def product_name(self):
        return str(self.__product_name).upper()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product name can not contain numbers")

    @property
    def product_price(self):
        return round(self.__product_price, 2)

    @product_price.setter
    def product_price(self, value):
        if value.isalpha() == False:
            self.__product_price = float(value)
        else:
            raise Exception("Product price must be a number")
    # -- Methods
    def __str__(self):
        """Comma separation for writing to file and display
        :param product_name: string attribute
        :param product_price: float attribute converted to string
        """
        return self.product_name +"," + str(self.product_price)

    def product_add_to_list(object, list_of_product_objects):
        """Adds new object to list
        :param list_of_product_obj: list of objects
        :return list of objects
        """
        list_of_product_objects.append(object)
        return list_of_product_objects
# Processing

class FileProcessor:
    """Processes data to and from a file and list of products
        Methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (list of product objects)
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """Reads lines from file and puts them in a list
        :param file_name: name of file (target)
        :param file: object for (target) file
        :param product_name: attribute of object
        :param product_price: attribute of object
        :param list_of_product_obj: list of objects
        :return list of objects
        """
        list_of_product_objects.clear()
        while True:
            try:
                with open(file_name, "r+") as file:
                    for line in file:
                        product_name, product_price = line.split(",")
                        row = Product(product_name, float(product_price))
                        list_of_product_objects.append(row)
            except EOFError: #End read loop if at end of file
                break
            except FileNotFoundError: #Create file if it doesn't exist
                print("File not found")
                print() #extra line
                file = open(file_name, "a+")
                file.close()
                break
            finally: #End loop if no errors found
                print("File loaded successfully\n")
                break
        return list_of_product_objects
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """Saves data from list to file
        :param file_name: target file
        :param file: object for target file
        return: list
        """
        with open(file_name, "w+") as file:
            for product in list_of_product_objects:
                #Strings formatted with __str__ method in Product
                file.write(str(product) + "\n")
        return list_of_product_objects
    # Processing  ------------------------------------------------

    # Presentation (Input/Output) --------------------------------
class IO:
    """Prints menu, lists, and captures input for products

    methods:
        print_main_menu_options():
        input_menu_choice():
        print_list_of_products(list_of_product_objects):
        input_product_details(): -> new_product_object
        """
    @staticmethod
    def print_main_menu_options():
        """Displays a menu of options to user
        :return nothing
        """
        print("""
        Menu of Options:
        1 - Show Current List
        2 - Add A New Product
        3 - Save Product List
        4 - Exit Program
        """)

    @staticmethod
    def input_menu_choice():
        """Captures menu choice from user
        :param choice: int options 1-4
        :return: string
        """
        choice = str(input("Please choose an option [1-4]: ")).strip()
        print()
        return choice

    @staticmethod
    def print_list_of_products(list_of_product_objects):
        """Shows current list of products
        :param product_object: objects in list
        :param list_of_product_objects list of objects to display
        :return: nothing
        """
        print("***************PRODUCTS***************")
        if len(list_of_product_objects) > 0:
            for product_object in list_of_product_objects:
                print(product_object.product_name + " at $" + str(product_object.product_price))
        else:print("No Product Information to Display")

    @staticmethod
    def input_product_details():
        """Create new product object, initialize, fill with user input
        :param new_product_object: object
        :param product_name: attribute of object
        :param product_price: attribute of object
        :return: object
        """
        new_product_object = Product("", None) #Initialize new object
        new_product_object.product_name = input("What is the Product's Name?: ")
        new_product_object.product_price = input("What is the Product's Price?: ")
        return new_product_object

 # Presentation (Input/Output) ------------------------------------------------#

# Main Body of Script --------------------------------------------------------#

# Load data from file into list of products when script starts

FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
#Show User a Menu of Options
while True:
    IO.print_main_menu_options()

    # Get User's Menu Option Choice
    strChoice = IO.input_menu_choice()

    # Show User Current Data in List of Product Objects
    if strChoice.strip() =="1":
        IO.print_list_of_products(lstOfProductObjects)

    # Let User Add Data to Product Objects
    if strChoice.strip() =="2":
        try:
            objProduct = IO.input_product_details()
            Product.product_add_to_list(objProduct, lstOfProductObjects)
            print("\n\"" + objProduct.product_name + "\"" +
            "has been added to the List of Products for $" +
            str(objProduct.product_price))
        except Exception as e: #Error handling for attribute
            print(e)
    # Let User Save Data
    if strChoice.strip() == "3":
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print("The List of Products has been saved")

    # Let User Exit the Program
    if strChoice.strip() == "4":
        print("You have chosen to exit the program Goodbye")
        break