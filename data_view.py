import pandasgui as pgui

def run_df_gui(df):
    if df is None:
        return False
    pgui.show(df)
    return True
