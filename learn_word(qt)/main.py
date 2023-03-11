import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject
from GUI import main


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    stats = MainWindow()
    stats.show()
    sys.exit(app.exec_())