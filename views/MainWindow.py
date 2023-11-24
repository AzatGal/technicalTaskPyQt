from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QMainWindow, QTableView, QVBoxLayout, QWidget

from models.DataModels import MongoDBContext
from views.ChartDialog import ChartDialog


class MainWindow(QMainWindow):
    def __init__(self, _users: MongoDBContext):
        super().__init__()
        self.users = _users

        self.model = QStandardItemModel()
        self.model.setColumnCount(1)
        self.model.setHorizontalHeaderLabels(["User name"])

        self.table = QTableView()
        font = QFont()
        font.setPointSize(13)
        self.table.setFont(font)
        self.table.setModel(self.model)
        self.table.doubleClicked.connect(self.open_chart_window)

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.accounts = dict()

        for i in self.users.accounts_df['username']:
            self.add_account(i)
            self.accounts[i] = self.users.accounts_df.loc[self.users.accounts_df['username'] == i]['id'].values[0]

    def add_account(self, account):
        item_account = QStandardItem(account)
        self.model.appendRow([item_account])

    def open_chart_window(self, index):
        selected_account = self.model.item(index.row(), 0).text()
        graph_window = ChartDialog(self.users)
        graph_window.resize(1000, 500)
        graph_window.show_chart(self.accounts[selected_account], selected_account)
        graph_window.exec_()



