import pandas as pd
import numpy as np


def augmentDF(DF):
    ColumnsTypes = {"Name": "object", "Gender": "object", "Role": "object",
                    "Salary": "float64", "Age": "Int64",
                    "Education": "object", "Distance": "Int64",
                    "Remote": "boolean", "Marital status": "object",
                    "Smoking": "boolean", "Driver license": "boolean",
                    "Language skills": "object", "Employed at": "datetime64[ns]"}
    TypeNullVal = {
    "Int64": pd.NA,
    "float64": np.nan,
    "boolean": np.nan,
    "datetime64[ns]": pd.NaT,
    "object": np.nan
    }
    PrevCols = DF.columns
    UpdatedDF = DF
    for Column, Type in ColumnsTypes.items():
        if not Column in PrevCols:
            UpdatedDF[Column] = TypeNullVal[Type]
        UpdatedDF[Column] = UpdatedDF[Column].astype(Type)
    return UpdatedDF


def isAnyNullType(Obj):
    NullTypes = [pd.NA, np.nan, pd.NaT, None]
    for Type in NullTypes:
        if Obj is Type:
            return True
    return False

# def readDF(FileName):
#     return pd.read_excel(FileName)

# def writeDF(FileName, DF):
#     DF.to_excel(FileName, index=False)

