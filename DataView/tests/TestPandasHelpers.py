import sys
sys.path.append("..")

import pandas as pd
import numpy as np
from DataView import isAnyNullType

def testIsAnyNullType():
    print("testIsAnyNullType: ", end="")
    assert(isAnyNullType(pd.NA) == True)
    assert(isAnyNullType(pd.NaT) == True)
    assert(isAnyNullType(np.nan) == True)
    assert(isAnyNullType(None) == True)

    assert(isAnyNullType(4) == False)
    assert(isAnyNullType("string") == False)
    print("PASSED")


def main():
    testIsAnyNullType()

if __name__ == "__main__":
    main()
