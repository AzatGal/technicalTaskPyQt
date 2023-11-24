from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QMainWindow, QTableView, QVBoxLayout, QWidget, QLabel, QAbstractItemView

from controllers.AccountControllers import UserController
from views.ChartDialog import ChartDialog


class MainWindow(QMainWindow):
    def __init__(self, _db):
        super().__init__()
        self.user_controller = UserController(_db)

        self.model = QStandardItemModel()
        self.model.setColumnCount(1)
        self.model.setHorizontalHeaderLabels(["User name"])

        self.table = QTableView()
        font = QFont()
        font.setPointSize(13)
        self.table.setFont(font)
        self.table.setModel(self.model)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.doubleClicked.connect(self.open_chart_window)

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.add_accounts()

    def add_accounts(self):
        for i in self.user_controller.get_accounts():
            item_account = QStandardItem(i)
            self.model.appendRow([item_account])

    def open_chart_window(self, index):
        selected_account = self.model.item(index.row(), 0).text()
        graph_window = ChartDialog(self.user_controller)
        graph_window.resize(1000, 500)
        if selected_account not in list(self.user_controller.get_accounts().keys()):
            graph_window.show_chart('-1', 'unexisted account')
        else:
            graph_window.show_chart(self.user_controller.get_accounts()[selected_account], selected_account)
        graph_window.exec_()

