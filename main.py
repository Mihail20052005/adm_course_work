from graph.graph_algo import *
from graph.graph_structure import *
from gui.gui import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
