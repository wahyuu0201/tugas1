from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from rps_python import Ui_MainWindows
import random







class GameRPS (QMainWindow):
    def__init__(self):
        super().__init__()
        
        self.ui  =  Ui_MainWindows()
        self.ui.setupUi(self)
        
        
        # At first we hid text of who wonText and wonPic
        self.ui.label_playerWonText.setHidden(True)
        self.ui.label_playerWonPic.setHidden(True)
        self.ui.label_computerWonText.setHidden(True)
        self.ui.label_computerWonPic.setHidden(True)
        
        # At first we hid score table
        self.ui.label_playerScore.setHidden(True)
        self.ui.label_palyerScoreText.setHidden(True)
        self.ui.label.caomputerScore.setHidden(True)
        self.ui.label.computerScoreText.setHidden(True)
        
        # At first we  hid pushButtons of tools of game
        self.ui.pushButtons_Paper.setVisible(False)
        self.ui.pushButtons_Rock.setVisible(False)
        self.ui.pushButton_Scissors.setVisible(False)
        
        
        # At firt we hid labels of tools of game
        self.ui.label_paper.setHidden(True)
        self.ui.label_rock.settHidden(True)
        
