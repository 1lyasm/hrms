import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def augmentDF(DF):
    columns_types = {"Name": "object", "Surname": "object", "Gender": "object", "Role": "object",
                    "Salary": "float64", "Age": "Int64",
                    "Education": "object", "Distance": "Int64",
                    "Remote": "boolean", "Marital status": "object",
                    "Smoking": "boolean", "Driver license": "boolean",
                    "Language skills": "object", "Employed at": "datetime64[ns]"}
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


def is_any_null_type(obj):
    null_types = [pd.NA, np.nan, pd.NaT, None]
    for type in null_types:
        if obj is type: return True
    return False


def run(FileName):
    df = pd.read_excel(FileName)
    df = augmentDF(df)
    views = ["gender_barchart",
            "age_groups_barchart", 
            "marital_status_barchart",
            "smoking_habit_barchart",
            "onsite_remote_barchart",
            "driver_license_barchart", 
            "salary_barchart",
            "education_barchart"
    ]


    def gen_gender_barchart():
        x_axis = ["M", "F"]
        height = df["Gender"].value_counts()
        plt.bar(x_axis, height=height, label="Gender")
        plt.legend()
        plt.savefig("views/gender_barchart.jpg")

    
    def gen_age_groups_barchart():
        pass


    def gen_marital_status_barchart():
        pass


    def gen_smoking_habit_barchart():
        pass


    def gen_onsite_remote_barchart():
        pass


    def gen_driver_license_barchart():
        pass


    def gen_salary_barchart():
        pass


    def gen_education_barchar():
        pass


    generators = [gen_gender_barchart,
            gen_age_groups_barchart, 
            gen_marital_status_barchart,
            gen_smoking_habit_barchart,
            gen_onsite_remote_barchart,
            gen_driver_license_barchart, 
            gen_salary_barchart,
            gen_education_barchar
    ]
    for gen in generators: gen()
    try:
        os.mkdir("views")
    except FileExistsError:
        pass
    print("Views: ")
    for view in views: print(f"\t{view}")
    df.to_excel(FileName, index=False)
    help_text = """
Commands: 
    help: Display this page
    show [file_name]: Display file_name view
    q: Return to main menu
    """

     while (True):
        try:
            inp = input("> ")
        except KeyboardInterrupt:
            return
        if inp == "help":
            print(help_text)
        elif inp == "": pass
        elif inp.split()[0] == "show":
            if len(inp.split()) == 1:
                print("show requires parameter")
            else:
                file_name = inp.split()[1]
                print(file_name)
                if not file_name in views:
                    print("View does not exist")
        elif inp == "q":
            return
        else:
            print("Invalid command")


def main():
    run("EmployeesNew.xlsx")


if __name__ == "__main__":
    main()
