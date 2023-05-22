import pandas as pd
import numpy as np
import os

import filter_add
import face_recog.recognizer as recog
import doc_gen


def main():
    print("Systems project - HRMS\n")
    print("Choose action:\n")
    print("""
\t1. Face recognition
\t2. Data view and addition
\t3. Document generation
\t*. Exit""")
    df = pd.read_excel("svatprj.xlsx")
    while 1: 
        inp = int(input("\nChoice: "));
        print("")
        if inp == 1:
            recog.show()
        elif inp == 2:
            filter_add.show(df)
        elif inp == 3:
            doc_gen.show(df)
        else: 
            exit()

if __name__ == "__main__":
    main()

