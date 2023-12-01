from PyQt6.Qtwidgets import (QApplications, QVBoxLayot, QLable, QWidget,
                             QGridLayout, QLineEdit, QPushButton)
import sys

from datetime import datetime
class AgeCalculator(QWidget):
    def __init__(self): #Qwidget has own init method so, we need to use super to call and use child init method
        super().__init__() # return partent of the called is QWidget
        self.setWindowTitle('Age calculator') # it will set title
        grid = QGridLayout()

        # use used self beacuse we using date_birth_line_edit in anothe close we it to instant variable to use it in another class
        name_lable = QLable('Name:') #name lable
        self.name_line_edit = QLineEdit() # edit lable eg: entering your name box


        date_birth_lable = QLable('Date of birth mm/dd/yyy')# brith lable
        self.date_birth_line_edit = QLineEdit()#enter edit box or called as insert box of your birth
        # use used self beacuse we using date_birth_line_edit in anothe close we it to instant variable to use it in another class
        #add calculate buttoon

        calculate_button = QPushButton('calculate Age') # it will add button
        calculate_button.clicked.connect(self.calculate_age) # after click the button it have to call calculate_age funtion
        self.output_lable = QLable('')

        grid.addWidget(name_lable,0 ,0) #0 row
        grid.addWidget(self.name_line_edit, 0, 1) # 0 row next to above
        grid.addWidget(date_birth_lable,1 ,0)# next row
        grid.addWidget(self.date_birth_line_edit, 1, 1)# next row next to it
        grid.addWidget(calculate_button, 2, 0,1,2) #last 1,2 is 1 row for 2 columns
        grid.addWidget(self.output_lable, 3, 0, 1, 2)


        self.setLayout(grid)
    def calculate_age(self):
        current_year = datetime.now().year # current yr - the date user enters
        date_of_birth = self.date_birth_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, '%m/%d/%Y').date().year
        age = current_year - year_of_birth
        self.output_lable.setText(f'{self.name_line_edit} is {age} year')

app = QApplications(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
