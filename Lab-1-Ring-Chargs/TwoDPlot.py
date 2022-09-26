from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
from mpl_toolkits.mplot3d import axes3d

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

class Ui_TwoDPlot(object):
    def f(self, z, r):
            return ((1*r/(2))*((z)/(z**2 + r**2)**(3/2)-(z-1)/((z-1)**2 + r**2)**(3/2)))
    def redrawFigure(self):
            self.sc.ax.cla()
            self.sc.ax.plot(self.zt, self.f(self.zt, self.r), 'r-')
            self.sc.ax.set_title("2D Plot of the Electric Field with Varying Z\nWhere r = {}, h = 1, lambda = 1, and Epsilon Naught = 1".format(self.r), fontsize=15)
            self.sc.draw()

    def setupUi(self, TwoDPlot):
        self.r = 1
        self.zt = np.arange(-3.0, 3.0, 0.01)
        self.layout = QtWidgets.QVBoxLayout()
        self.sc = MplCanvas(self, width=5, height=5, dpi=100) # Create a built in canvas to do plotting
        self.sc.ax.plot(self.zt, self.f(self.zt, self.r))
        self.sc.ax.grid()

        self.sc.ax.set_xlabel('$z$', fontsize=10)
        self.sc.ax.set_ylabel('$Ez$', fontsize=10)
        
        self.sc.ax.set_title("2D Plot of the Electric Field with Varying Z\nWhere r = {}, h = 1, lambda = 1, and Epsilon Naught = 1".format(self.r), fontsize=15)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.toolbar = NavigationToolbar(self.sc, TwoDPlot)

        self.layout.addWidget(self.toolbar) # Add the canvas and toolbar to the layout
        self.layout.addWidget(self.sc)
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.layout)
        TwoDPlot.setCentralWidget(self.widget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TwoDPlot = QtWidgets.QMainWindow()
    ui = Ui_TwoDPlot()
    ui.setupUi(TwoDPlot)
    TwoDPlot.show()
    sys.exit(app.exec_())
