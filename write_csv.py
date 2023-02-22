import pandas as pd 

def write_dataset_to_csv(dataset_list):
    cols=["test_column1", "test_column2"]
    fn = "test_csv.csv"
    df = pd.DataFrame(dataset_list, columns=cols)
    df.to_csv(fn, index=False)