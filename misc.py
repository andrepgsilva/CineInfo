import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib.request


def redirect_window(child, name):
    for i in QApplication.topLevelWidgets():
        if i.metaObject().className() == name:
            if child.metaObject().className() == "LoginWindow":
                child.lineEdit.setText("")
                child.lineEdit_2.setText("")
                child.label_4.setText("")
            i.show()
            child.hide()


def change_image(widget, path ,webpath=False):
    if webpath == True:
        web_data = urllib.request.urlopen(path).read()
        image = QImage()
        image.loadFromData(web_data)
        widget.setPixmap(QPixmap(image))
    else:
        widget.setPixmap(QPixmap(path))


def clickable(widget):

    class Filter(QObject):

        clicked = pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
                return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


def change_info(element, widget):
    change_image(widget.info_poster, element.poster, True)
    widget.info_name.setText(element.name)
    widget.info_overview.setText(element.overview)
    widget.info_date_2.setText(element.date)
    widget.info_vote_2.setText(element.vote)


def inc_search(element_value, decrease = False):
    if element_value[0] < 15 and decrease == False:
        element_value[0] += 5
    elif element_value[0] < 15 and element_value[0] > 0 and decrease:
        element_value[0] -= 5
    return element_value[0]
