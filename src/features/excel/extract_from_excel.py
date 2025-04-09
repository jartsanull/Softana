import pandas as pd

excel_input = input("")
excel_reader = input("")

excel_choices = ["read"]

def read_excel():
    # Reading an Excel file
    df = pd.read_excel(excel_reader, sheet_name='Sheet1')

match excel_choices:
    case "read":
        read_excel()
    case _:
        print("Invalid choice")