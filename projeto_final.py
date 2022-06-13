# -*- coding: utf-8 -*-
import sys

import PySide2
import mysql.connector
import time
import os

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QMainWindow, QDialog
from PySide2.QtCore import QFile
from PySide2 import QtGui
from PySide2 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets

########################banco de dados ###############################################
meu_db = ("new_eletronica", )


def conecta_db(db=None):
    if db == None:
        banco = mysql.connector.connect(host="localhost", user="root", passwd="")
        return banco
    else:
        banco = mysql.connector.connect(host="localhost", user="root", passwd="", database=db)
        return banco


def existe_db():
    status = False
    try:
        db = conecta_db()
        cursor = db.cursor()

        cursor.execute("SHOW DATABASES")

        for banco in cursor:
            if banco == meu_db:
                status = True

        cursor.close()
        db.close()


    except BaseException as erro:
        print("erro ao testa banco" + str(erro))
    return status


def criar_db():

    print("=" * 45)
    print("Bem Vindo ao Banco de Dados.")
    time.sleep(2)
    print("configurando o sistema. por favor, aguarde!")
    print("=" * 45)
    time.sleep(5)
    os.system("cls")
    try:  # try sempre tera esse padrão
        db = conecta_db()
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE " + meu_db[0])
        print("CREATED SUCCESS !!")
        cursor.close()
        db.close()
        criar_tabelas()

    except BaseException as erro:  # Sempre que usar o try:
        print("Erro na criação do banco." + str(erro))


def criar_tabelas():
    try:
        db = conecta_db(meu_db[0])
        cursor = db.cursor()

        sql = "CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, usuario VARCHAR(20), passwd VARCHAR (10))"
        cursor.execute(sql)

        sql = "CREATE TABLE produtos (id INT AUTO_INCREMENT PRIMARY KEY, codigo VARCHAR(255), fornecedor VARCHAR (255), nome VARCHAR (255), detalhes VARCHAR (255), preço VARCHAR (255), UNIQUE(codigo) )"
        cursor.execute(sql)

        sql = "INSERT INTO usuarios (usuario, passwd) VALUES (%s, %s)"
        val = ("admin", "admin")
        cursor.execute(sql, val)

        db.commit()
        cursor.close()
        db.close()
        print("=" * 45)
        print("Criando Tabela, por favor aguarde!")
        time.sleep(3)
        print("=" * 45)
        print("Tabela criada com sucesso. !!")
    except BaseException as erro:
        print("Erro ao criar as tabelas." + str(erro))




def cadastra_cliente():
    c = cad.lineEdit_codigo.text()
    f = cad.lineEdit_fornecedor.text()
    n = cad.lineEdit_nome.text()
    d = cad.lineEdit_detalhes.text()
    p = cad.lineEdit_preco.text()
    #q = *True*
    try:
        db = conecta_db(meu_db[0])  # conecta faz o especifico fecha a conexão e cria o cursor
        cursor = db.cursor()  # tem que ter ()
        sql = "SELECT * FROM produtos WHERE codigo LIKE '%" + c + "%'"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if c == "" and f == "" and n == "" and d == "" and p == "": #and q == "":
            carregar_janela_erro()

        elif c == resultado :
            carregar_janela_erro()
        elif len(c) > 0 and len(f) >= 0 and len(n) > 0 and len(d) >= 0 and len(p) >= 0 :
            sql = "INSERT  INTO  produtos (codigo, fornecedor, nome, detalhes, preço) VALUES (%s, %s, %s, %s, %s)"  # mysql entrando no codigo
            val = (c, f, n, d, p)
            cursor.execute(sql, val)
            db.commit()
            carregar_janela_ok()
        else:
            carregar_janela_erro()



    except BaseException as erro:
        carregar_janela_erro_codigo()


    finally:
        cursor.close()
        db.close()


def editar_cliente():
    b = edit.lineEdit_pesqEDITAR.text()

    try:
        db = conecta_db(meu_db[0])
        cursor = db.cursor()
        sql = "SELECT DISTINCT * FROM produtos WHERE codigo LIKE '%" + b + "%'"

        cursor.execute(sql)
        resultado = cursor.fetchall()

        if b == "":
            carregar_janela_erro()
        else:
            for x in resultado:
                edit.label_codED.setText(str(x[1]))
                edit.label_fornED.setText(str(x[2]))
                edit.label_nomeED.setText(str(x[3]))
                edit.label_detED.setText(str(x[4]))
                edit.label_precED.setText(str(x[5]))
            if not x in resultado:
                carregar_janela_erro()
    except BaseException as erro:
        carregar_janela_erro()
    finally:
        cursor.close()
        db.close()

