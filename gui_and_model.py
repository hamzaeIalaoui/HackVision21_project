import pandas as pd 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QFileDialog
import sys
import csv

school_names = []
student_enrolls = []
teaching_staffs = []
ICSEA_scores = []
expenditures = []


class MainWindow(QMainWindow):

    def on_resize(self):
        self.dimension = self.size()
        width,height= self.dimension.width(), self.dimension.height

    def setup(self, width, height):
        self.setObjectName("MainWindow")
        self.resize(639, 679)
        self.setMinimumSize(639,679)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.QuitButton = QtWidgets.QPushButton(self.central_widget)
        self.QuitButton.setGeometry(QtCore.QRect(20, 590, 71, 31))
        self.QuitButton.setStyleSheet("font: 63 11pt \"URW Gothic\";\n"
"background-color:  rgb(55, 91, 182)")
        self.QuitButton.setObjectName("QuitButton")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(210, 10, 211, 201))
        self.label.setStyleSheet("background-image: url(./logo.png);")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("./logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.central_widget)
        self.groupBox.setGeometry(QtCore.QRect(110, 210, 401, 71))
        self.groupBox.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.groupBox.setObjectName("groupBox")
        self.schoolnameinputline = QtWidgets.QLineEdit(self.groupBox)
        self.schoolnameinputline.setGeometry(QtCore.QRect(10, 30, 291, 31))
        self.schoolnameinputline.setObjectName("schoolnameinputline")
        self.checkbutton = QtWidgets.QPushButton(self.groupBox)
        self.checkbutton.setGeometry(QtCore.QRect(310, 30, 81, 31))
        self.checkbutton.setStyleSheet("font: 63 13pt \"URW Gothic\";\n"
"background-color:  rgb(55, 91, 182)")
        self.checkbutton.setObjectName("checkbutton")
        self.groupBox_6 = QtWidgets.QGroupBox(self.central_widget)
        self.groupBox_6.setGeometry(QtCore.QRect(130, 280, 361, 291))
        self.groupBox_6.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 30, 191, 71))
        self.groupBox_2.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.Nofenrolledfield = QtWidgets.QTextBrowser(self.groupBox_2)
        self.Nofenrolledfield.setGeometry(QtCore.QRect(10, 30, 171, 31))
        self.Nofenrolledfield.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.Nofenrolledfield.setObjectName("Nofenrolledfield")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_3.setGeometry(QtCore.QRect(210, 30, 141, 71))
        self.groupBox_3.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.numberofteachersFIELD = QtWidgets.QTextBrowser(self.groupBox_3)
        self.numberofteachersFIELD.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.numberofteachersFIELD.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.numberofteachersFIELD.setObjectName("numberofteachersFIELD")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_5.setGeometry(QtCore.QRect(100, 190, 171, 81))
        self.groupBox_5.setStyleSheet("font: 14pt \"Ubuntu\";")
        self.groupBox_5.setObjectName("groupBox_5")
        self.fundingelegibilityfield = QtWidgets.QTextBrowser(self.groupBox_5)
        self.fundingelegibilityfield.setGeometry(QtCore.QRect(10, 30, 151, 41))
        self.fundingelegibilityfield.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.fundingelegibilityfield.setObjectName("fundingelegibilityfield")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 110, 191, 71))
        self.groupBox_4.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.groupBox_4.setObjectName("groupBox_4")
        self.Expenditurefield = QtWidgets.QTextBrowser(self.groupBox_4)
        self.Expenditurefield.setGeometry(QtCore.QRect(10, 30, 171, 31))
        self.Expenditurefield.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.Expenditurefield.setObjectName("Expenditurefield")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setGeometry(QtCore.QRect(210, 110, 131, 71))
        self.groupBox_7.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.groupBox_7.setObjectName("groupBox_7")
        self.ICSEAscorefield = QtWidgets.QTextBrowser(self.groupBox_7)
        self.ICSEAscorefield.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.ICSEAscorefield.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.ICSEAscorefield.setObjectName("ICSEAscorefield")
        MainWindow.setCentralWidget(self,  self.central_widget)


        self.QuitButton.clicked.connect(self.exit_app) 
        self.checkbutton.clicked.connect(self.search_school)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def search_school(self):
        DATA = []
        target_school = self.schoolnameinputline.text()
        for x in school_names:
            if target_school == school_names[x]:
                 self.Expenditurefield.append(expenditures[x])
                 self.ICSEAscorefield.append(ICSEA_scores[x])
                 self.Nofenrolledfield.append(student_enrolls[x])
                 self.numberofteachersFIELD.append(teaching_staffs[x])

    def model(self, DATA):
        #import the data in dfx
        dfx  =pd.read_excel("data123.xlsx")
        X = dfx.iloc[:, 1:-1].values
        y = dfx.iloc[:, -1].values
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)
        #modelling
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(n_estimators = 5, criterion = 'entropy')
        model.fit(X_train, y_train)

        #0 means fund required, 1 means fund no required
        unseenXExpand=[]
        unseenXExpand.append([1422,163,760,10176])
        unseenXExpand.append([1222,263,960,16176])
        unseenXExpand.append(DATA)

        y_pred1 = model.predict(unseenXExpand)
        y_pred1[-1]
        # In[ ]:


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "FEC"))
        self.QuitButton.setText(_translate("MainWindow", "Quit"))
        self.groupBox.setTitle(_translate("MainWindow", "School Name"))
        self.checkbutton.setText(_translate("MainWindow", "Check"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Nº of enrolled students"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Nº of teachers"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Funding Eligibility"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Expenditure in AUD"))
        self.groupBox_7.setTitle(_translate("MainWindow", "ICSEA Score"))

    def popup_close(self, input):
        if input.text() == '&Yes':
            sys.exit(1)
    
    def exit_app(self):
        message = QMessageBox()
        message.setWindowTitle('Avertissement')
        message.setText('Êtes-vous sûr de vouloir quitter ?')
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setDefaultButton(QMessageBox.No)
        message.buttonClicked.connect(self.popup_close)
        x = message.exec_()
    
    def on_click_load_CSV(self):
          

          
        with open("./data.csv") as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')
            for column in readCSV:
                school_name = column[0]
                student_enroll = column[1]
                teaching_staff = column[2]
                ICSEA_score = column[3]
                expenditure = column[4]
                school_names.append(school_name)
                student_enrolls.append(student_enroll)
                teaching_staffs.append(teaching_staff)
                ICSEA_scores.append(ICSEA_score)
                expenditures.append(expenditure)
 
    def closeEvent(self, event):
        self.exit_app()


