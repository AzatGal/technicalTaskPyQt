import sys

from PyQt5.QtWidgets import QApplication

from models.MongoDB import MongoDB
from views.MainWindow import MainWindow

if __name__ == "__main__":
    db = MongoDB()
    app = QApplication(sys.argv)
    window = MainWindow(db)
    window.resize(1000, 500)
    window.show()
    sys.exit(app.exec_())
