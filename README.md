### Supermarket Recommendation System

****


**this project provide a** `Recommender.py` **Class**

How to use this class !!

### Class Constructor Parameter

` __init__(self, transactionsDataset: List[Dict], userRow: set = {}, matchCount: int = 20,
                 returnItemCount: int = 10, useSerialization=False)`
                 

**1 -** `transactionsDataset` this is the dataset should be like this

`transactions = [

            ['Milk', 'Onion', 'Nutmeg', 'Kidney_Beans', 'Eggs', 'Yogurt'],
            ['Dill', 'Onion', 'Nutmeg', 'Kidney_Beans', 'Eggs', 'Yogurt'],
            ['Milk', 'Apple', 'Kidney_Beans', 'Eggs'],
            ['Milk', 'Unicorn', 'Corn', 'Kidney_Beans', 'Yogurt'],
            ['Corn', 'Onion', 'Kidney_Beans', 'Ice_cream', 'Eggs'],
            ['Corn', 'Onion', 'Ice_cream', 'Eggs'],
            ['Dill', 'Onion', 'Nutmeg', 'Eggs', 'Yogurt'],
            ['Milk', 'Onion', 'Nutmeg', 'Yogurt'],
    ]`

**2 -** `userRow` this is the row that the algorithm use to suggest a new items

**3 -** `matchCount` this is the N rows that the algorithm will select best N that match `userRow`

**4 -** `returnItemCount` the Best N items that will returned 

**5 -** `useSerialization` if you want to use serialization this proccess will train the dataset only once and then will store the result on hard disk 
when you want to learn the algorithm again it will load from the hard disk insted of looping throw the database each time



## Example

`userRow = [12,345,456567,6745,444,213,767,227]`

`recommender = Recommender(bills_items, userRow=userRow, matchCount=200, useSerialization=True)`


`best_items = recommender.run()`

`print(best_items)`