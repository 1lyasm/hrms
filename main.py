import pandas as pd
import numpy as np

import filter_add


def main():
    print("Systems project - HRMS\n")
    print("Choose action:\n")
    print("""
\t1. Face recognition
\t2. Data view and addition
\t3. Document generation
\t4. Salary management
\t5. Exit
          """)
    df = pd.read_excel("svatprj.xlsx")
    inp = int(input("Choice: "));
    print("")
    if inp == 1:
        pass
    elif inp == 2:
        filter_add.show(df)
    elif inp == 3:
        pass
    elif inp == 4:
        pass
    elif inp == 5:
        exit()
    else:
        print("Thank you.")

if __name__ == "__main__":
    main()

