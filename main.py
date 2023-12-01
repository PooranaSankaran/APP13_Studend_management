from PyQt6.Qtwidgets import (QApplications, QVBoxLayot, QLable, QWidget,
                             QGridLayout, QLineEdit, QPushButton, QMainWindow,QTableWidgetItem,
                             , QDialog, QVBoxLayout, QCoomboBox)
import sys
import sqlite3
class Mainwindow(QMainWindow): #QMainWindow allows us to add menu bar tool bar and staus bar in app
    def __init__(self):
        super().__init__()
        self.setWindowTitle('studend management system')

        #adding file and help menu
        file_menu_item = self.menuBar().addMenu('&File')
        help_menu_item = self.menuBar().addMenu('&Help')

        #add student
        add_student_action = QAction('Add Student',self)
        #add new data in ui for customer
        add_student_action.triggered.connect(self.insert) #we do write code in insert funtion below
        file_menu_item.addAction(add_student_action)

        #about action
        about_action = QAction('About',self)
        help_menu_item.addAction(about_action)
        #about_action.setMenuRole(QAction.MenuRole.NoRole)


        #add table and adding data
        self.table = QTableWidget()
        self.table.setColumnCount(4) # set 4 columns
        self.table.setHorizontalHeaderLable(('ID','Name','Course','Mobile'))# adding columns
        self.setCentralWidget(self.table)


    #adding data
    def load_data(self):
        connection = sqlite3.connect('datbase.db')
        result = connection.execute('SELECT * FROM students')
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):#it has some seperation so we using enumerate
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

class InsertDialog(QDialog): # QDialog eg if user enter phone,course, name the data will add to table that's y v using QDialog
    def __init__(self):
        super().__inti__()
        self.setWindowTitle('Student ManageMEnt System')
        self.setFixedWidth(300)
        set.setFixedHeight(300)

        layout = QVBoxLayout

        #add student new entry in ui
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('name')
        layout.addWidget(self.student_name)

        #add cource
        self.course_name = QCoomboBox()
        courses = ['bio','math','social','phy'] #sudjest student to choose
        self.course_name.addItem(courses)
        layout.addWidget(self.course_name)

        #add mobile widget
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText('Mobile')
        layout.addWidget(self.mobile)

        #add submit button
        button = QPushButton('Register')
        button.clicked.connect(self.add_student) # when user click the button then it start to work on add student funtion

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.cuurentIndex()) #it is combination value that why we using diff funtion
        mobile = self.mobile.text()
        connection = sqlite3.connect('database.db') #connect to database
        cursor = connection.cursor() # curson gonna executue the data base
        cursor.execute('INSERT into students (name, course, mobile) values (?, ? ,?)',
                       (name, course , mobile))
        connection.commit()
        cursor.close()
        connection.close()
        age_calculator.load_data()


app = QApplications(sys.argv)
age_calculator = Mainwindow()
age_calculator.show()
age_calculator.load_data()
sys.exit(app.exec())