import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt, QPoint
from PIL import Image

start_pos = None
end_pos = None

class SelectionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setWindowOpacity(0.1) 
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QColor(0, 0, 0), 1, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(128, 128, 128, 128)))
        
        if start_pos and end_pos:
            painter.drawRect(start_pos.x(), start_pos.y(), end_pos.x() - start_pos.x(), end_pos.y() - start_pos.y())
    
    def mousePressEvent(self, event):
        global start_pos, end_pos
        start_pos = event.pos()
    
    def mouseMoveEvent(self, event):
        global start_pos, end_pos
        end_pos = event.pos()
        self.update()
    
    def mouseReleaseEvent(self, event):
        global start_pos, end_pos
        end_pos = event.pos()
        
        
        self.hide()
        
        # Get the selected area coordinates
        x = min(start_pos.x(), end_pos.x())
        y = min(start_pos.y(), end_pos.y())
        width = abs(end_pos.x() - start_pos.x())
        height = abs(end_pos.y() - start_pos.y())
        
        
        screenshot = QApplication.primaryScreen().grabWindow(0)
        
        
        selected_area = screenshot.copy(x, y, width, height)
        
        
        selected_area.save('screenshot.png', 'PNG')
        print("Screenshot saved as 'screenshot.png'")
        
       
        self.show()
        
        self.close()

def select_area_screenshot():
    app = QApplication(sys.argv)
    selection_widget = SelectionWidget()
    selection_widget.showFullScreen()
    sys.exit(app.exec_())


select_area_screenshot()
