import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from itertools import takewhile
import re

form_class = uic.loadUiType("text_editor.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10

        # TextEdit과 관련된 버튼에 기능 연결
        self.pushButton.clicked.connect(self.click_button)

    def build_tree(self, lines):
        is_tab = '\t'.__eq__
        lines = iter(lines)
        stack = []
        result = []
        for line in lines:
            if line == "#--------------------------------------------------":
                result.append(line + '\n')
                continue
            elif bool(re.match(r"(^echo)", line)):
                result.append(line + '\n')
                continue
            else:
                indent = len(list(takewhile(is_tab, line)))
                stack[indent:] = [line.lstrip()]
                result.append(' '.join(stack) + '\n')
        return result

    def click_button(self):
        source = self.textEdit.toPlainText()
        result = "".join(self.build_tree(source.split('\n')))
        self.textEdit_2.setText(result)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()