if __name__ == "__main__":

    from PyQt5.QtWidgets import QApplication

    import gui
    import sys
       
    app = QApplication(sys.argv)
    Mainwindow = gui.MainWindow()
    Mainwindow.setup(639, 679)
    Mainwindow.show()
    sys.exit(app.exec_())        
