def data_explorer(path): 
    import pandas as pd

    # Load the dataset based on file extension
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    elif path.endswith(".xlsx"):
        df = pd.read_excel(path)
    elif path.endswith(".json"):
        df = pd.read_json(".json")
    else:
        raise ValueError("Unsupported file format")
    
    # How the output should be computed with labels
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nDescriptive Stats:\n", df.describe())

    return df

path = r"C:\Users\Michael Inedu\OneDrive\Data Analyst Portfolio_Michael_Inedu\Python for Data Analysis - 1 year milestone learning\Phase 1 - Dataset\iris.csv"

df = data_explorer(path)