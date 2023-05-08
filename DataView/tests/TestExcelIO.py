import sys
sys.path.append("..")
from util.ExcelIO import ExcelIO
from util.DFAugmenter import DFAugmenter

# MODIFIES THE EXCEL FILE

def testReadDF(FileName):
    DF = ExcelIO.readDF(FileName)
    print(DF)
    return DF

def testWriteDF(FileName, DF):
    DF.at[0, "Role"] = "Changed"
    DF = DFAugmenter.augment(DF)
    ExcelIO.writeDF(FileName, DF)
    DFAfterUpdate = ExcelIO.readDF(FileName)
    print("\n\nAfter update: \n", DFAfterUpdate)

def main():
    FileName = "../data/EmployeesTest.xlsx"
    DF = testReadDF(FileName)
    testWriteDF(FileName, DF)
    testReadDF(FileName)


if __name__ == "__main__":
    main()
