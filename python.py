from PyQt6.QtWidgets import QWidget, QApplication,QPushButton, QLabel, QLabel, QVBoxLayout,QLineEdit
from PyQt6.QtCore import Qt
import random

app = QApplication([])

main_window = QWidget()
main_window.setGeometry(100,100,200,200)
main_window.show()

button = QPushButton("Натисни")
label = QLabel("текст")
layout = QVBoxLayout()
line1 = QLineEdit()
line2 = QLineEdit()
label.setAlignment(Qt.AlignmentFlag.AlignCenter)

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(line1)
layout.addWidget(line2)
main_window.setLayout(layout)

def click_button():
    n1 = line1.text()
    n2 = line2.text()
    try:
        n = random.randint(int(n1),int(n2))
        label.setText(str(n))
    except:
        label.setText("ПОМИЛКА")

button.clicked.connect(click_button)
app.exec()