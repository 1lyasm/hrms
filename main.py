import pandas as pd
import numpy as np

import data_view


def read_df(file_name):
    return augment_df(pd.read_excel(file_name))


def augment_df(DF):
    columns_types = {
        "Name": "object",
        "Surname": "object",
        "Gender": "object",
        "Role": "object",
        "Salary": "float64",
        "Age": "Int64",
        "Education": "object",
        "Distance": "Int64",
        "Remote": "boolean",
        "Marital status": "object",
        "Smoking": "boolean",
        "Driver license": "boolean",
        "Language skills": "object",
        "Employed at": "datetime64[ns]"
    }
    type_null_val = {
        "Int64": pd.NA,
        "float64": np.nan,
        "boolean": np.nan,
        "datetime64[ns]": pd.NaT,
        "object": np.nan
    }
    prev_cols = DF.columns
    updated_df = DF
    for column, type in columns_types.items():
        if not column in prev_cols:
            updated_df[column] = type_null_val[type]
        updated_df[column] = updated_df[column].astype(type)
    return updated_df


def write_df(df, file_name):
    try:
        df.to_excel(file_name, index=False)
    except PermissionError:
        print(f"{file_name} is open in another program")
        exit()


def main():
    print("Systems project - HRMS\n")
    print("Choose action:\n")
    print("""
    1. Face recognition
    2. Data view
    3. Document generation
    4. Employee database
    5. Salary management
    6. Exit
          """)
    file_name = "employees_new.xlsx"
    df = read_df(file_name)
    inp = int(input("Choice: "));
    print("")
    if inp == 1:
        pass
    elif inp == 2:
        data_view.show(df)
    elif inp == 3:
        pass
    elif inp == 4:
        print(df.to_string()) 
    elif inp == 5:
        pass
    elif inp == 6:
        exit()
    else:
        print("error")
    write_df(df, file_name)

if __name__ == "__main__":
    main()

