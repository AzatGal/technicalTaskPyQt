from PyQt5.QtWidgets import QVBoxLayout, QDialog


class ChartDialog(QDialog):
    def __init__(self, _user_controller):
        super().__init__()
        self.setWindowTitle("Window with chart")
        self.user_controller = _user_controller

    def show_chart(self, account_id, account_name):
        canvas = self.user_controller.get_plot(account_id)
        self.setWindowTitle(f"User {account_name} balance chart")
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.setLayout(layout)
