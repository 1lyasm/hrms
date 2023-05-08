import pandas as pd

class ExcelIO:
    @staticmethod
    def readDF(FileName):
        return pd.read_excel(FileName)

    @staticmethod
    def writeDF(FileName, DF):
        DF.to_excel(FileName, index=False)
