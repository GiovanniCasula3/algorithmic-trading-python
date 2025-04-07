import numpy as py
import pandas as pd
import requests
import xlsxwriter
import math

stocks = pd.read_csv("starter_files/sp_500_stocks.csv")
print(stocks)