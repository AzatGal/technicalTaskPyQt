from PyQt5.QtWidgets import QVBoxLayout, QDialog

from controllers.AccountControllers import UserActions
from models.DataModels import MongoDBContext


class ChartDialog(QDialog):
    def __init__(self, _users: MongoDBContext):
        super().__init__()
        self.setWindowTitle("Window with chart")
        self.users = _users

    def show_chart(self, account_id, account_name):
        ua = UserActions(account_id, self.users)
        canvas = ua.get_plot()
        self.setWindowTitle(f"User {account_name} balance chart")
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.setLayout(layout)
