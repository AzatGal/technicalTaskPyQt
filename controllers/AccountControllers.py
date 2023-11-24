from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class UserActions:
    def __init__(self, _id, _user):
        self.account_id = _id
        self.user = _user

    def get_plot(self):
        figure = Figure()
        canvas = FigureCanvasQTAgg(figure)
        ax = figure.add_subplot(111)
        if len(self.user.current_balance_df(self.account_id)['bet_datetime']) != 0 and \
                len(self.user.current_balance_df(self.account_id)['balance']) != 0:
            ax.plot(self.user.current_balance_df(self.account_id)['bet_datetime'],
                    self.user.current_balance_df(self.account_id)['balance'], 'o')
            return canvas
        else:
            label = QLabel("user has no bets")
            label.setAlignment(Qt.AlignCenter)
            font = QFont()
            font.setPointSize(50)
            label.setFont(font)
            return label