def mudar():
    b = edit.lineEdit_pesqEDITAR.text()

    try:
        db = conecta_db(meu_db[0])
        cursor = db.cursor()

        sql = "SELECT * FROM produtos WHERE codigo LIKE '%" + b + "%'"

        cursor.execute(sql)
        resultado = cursor.fetchall()
        if b == "":
            carregar_janela_erro()
        else:

            for x in resultado:
                codigo =  edit.lineEdit_codNOVO.text()
                fornecedor = edit.lineEdit_fornNOVO.text()
                nome = edit.lineEdit_nomeNOVO.text()
                detalhes  = edit.lineEdit_detNOVO.text()
                preco = edit.lineEdit_precNOVO.text()

        if len(codigo) == 0 and len(fornecedor) == 0 and len(nome) == 0 and len(detalhes) == 0 and len(preco) == 0:
            carregar_janela_erro()
        if len(codigo) > 0 and len(fornecedor) > 0 and len(nome) > 0 and len(detalhes) > 0and len(preco) > 0:

            sql = "UPDATE produtos SET codigo = %s, fornecedor = %s, nome = %s, detalhes = %s, preço = %s WHERE produtos.id = " + str(x[0])
            val = (codigo, fornecedor, nome, detalhes, preco)
            cursor.execute(sql, val)
            db.commit()
            print("Dados alterados com sucesso")
            carregar_janela_ok()
        if b == "":
            carregar_janela_erro()


        elif len(codigo) > 0 and len(fornecedor) >= 0 and len(nome) >= 0 and len(detalhes) >= 0 and len(preco) >= 0:
            sql = "UPDATE produtos SET codigo = %s WHERE produtos.id = " + str(x[0])
            val = (codigo,)
            cursor.execute(sql, val)
            db.commit()
            print("Dados alterados com sucesso")
            carregar_janela_ok()

        elif len(codigo) >= 0 and len(fornecedor) > 0 and len(nome) >= 0 and len(detalhes) >= 0 and len(preco) >= 0:
            sql = "UPDATE produtos SET fornecedor = %s WHERE produtos.id = " + str(x[0])
            val = (fornecedor,)
            cursor.execute(sql, val)
            db.commit()
            print("Dados alterados com sucesso")
            carregar_janela_ok()

        elif len(codigo) >= 0 and len(fornecedor) >= 0 and len(nome) > 0 and len(detalhes) >= 0 and len(preco) >= 0:
            sql = "UPDATE produtos SET nome = %s WHERE produtos.id = " + str(x[0])
            val = (nome,)
            cursor.execute(sql, val)
            db.commit()
            print("Dados alterados com sucesso")
            carregar_janela_ok()

        elif len(codigo) >= 0 and len(fornecedor) >= 0 and len(nome) >= 0 and len(detalhes) > 0 and len(preco) >= 0:
            sql = "UPDATE produtos SET detalhes = %s WHERE produtos.id = " + str(x[0])
            val = (detalhes,)
            cursor.execute(sql, val)
            db.commit()
            print("Dados alterados com sucesso")
            carregar_janela_ok()

        elif len(codigo) >= 0 and len(fornecedor) >= 0 and len(nome) >= 0 and len(detalhes) >= 0 and len(preco) > 0:
            sql = "UPDATE produtos SET preço = %s WHERE produtos.id = " + str(x[0])
            val = (preco,)
            cursor.execute(sql, val)
            db.commit()
            print("Dados alterados com sucesso")
            carregar_janela_ok()

    except BaseException as erro:
        carregar_janela_erro()
        print("Erro ao editar cliente..." + str(erro))
    finally:
        cursor.close()
        db.close()


def pesquisar_cliente():
    a = remove.lineEdit_pesquisar.text()
    try:

        db = conecta_db(meu_db[0])
        cursor = db.cursor()
        if len(a) >= 2:
            sql = "SELECT * FROM produtos WHERE codigo LIKE '%" + a + "%'"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            for x in resultado:
                remove.label_codigo.setText(str(x[1]))
                remove.label_fornecedor.setText(str(x[2]))
                remove.label_nome.setText(str(x[3]))
                remove.label_detalhes.setText(str(x[4]))
                remove.label_preco.setText(str(x[5]))
            if not x in resultado:
                carregar_janela_erro()

        else:
            carregar_janela_erro()
    except BaseException as erro:
        carregar_janela_erro()
    finally:
        cursor.close()
        db.close()


