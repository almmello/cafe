import sys
import ctypes
from PyQt5 import QtWidgets

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip('Caffeine is OFF')
        menu = QtWidgets.QMenu(parent)
        switch_on = menu.addAction("Switch On")
        switch_off = menu.addAction("Switch Off")
        exit_ = menu.addAction("Exit")
        self.setContextMenu(menu)
        switch_on.triggered.connect(self.switch_on)
        switch_off.triggered.connect(self.switch_off)
        exit_.triggered.connect(lambda: sys.exit())
        self.activated.connect(self.onTrayIconActivated)

    def switch_on(self):
        self.setIcon(QtWidgets.QStyle.SP_DriveHDIcon) # Example of system-provided icon
        self.setToolTip("Caffeine is ON")
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

    def switch_off(self):
        self.setIcon(QtWidgets.QStyle.SP_DriveCDIcon) # Example of system-provided icon
        self.setToolTip("Caffeine is OFF")
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS)

    def onTrayIconActivated(self, reason):
        if reason == self.DoubleClick:
            self.showMessage(
                "System Tray",
                "Double click detected!",
                QtWidgets.QSystemTrayIcon.Information,
                2000
            )

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtWidgets.QStyle.SP_DriveCDIcon, w) # Example of system-provided icon
    tray_icon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
