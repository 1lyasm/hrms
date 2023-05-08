import pandas as pd
import sys
sys.path.append("..")
from util.DFAugmenter import DFAugmenter
from util.ExcelIO import ExcelIO


def main():
    FileName = "../data/EmployeesTest.xlsx"
    AugDF = DFAugmenter.augment(ExcelIO.readDF(FileName))
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
      print(AugDF)


if __name__ == "__main__":
    main()
