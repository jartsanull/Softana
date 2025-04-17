import os
import pandas as pd
import time


def extract_excel():
    excel_reader = input("Choose a file: \n")
    return excel_reader


def excel_detector(excel_reader):
    if os.path.exists(excel_reader):
        print("The file is brought")
        return True
    else:
        print("Error: the file does not exist")
        return False


excel_choices = ["Read", "Filter", "Analyse"]


def excel_choose():
    print("Please choose a function: \n")
    for choice in excel_choices:
        print(f"{choice}")
    choice = input("").lower()
    return choice


def read_excel(excel_reader):
    try:
        df = pd.read_excel(excel_reader)
        print("Excel content:")
        print(df.head())
    except Exception as e:
        print(f"Error reading Excel file: {e}")


def extractExc_main():
    excel_reader = extract_excel()
    time.sleep(3)
    print()
    choice_ex = excel_choose()
    print()

    match choice_ex:
        case "read":
            read_excel(excel_reader=excel_reader)
        case "filter":
            print("Filter function not yet implemented.")
        case "analyse":
            print("Analyse function not yet implemented.")
        case _:
            print("Invalid choice")


extractExc_main()
