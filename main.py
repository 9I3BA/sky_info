import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from info import load_city, save_city, get_weather, FILENAME

class Welcome_window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/welcome.ui", self)
        self.save_city_btn.clicked.connect(self.save)

    def save(self):
        city = self.line_inp_city.text().strip()

        if not city:
            QMessageBox.warning(self, "Ошибка", "Введите название города")
            return

        save_city(city)

        self.main_win = Main_window()
        self.main_win.show()
        self.close()

class Main_window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main.ui", self)
        self.update_weather()
        self.settings_btn.clicked.connect(self.settings)
    def update_weather(self):
        city = load_city()
        if not city:
            QMessageBox.warning(self, "Ошибка", "Город не найден")
            return

        result = get_weather(city)

        if result["ok"]:
            self.label_city_name.setText(result["city"])
            self.description_label.setText(result["description"].capitalize())
            self.temperature_label.setText(f"{result['temp']}°C (ощущается как {result['feels_like']}°C)")
        else:
            QMessageBox.critical(self, "Ошибка", result["error"])
    def settings(self):
        self.settings_win = Settings_window()
        self.settings_win.show()
        self.close()
class Settings_window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/settings.ui", self)

        self.edit_city_btn.clicked.connect(self.edit_city)
        self.back_btn.clicked.connect(self.back)
        self.language_btn.clicked.connect(self.language)

    def edit_city(self):
        self.welcome_window = Welcome_window()
        self.welcome_window.show()
        self.close()

    def language(self):
        QMessageBox.information(self, "Massage", "LEARN RUSSIAN, WHY DO I UNDERSTAND YOU BUT YOU DON'T?")

    def back(self):
        self.main_win = Main_window()
        self.main_win.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        window = Welcome_window()
    else:
        window = Main_window()

    window.show()
    sys.exit(app.exec())