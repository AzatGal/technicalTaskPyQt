import sys

from PyQt5.QtWidgets import QApplication

from models.DataModels import MongoDBContext
from views.MainWindow import MainWindow

if __name__ == "__main__":
    u = MongoDBContext()
    app = QApplication(sys.argv)
    window = MainWindow(u)
    window.resize(1000, 500)
    window.show()
    sys.exit(app.exec_())