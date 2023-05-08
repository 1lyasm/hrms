import pandas as pd
import numpy as np

def isAnyNullType(Obj):
    NullTypes = [pd.NA, np.nan, pd.NaT, None]
    for Type in NullTypes:
        if Obj is Type:
            return True
    return False
