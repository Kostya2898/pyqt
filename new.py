from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout,QListWidget,QLineEdit

def window_b():
    text = ander.text()
    ander1.addItem(text)
    window.hide()
    window2.show()
def window_a():
    window2.hide()
    window.show()



app = QApplication([])

window = QWidget()
label = QLabel("Window A")
ander1 = QListWidget()
ander = QLineEdit()
button = QPushButton("Перейти на вікно B")
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(ander)
window.setLayout(layout)

window2 = QWidget()
label2 = QLabel("Window B")
button2 = QPushButton("Перейти на вікно A")
layout2 = QVBoxLayout()
layout2.addWidget(label2)
layout2.addWidget(button2)
layout2.addWidget(ander1)
window2.setLayout(layout2)
window2.hide()


button.clicked.connect(window_b)
button2.clicked.connect(window_a)

window.show()
app.exec()
