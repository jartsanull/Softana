import pandas as pd

def read_excel():
    # Reading an Excel file
    df = pd.read_excel('file.xlsx', sheet_name='Sheet1')