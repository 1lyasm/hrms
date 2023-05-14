from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


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


def is_any_null_type(obj):
    null_types = [pd.NA, np.nan, pd.NaT, None]
    for type in null_types:
        if obj is type: return True
    return False


def run(file_name):
    try: 
        df = pd.read_excel(file_name)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        exit()
    df = augment_df(df)
    views = [
        "gender_barchart", "age_groups_barchart", "marital_status_barchart",
        "smoking_habit_barchart", "onsite_remote_barchart",
        "driver_license_barchart", "salary_barchart", "education_barchart"
    ]
    image_ext = "jpg"
    bar_colors = ["red", "blue", "cyan"]
    def gen_gender_barchart():
        x_axis = ["M", "F", "NaN"]
        height = df["Gender"].replace(np.nan, "NaN") \
            .value_counts().reindex(x_axis, fill_value=0)
        height.plot(kind="bar", color=bar_colors)
        plt.xlabel("Gender")
        plt.ylabel("Count")
        plt.title("Gender distribution")

    def gen_age_groups_barchart():
        age_groups = pd.cut(df["Age"], bins=[0, 18, 30, 50, float("inf")], labels=["0-18", "19-30", "31-50", "51+"])
        height = age_groups.value_counts().sort_index()
        colors = ["blue", "green", "orange", "red"]  # Define colors for each age group
        
        height.plot(kind="bar", color=colors)
        plt.xlabel("Age Groups")
        plt.ylabel("Count")
        plt.title("Age Groups Distribution")
        plt.savefig(f"views/age_groups_barchart.{image_ext}")

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

    generators = [
        gen_gender_barchart, gen_age_groups_barchart,
        gen_marital_status_barchart, gen_smoking_habit_barchart,
        gen_onsite_remote_barchart, gen_driver_license_barchart,
        gen_salary_barchart, gen_education_barchar
    ]
    try:
        os.mkdir("views")
    except FileExistsError:
        pass
    for gen in generators:
        gen()
        plt.savefig(f"views/{gen.__name__[4:]}.{image_ext}")
    print("Views: ")
    for view in views:
        print(f"\t{view}")
    try:
        df.to_excel(file_name, index=False)
    except PermissionError:
        print(f"{file_name} is open in another program")
        exit()
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
        elif inp == "":
            pass
        elif inp.split()[0] == "show":
            if len(inp.split()) == 1:
                print("show requires parameter")
            else:
                file_name = inp.split()[1]
                if file_name in views:
                    Image.open(f"views/{file_name}.{image_ext}").show()
                else:
                    print("View does not exist")
        elif inp == "q":
            return
        else:
            print("Invalid command")


def main():
    run("employees_new.xlsx")


if __name__ == "__main__":
    main()
