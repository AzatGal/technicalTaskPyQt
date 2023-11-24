from abc import ABC, abstractmethod


class AbstractDB(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_results_of_bet_df(self, account_id):
        pass

    @abstractmethod
    def current_balance_df(self, account_id):
        pass