def excluir_produtos():
    try:
        db = conecta_db(meu_db[0])
        cursor = db.cursor()
        a = True
        ab = remove.lineEdit_pesquisar.text()
        if ab =="" :
            a = False
        if a == True:
            sql = 'SELECT * FROM produtos WHERE codigo = %s'
            val = (ab,)
            cursor.execute(sql, val)
            resultado = str(cursor.fetchall())
            if ab in resultado:
                sql = "DELETE FROM produtos WHERE produtos.codigo = %s "
                val=(ab,)
                cursor.execute(sql,val)
                db.commit()
                carregar_janela_ok()
        else:
          carregar_janela_erro()




        #sql = f"DELETE FROM produtos WHERE produtos.id = {str(a[0])}"

        #cursor.execute(sql)
        #db.commit()

    except BaseException as erro:
        carregar_janela_erro()


    finally:
        cursor.close()
        db.close()




########################banco de dados ###############################################


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 322)
        Dialog.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password.setGeometry(QtCore.QRect(150, 160, 161, 31))
        self.lineEdit_password.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                             "background-color: rgb(53, 53, 53);")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_username = QtWidgets.QLabel(Dialog)
        self.label_username.setGeometry(QtCore.QRect(70, 110, 71, 20))
        self.label_username.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                          "font: 75 11pt \"MS Shell Dlg 2\";\n"
                                          "font: 8pt \"MS Shell Dlg 2\";")
        self.label_username.setAlignment(QtCore.Qt.AlignCenter)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(Dialog)
        self.label_password.setGeometry(QtCore.QRect(70, 170, 71, 20))
        self.label_password.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_password.setAlignment(QtCore.Qt.AlignCenter)
        self.label_password.setObjectName("label_password")
        self.pushButton_login = QtWidgets.QPushButton(Dialog)
        self.pushButton_login.setGeometry(QtCore.QRect(70, 230, 75, 23))
        self.pushButton_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../login-icon-png-0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_login.setIcon(icon)
        self.pushButton_login.setObjectName("pushButton_login")

        self.pushButton_singup = QtWidgets.QPushButton(Dialog)
        self.pushButton_singup.setGeometry(QtCore.QRect(250, 230, 75, 23))
        self.pushButton_singup.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../signup-icon-29.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_singup.setIcon(icon1)
        self.pushButton_singup.setObjectName("pushButton_singup")

        self.lineEdit_password_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password_2.setGeometry(QtCore.QRect(150, 100, 161, 31))
        self.lineEdit_password_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                               "background-color: rgb(53, 53, 53);")
        self.lineEdit_password_2.setObjectName("lineEdit_password_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 10, 81, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../login-icon-png-0.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")


def exibir_produto():
    try:

        db = conecta_db(meu_db[0])
        cursor = db.cursor()

        sql = "SELECT * FROM produtos"
        cursor.execute(sql)
        resultado = cursor.fetchall()

        prod.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate (resultado):
          prod.tableWidget.insertRow(row_number)
          for column_number, data in enumerate (row_data):
                prod.tableWidget.setItem(row_number, column_number, PySide2.QtWidgets.QTableWidgetItem(str(data)))

        #prod.textBrowser.setText(resultado)

    except BaseException as erro:
        print("Erro exibindo cliente.", str(erro))
        cursor.close()
        db.close()


def verificar():
    a = Dialog.lineEdit_password_2.text()
    b = Dialog.lineEdit_password.text()
    try:
        db = conecta_db(meu_db[0])
        cursor = db.cursor()  # cursor precisara de "()"

        cursor.execute("SELECT count(*) FROM usuarios")  # cONTA TODOS OS USUARIOS

        resultado = cursor.fetchone()

        c = False
        d = False

        if resultado[0] == 1:  # se so tiver um, so tera um admin
            sql = "SELECT * FROM usuarios"
            cursor.execute(sql)
            valor = cursor.fetchone()
            if a == valor[1]:
                c = True
                print(valor[1], "login")
            if b == valor[2]:
                d = True
                print(valor[2], "senha")
        if c and d == True:
            Dialog.close()
            carregar_janela_menu()

        else:
            carregar_janela_erro()
    except BaseException as erro:  # sempre que tiver o try tera o except
        print("Erro ao criar usuario." + str(erro))
    finally:
        cursor.close()
        db.close()


Dialog = None


