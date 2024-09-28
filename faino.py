from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QMessageBox

app = QApplication([])

main_window = QWidget()
main_window.setGeometry(100, 100, 200, 200)  # Збільшено розмір для зручності

text = QLabel("Яка столиця України?")

btn_answer1 = QRadioButton("Коломия")
btn_answer2 = QRadioButton("Київ")
btn_answer3 = QRadioButton("Харків")
btn_answer4 = QRadioButton("П'ядики")

boom_chek = QPushButton("Перевірити")

# Додаємо горизонтальні макети до вертикального макета
v_layout = QVBoxLayout()
h_layout1 = QHBoxLayout()
h_layout2 = QHBoxLayout()


# Додаємо кнопку перевірки під варіантами відповідей
v_layout.addWidget(text)


h_layout1.addWidget(btn_answer1)
h_layout1.addWidget(btn_answer2)
h_layout2.addWidget(btn_answer3)
h_layout2.addWidget(btn_answer4)

v_layout.addLayout(h_layout1)
v_layout.addLayout(h_layout2)
v_layout.addWidget(boom_chek)


main_window.setLayout(v_layout)

def show_win():
    victory = QMessageBox()
    victory.setText("Все вірно П'ядики - це столиця України")
    victory.exec() 


def click():
    if btn_answer4.isChecked():
        show_win()

boom_chek.clicked.connect(click)


main_window.show()
app.exec()
