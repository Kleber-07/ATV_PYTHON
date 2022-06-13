# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 322)

        MainWindow.setStyleSheet("background-color: rgb(0,255,255); color: rgb(0,0,0)")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(70, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lbl_printar = QtWidgets.QLabel(self.centralwidget)
        self.lbl_printar.setEnabled(True)
        self.lbl_printar.setGeometry(QtCore.QRect(20, 180, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_printar.setFont(font)
        self.lbl_printar.setText("")
        self.lbl_printar.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_printar.setWordWrap(False)
        self.lbl_printar.setObjectName("lbl_printar")

        self.btn_gerar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gerar.setGeometry(QtCore.QRect(100, 250, 111, 31))
        self.btn_gerar.setObjectName("btn_gerar")
        self.btn_gerar.clicked.connect(self.momentos)


        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 281, 124))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.rdb_1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_1.setObjectName("rdb_1")
        self.verticalLayout_2.addWidget(self.rdb_1)

        self.rdb_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_2.setObjectName("rdb_2")
        self.verticalLayout_2.addWidget(self.rdb_2)


        self.rdb_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_3.setObjectName("rdb_3")
        self.verticalLayout_2.addWidget(self.rdb_3)

        self.rdb_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.rdb_4.setObjectName("rdb_4")
        self.verticalLayout_2.addWidget(self.rdb_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Hoje você esta?"))
        self.btn_gerar.setText(_translate("MainWindow", "GERAR"))
        self.rdb_1.setText(_translate("MainWindow", "Tô Bem"))
        self.rdb_2.setText(_translate("MainWindow", "Mais ou menos"))
        self.rdb_3.setText(_translate("MainWindow", "Tô chateado!"))
        self.rdb_4.setText(_translate("MainWindow", "Tô muito chateado!"))

    def momentos(self):
        7
        try:
            if self.rdb_1.isChecked():
                self.lbl_printar.setText(str(random.choice(["Não importa a cor do céu.\n Quem faz o dia bonito é você.", "E que nunca nos falte a\n esperança de dias melhores.","Simplesmente viva a vida!","E que venham novas histórias,\n novos sorrisos e novas pessoas.","Seja otimista. Esta é a melhor\n forma de ver a vida.","Você nasceu para ser feliz,\n não para ser normal.","Pensamento positivo só leva a gente\n pra frente!","Hoje é um bom dia para sorrir!","O segredo é um só: acreditar\n que tudo vai dar certo, porque vai!","Ciclo da vida: tentar,\n cair, levantar, recomeçar.\n Nunca desistir."])))
            elif self.rdb_2.isChecked():
                self.lbl_printar.setText(str(random.choice(["Tudo é possível, mas nem tudo é\n necessário.","Se é pra ter uma crise,\n que seja de riso!", "Seja feliz e não perfeito.","Queira o bem, plante\n o bem e o resto vem!", "Viva simples, sonhe grande,\n seja grato, dê amor, ria muito!","Cair não é ruim quando\n você tem forças para levantar.","Crescer, evoluir e manter as\n bases fortes!","A vida se renova a\n cada amanhecer","Nada é em vão, tudo \n vem pra ensinar.", "Sorte que a vida muda,\n que muita coisa o tempo cura.","A vida é aquilo que você\n deseja diariamente.","Coração em paz floresce\n mesmo sozinho."])))
            elif self.rdb_3.isChecked():
                self.lbl_printar.setText(str(random.choice(["Um pequeno pensamento positivo pela\n manhã pode mudar todo o seu dia.","Acredite. Lute. Conquiste.\n E acima de tudo, seja feliz.","Não deixe que as pessoas te façam\n desistir daquilo que\nvocê mais quer na vida.","Se apaixone por alguém que te\n faça rir dos seus próprios erros","Deixe o seu sorriso\n mudar o mundo","Nunca deixe o mundo mudar o\n seu sorriso.","Não corra atrás de alguém que não\n dá um passo por você.","Não importa o que\n você decidiu. O que importa é que\n isso te faça feliz.","Querer ser outra pessoa é um\n desperdício da pessoa que\n você é."])))

            elif self.rdb_4.isChecked():
                self.lbl_printar.setText(str(random.choice(["Hoje, é dia de se apaixonar…\n Por você, por sua família, por seus\n sonhos, pela vida.","Não deixe que o medo\n de cair te impeça de voar.","Firme na direção das suas metas.\n Porque o pensamento cria,\n o desejo atrai e a fé realiza.","Você é mais forte do\n que imagina. Acredite.","Você não é derrotado quando\n perde. Você é derrotado\n quando desiste.","A vida começa onde termina\n a sua zona de conforto","Quanto mais a gente agradece,\n mais coisas boas acontecem.","Enfrente os problemas\n e leve a melhor!"])))
            else:
                self.lbl_printar.setText(str("Escolha uma opção!"))
        except:
            self.lbl_printar.setText(str("Erro"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