class carrega_menu():
    janela = None

    def __init__(self):
        global janela
        self.jan = QtWidgets.qApp
        self.arquivo = QFile("menu.ui")
        self.arquivo.open(QFile.ReadOnly)

        self.carrega = QUiLoader()
        janela = self.carrega.load(self.arquivo)
        self.arquivo.close()
        janela.show()

        janela.pushButton_cadrastar2.clicked.connect(carregar_janela_cadastro)
        janela.pushButton_imprimir.clicked.connect(carregar_janela_produtos)
        janela.pushButton_remover.clicked.connect(carrega_remover)
        janela.pushButton_editar.clicked.connect(carregar_janela_editar)

def carregar_janela_menu():
    Dialog.close()
    j = carrega_menu()


Dialog = None



##################cadastro####################
class carrega_cadastro2():
    cad = None

    def __init__(self):
        global cad
        self.jan = QtWidgets.qApp
        self.arquivo = QFile("cadastro_produtos.ui")
        self.arquivo.open(QFile.ReadOnly)

        self.carrega = QUiLoader()
        cad = self.carrega.load(self.arquivo)

        self.arquivo.close()
        cad.show()
        cad.pushButton_cadastrarprod.clicked.connect(cadastra_cliente)


def carregar_janela_cadastro():
    j = carrega_cadastro2()


Dialog = None


##################cadastro####################
class carrega_remover():
    remove = None

    def __init__(self):
        global remove
        self.jan = QtWidgets.qApp
        self.arquivo = QFile("remover.ui")
        self.arquivo.open(QFile.ReadOnly)

        self.carrega = QUiLoader()
        remove = self.carrega.load(self.arquivo)

        self.arquivo.close()
        remove.show()
        remove.pushButton_pesquisar.clicked.connect(pesquisar_cliente)
        remove.pushButton_excluir.clicked.connect(excluir_produtos)


def carregar_janela_remover():
    Dialog.close()
    j = carrega_remover()


Dialog = None


##################produto####################
class carrega_produtos():
    prod = None

    def __init__(self):
        global prod
        self.jan = QtWidgets.qApp
        self.arquivo = QFile("carregar_produto.ui")
        self.arquivo.open(QFile.ReadOnly)

        self.carrega = QUiLoader()
        prod = self.carrega.load(self.arquivo)

        self.arquivo.close()
        prod.show()
        prod.pushButton.clicked.connect(exibir_produto)


def carregar_janela_produtos():
    j = carrega_produtos()

##################editar_produto####################
class carrega_editar():
    edit = None
    def __init__(self):
        global edit
        self.jan = QtWidgets.qApp
        self.arquivo = QFile("editar_produto.ui")
        self.arquivo.open(QFile.ReadOnly)

        self.carrega = QUiLoader()
        edit = self.carrega.load(self.arquivo)

        self.arquivo.close()
        edit.show()
        edit.pushButton_pesqEDITAR.clicked.connect(editar_cliente)
        edit.pushButton_editprodNOVO.clicked.connect(mudar)



def carregar_janela_editar():
    a = carrega_editar()

class carrega_erro():
    stop = None

    def __init__(self):
        global stop
        self.jan = QtWidgets.qApp
        self.arquivo = QFile("msg_erro.ui")
        self.arquivo.open(QFile.ReadOnly)

        self.carrega = QUiLoader()
        stop = self.carrega.load(self.arquivo)

        self.arquivo.close()
        stop.show()


def carregar_janela_erro():
    j = carrega_erro()


class carrega_erro_codigo():
    stop = None

    def __init__(self):
        global stop
        self.jan = QtWidgets.qApp
        self.arquivo = QFile("msg_erro_editar.ui")
        self.arquivo.open(QFile.ReadOnly)

        self.carrega = QUiLoader()
        stop = self.carrega.load(self.arquivo)

        self.arquivo.close()
        stop.show()


def carregar_janela_erro_codigo():
    j = carrega_erro_codigo()





class carrega_aprovado():
    ok = None

    def __init__(self):
        global ok
        self.jan = QtWidgets.qApp
        self.arquivo = QFile("msg_ok.ui")
        self.arquivo.open(QFile.ReadOnly)

        self.carrega = QUiLoader()
        ok = self.carrega.load(self.arquivo)

        ok.show()
        self.arquivo.close()




def carregar_janela_ok():
    j = carrega_aprovado()








if __name__ == "__main__":

    if not existe_db():
        criar_db()

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui_file = QFile("login.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()

    Dialog = loader.load(ui_file)
    Dialog.pushButton_login.clicked.connect(verificar)
    ui_file.close()
    Dialog.show()
    sys.exit(app.exec_())
