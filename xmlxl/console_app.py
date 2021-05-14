# This is just an outline of the Console Application that processes the Excel file

import openpyxl as XL
import colorama
import os
import sys
import xml.etree.ElementTree as ET
import random
# import lxml.etree as ET
import datetime

def welcome_msg(): 
    print(colorama.Fore.BLUE + colorama.Back.WHITE + "---------------------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE + colorama.Back.WHITE + " XML Generation Utility for Form 15CA Part A " + colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE + colorama.Back.WHITE + "---------------------------------------------" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "This utility accepts an Excel file as input and produces multiple XML files as output." + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "The resultant XML files will be saved in a subfolder named \"XML<nnnn>\", (where \"<nnnn>\" is a 4-digit random number), e.g. XML1565, in the same folder as that of the given Excel file." + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "Further, this utility does not perform any data validation. It merely assumes that all data entered in the Excel file is valid, complete, and correct." + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "In other words, this utility purely operates upon the provided data on GIGO basis i.e. \"Garbage In, Garbage Out\"." + colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + colorama.Style.BRIGHT+ "This utility may seriously harm your computer if used irresponsibly." + colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + colorama.Style.BRIGHT+ "Do not proceed if you don\'t know or understand the purpose of this program." + colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + colorama.Style.BRIGHT+ "Warning: Only for use with the prescribed Excel file supplied with this utility." + colorama.Style.RESET_ALL)
    user_choice = input(r"Cotinue? (Y/N): ")
    if ((user_choice == 'Y') or (user_choice == 'y')):
        return True
    else:
        return False

def get_file_name():
    return input("Enter complete path of the Excel file (including filename): ")

def check_file_existence(excel_file):
    return os.path.exists(excel_file)

def main():
    colorama.init()
    
    if (welcome_msg()==False):
        error_handler("ERR1000")
        sys.exit(0)

    excel_file_name = get_file_name()

    if (check_file_existence(excel_file_name) == False):
        error_handler("ERR1001")
        sys.exit(0)
    
    xlwb = open_xl_workbook(excel_file_name)


# Once the Excel file is accessed: 
# 1. Each cell is validated in all rows
# 2. If there is even one error, the same is displayed and the application exits to command prompt without processing furthter
# 3. If no validation errors are found, each row is converted to one XML file
# 4. Exit to command prompt after all rows have been converted to XML