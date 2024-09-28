import sys
import json
import os
from PyQt6.QtWidgets import QInputDialog, QMessageBox, QApplication, QMainWindow
from ui import Ui_MainWindow  

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.notes = {}

        self.load_notes()

        self.pushButton.clicked.connect(self.add_note)
        self.pushButton_2.clicked.connect(self.del_note)
        self.pushButton_3.clicked.connect(self.save_note)


        self.listWidget.itemClicked.connect(self.show_note) 

 
    def load_notes(self):
        if os.path.exists("notes_data.json"):
            
            with open("notes_data.json", "r", encoding="utf-8") as file: 
                self.notes = json.load(file)  
            self.listWidget.addItems(self.notes.keys())  
        else:
            QMessageBox.warning(self, "Помилка", "відсутні файли notes_data.json")
            
    def add_note(self):
        note_name, ok = QInputDialog.getText(self, "Додати замітку", "Назва замітки: ")
        if ok and note_name != "":
            if note_name not in self.notes:
                self.notes[note_name] = {"текст": "", "теги": []}
                self.listWidget.addItem(note_name)  
            else:
                QMessageBox.warning(self, "Помилка", "Замітки не існує")

        else:
            QMessageBox.warning(self, "Помилка", "Замітка не може бути пророжньою") 
         

    def show_note(self):
        if self.listWidget.selectedItems():
            key = self.listWidget.selectedItems()[0].text()
            self.textEdit.setText(self.notes[key]["текст"])  
            self.listWidget_2.clear()
            self.listWidget_2.addItems(self.notes[key]["теги"])  
        else:
            QMessageBox.warning(self, "Помилка", "вибраної замітки немає") 
            

    def save_note(self):
        if self.listWidget.selectedItems():
            key = self.listWidget.selectedItems()[0].text()
            self.notes[key]["текст"] = self.textEdit.toPlainText() 
            with open("notes_data.json", "w", encoding="utf-8") as file:
                json.dump(self.notes, file, sort_keys=True, ensure_ascii=False, indent=4)
        else:
            QMessageBox.warning(self, "Помилка", "замітка для збереження не обрана")
         


    def del_note(self):
        if self.listWidget.selectedItems():
            key = self.listWidget.selectedItems()[0].text()
            del self.notes[key] 
            self.listWidget.clear()
            self.textEdit.clear()
            self.listWidget.addItems(self.notes.keys())  
            with open("notes_data.json", "w", encoding="utf-8") as file:
                json.dump("MainWindow", file)

        else:
            QMessageBox.warning(self, "Помилка", "замітка для видалення не обрана")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
