import re
import pandas as pd


def extract_price_from_text(text: str) -> str:
    """
    Extracts the price from the given text.
    """
    match = re.search(r"\$(\d+\.\d+)", text)

    if match:
        number = match.group(1)
    else:
        print("No match found.")
    return number


def get_excel_data(file_path: str) -> list:
    """
    Reads the data from the given Excel file.
    """
    df = pd.read_excel(file_path)
    columns_to_lists = [df.iloc[:, i].tolist() for i in range(df.shape[1])]

    return columns_to_lists
