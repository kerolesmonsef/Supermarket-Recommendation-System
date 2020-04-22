from typing import List, Dict
import pandas as pd
import numpy as np
import pickle
import os


class Recommender:
    def __init__(self, transactionsDataset: List[Dict], userRow: set = {}, matchCount: int = 20,
                 returnItemCount: int = 10, useSerialization=False):

        self.transactions = transactionsDataset
        self.userRow = set(userRow)
        self.matchCount = matchCount
        self.returnItemCount = returnItemCount
        self.pivotTable = pd.DataFrame()

        self.items = set([item for row in transactionsDataset for item in row])
        transactionsLen = len(transactionsDataset)

        if os.path.exists('pivotTable.some') is False or useSerialization is False:
            for item in self.items:
                self.pivotTable[str(item)] = np.zeros(transactionsLen)

            self.pivotTable['relate'] = np.zeros(transactionsLen)

            for indx, row in enumerate(transactionsDataset):
                for item in row:
                    self.pivotTable.at[indx, str(item)] = 1

            with open('pivotTable.some', 'wb') as f:
                pickle.dump(self.pivotTable, f)
        else:
            pickle_in = open('pivotTable.some', 'rb')
            self.pivotTable = pickle.load(pickle_in)

    def setUserRow(self, userRow: list):
        self.userRow = userRow

    def run(self):
        self.compareRows()
        bestMatchedRows = self.bestNMatch(self.matchCount)
        sumBestRows = bestMatchedRows.sum(axis=0)
        sumBestRows.drop(set(map(str, self.userRow)), inplace=True)
        sumBestRows.drop('relate', inplace=True)
        bestSortedItems = sumBestRows.sort_values(ascending=False)
        return bestSortedItems.head(self.returnItemCount)

    def compareRows(self):
        if len(self.userRow) == 0:
            raise Exception("pls choose some items [userRow]")
        userRowLen = len(self.userRow)
        for i in range(len(self.pivotTable)):
            successCount = 0
            for item in self.userRow:
                if self.pivotTable.at[i, str(item)] == 1:
                    successCount += 1
            self.pivotTable.at[i, 'relate'] = float(successCount / userRowLen)

    def bestNMatch(self, N: int = 20) -> pd.DataFrame:
        sortedTable = self.pivotTable.sort_values(by='relate', ascending=False)
        return sortedTable.head(N)
