import pandas as pd
from pymongo.mongo_client import MongoClient
from abc import ABC, abstractmethod


class DBContex(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_results_of_bet_df(self, account_id):
        pass

    @abstractmethod
    def current_balance_df(self, account_id):
        pass


class MongoDBContext(DBContex):
    def __init__(self):
        self.url = "mongodb+srv://azat:azat@cluster0.kf6oe42.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        self.client = MongoClient(self.url)
        self.accounts_df = pd.DataFrame(self.client['users']['accounts'].find())
        self.bets_df = pd.DataFrame(self.client['users']['bets'].find())
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def md_client(self):
        return self.client

    def accounts_collection(self):
        return self.client['users']['accounts']

    def bets_collection(self):
        return self.client['users']['bets']

    def get_bets_df(self, account_id):
        return self.bets_df[self.bets_df['id'] == account_id]

    def get_results_of_bet_df(self, account_id):
        df = self.get_bets_df(account_id)
        df.loc[:, 'result of bet'] = df.loc[:, 'return'] - df.loc[:, 'bet_amount']
        return df

    def current_balance_df(self, account_id):
        df = self.get_results_of_bet_df(account_id)
        df.loc[:, 'bet_datetime'] = pd.to_datetime(df.loc[:, 'bet_datetime'])
        df.sort_values('bet_datetime')
        df.loc[:, 'balance'] = df.loc[:, 'balance_first'] - df.loc[:, 'result of bet']
        return df

