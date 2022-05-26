from click import password_option
from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="Felipe",
    passwd="",
    database="cadastro_produtos"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3text()
    
    categoria =""
    
    if formulario.radioButton.isChecked():
        print("Categoria Informatica foi selecionado")
        categoria="Eletronicos"
    elif formulario.radioButton_2.isChecked():
        print("Catrgoria Aliementos foi selecionado")
        categoria="Informatica"
    else :
        print("Categoria Eletronicos foi selecionado")
        categoria="Alimentos"
    print("Codigo", linha1)
    print("Descrição", linha2)
    print("Preço", linha3)
    cursor =banco.cursor()
    comando_SQL ="INSERT INTO produtos(codigo,descricao,preco,categoria) VALUES(%s,%s,%s,%s)"
    dados =(str(linha1),str(linha2),str(linha3),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    
    
    
    
    app=QtWidgets.QApplication([])
    formulario=uic.loadUi("formulario.ui")
    formulario.pushButton.clicked.connect(funcao_principal)
    
    formulario.show()
    app.exec()
    
    create table produtos(
    id INT NOT NULL AUTO_INCREMENT, 
    codigo INT,
    descricao VARCHAR(50),
    preco DOUBLE , 
    categoria VARCHAR (20),
    PRIMARY KEY(ID)
    );
    
    INSERT INFO produtos(codigo,descricao,preco,categoria)  values(123,"impressora",500.00,"informatica");
    