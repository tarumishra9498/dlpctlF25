from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal

class ClickableLabel(QLabel):
    clicked = Signal(int, int)
    moved = Signal(int, int)
    def mousePressEvent(self, ev):
        super().mousePressEvent(ev)
        x = int(ev.position().x())
        y = int(ev.position().y())
        self.clicked.emit(x, y)
    def mouseMoveEvent(self, ev):
        super().mouseMoveEvent(ev)
        x = int(ev.position().x())
        y = int(ev.position().y())
        self.moved.emit(x, y)