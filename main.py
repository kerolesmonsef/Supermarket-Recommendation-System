import pandas as pd
from Recommender import Recommender

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

bills = pd.read_csv("dataset/bills.csv")
bills_items = bills.groupby('billID').apply(lambda x: set((x['itemID'])))
#
# transactions = [
#     ['Milk', 'Onion', 'Nutmeg', 'Kidney_Beans', 'Eggs', 'Yogurt'],
#     ['Dill', 'Onion', 'Nutmeg', 'Kidney_Beans', 'Eggs', 'Yogurt'],
#     ['Milk', 'Apple', 'Kidney_Beans', 'Eggs'],
#     ['Milk', 'Unicorn', 'Corn', 'Kidney_Beans', 'Yogurt'],
#     ['Corn', 'Onion', 'Kidney_Beans', 'Ice_cream', 'Eggs'],
#     ['Corn', 'Onion', 'Ice_cream', 'Eggs'],
#     ['Dill', 'Onion', 'Nutmeg', 'Eggs', 'Yogurt'],
#     ['Milk', 'Onion', 'Nutmeg', 'Yogurt'],
# ]
userRow = bills_items.iloc[1]
recommender = Recommender(bills_items, userRow=userRow, matchCount=200, useSerialization=True)
best_items = recommender.run()
print(best_items)
