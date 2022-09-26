from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
from mpl_toolkits.mplot3d import axes3d

def f(z, r):
    return ((1*r/(2))*((z)/(z**2 + r**2)**(3/2)-(z-1)/((z-1)**2 + r**2)**(3/2)))

zt = np.arange(-3.0, 3.0, 0.01)
rt = np.arange(0.1, 1, 0.1)

X, Y = np.meshgrid(zt, rt)
Z = f(X, Y)

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(projection='3d')
        super(MplCanvas, self).__init__(fig)

class Ui_ThreeDPlot(object):
    def setupUi(self, ThreeDPlot):
        ThreeDPlot.setObjectName("ThreeDPlot")
        ThreeDPlot.resize(800, 600)

        layout = QtWidgets.QVBoxLayout()
        sc = MplCanvas(self, width=5, height=5, dpi=100) # Create a built in canvas to do plotting
        sc.ax.plot_surface(X,Y,Z, rstride=2, cstride=2, cmap='plasma', edgecolor='none')
        sc.ax.view_init(35, 75)

        sc.ax.set_xlabel('$z$', fontsize=20)
        sc.ax.set_ylabel('$r$', fontsize=20)
        sc.ax.set_zlabel('$Ez$', fontsize=20)
        
        sc.ax.set_title("3D Surface Plot of Electric Field at Varying z and r Values\nWhere h = 1, lambda = 1, and Epsilon Naught = 1", fontsize=15)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, ThreeDPlot)

        layout.addWidget(toolbar) # Add the canvas and toolbar to the layout
        layout.addWidget(sc)
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(layout)
        ThreeDPlot.setCentralWidget(self.widget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThreeDPlot = QtWidgets.QMainWindow()
    ui = Ui_ThreeDPlot()
    ui.setupUi(ThreeDPlot)
    ThreeDPlot.show()
    sys.exit(app.exec_())
