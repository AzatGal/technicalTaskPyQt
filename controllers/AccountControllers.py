from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class UserController:
    def __init__(self, _db):
        self.__data_base = _db

    def get_plot(self, account_id):
        figure = Figure()
        canvas = FigureCanvasQTAgg(figure)
        ax = figure.add_subplot(111)
        if len(self.__data_base.current_balance_df(account_id)['bet_datetime']) == 0 or \
                len(self.__data_base.current_balance_df(account_id)['balance']) == 0:
            label = QLabel("user has no bets")
            label.setAlignment(Qt.AlignCenter)
            font = QFont()
            font.setPointSize(50)
            label.setFont(font)
            return label
        else:
            ax.plot(self.__data_base.current_balance_df(account_id)['bet_datetime'],
                    self.__data_base.current_balance_df(account_id)['balance'], 'o')
            return canvas

    def get_accounts(self):
        return self.__data_base.accounts_df.set_index('username')['id'].to_dict()










