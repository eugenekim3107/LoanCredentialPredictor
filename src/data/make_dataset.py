import pandas as pd

#url to generate data from github
url = 'https://raw.githubusercontent.com/eugenekim3107/LoanProject/main/data/raw/loan_data.csv'
loan = pd.read_csv(url, sep=",")

#not necessary for this project
loan = loan.drop(['not.fully.paid'],axis=1)
