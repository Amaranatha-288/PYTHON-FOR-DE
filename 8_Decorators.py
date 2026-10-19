def pandas_decorator(fx):

    def mainfunc(*args):
       response = fx(*args)
       #Do some pandas specific processing here
       response.to_parquet(".venv\Ch_1_OOP\\temp.parquet")
       return response
    
    return mainfunc

@pandas_decorator
def csv_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(".venv\Ch_1_OOP\\orders.csv")
    return df

response = csv_to_parquet(".venv\Ch_1_OOP\orders.csv")
print(response.head())