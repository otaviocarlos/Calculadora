import wx
import numpy as np 
from math import *
from classe_matriz import Matriz
from classe_vtk import VtkClasse

class Calculadora(wx.Frame):
	def __init__(self, *args,**kwargs): #args e kwargs são usados para receber multiplos parâmetros
		super(Calculadora,self).__init__(*args,**kwargs)
		self.resultado = 0
		self.memoria = 0
		self.frmCalc()
		#Caixa de texto:
		self.text = wx.TextCtrl(self,size=(354,45),pos=(5,5))

	def frmCalc(self):
		self.CreateStatusBar()
		self.SetStatusText('Calculadora')

		#criando componente Panel:
		panel = wx.Panel(self)#Associa o panel ao frame criado

		#Elementos da parte gráfica:
		
		#Quarta Linha
		posy=60+3*40
		wx.Button(panel,0,'0',size=(40,40),pos=(10,posy))
		wx.Button(panel,110,'.',size=(40,40),pos=(50,posy))
		wx.Button(panel,111,'+-',size=(40,40),pos=(90,posy))
		wx.Button(panel,127,',',size=(40,40),pos=(140,posy))
		wx.Button(panel,128,'=',size=(40,40),pos=(180,posy))
		wx.Button(panel,129,'%',size=(40,40),pos=(270,posy))
		wx.Button(panel,130,'MC',size=(40,40),pos=(310,posy))

		#Terceira Linha
		posy=60+2*40
		wx.Button(panel,1,'1',size=(40,40),pos=(10,posy))
		wx.Button(panel,2,'2',size=(40,40),pos=(50,posy))
		wx.Button(panel,3,'3',size=(40,40),pos=(90,posy))
		wx.Button(panel,122,'(',size=(40,40),pos=(140,posy))
		wx.Button(panel,123,')',size=(40,40),pos=(180,posy))
		wx.Button(panel,125,'x^y',size=(40,40),pos=(270,posy))
		wx.Button(panel,126,'M-',size=(40,40),pos=(310,posy))

		
		#Segunda Linha
		posy=60+40
		wx.Button(panel,4,'4',size=(40,40),pos=(10,posy))
		wx.Button(panel,5,'5',size=(40,40),pos=(50,posy))
		wx.Button(panel,6,'6',size=(40,40),pos=(90,posy))
		wx.Button(panel,117,'x',size=(40,40),pos=(140,posy))
		wx.Button(panel,118,'÷',size=(40,40),pos=(180,posy))
		wx.Button(panel,119,'Bkspc',size=(40,40),pos=(220,posy))
		wx.Button(panel,120,'√x',size=(40,40),pos=(270,posy))
		wx.Button(panel,121,'M+',size=(40,40),pos=(310,posy))
		
		#Primeira Linha
		posy=60
		wx.Button(panel,7,'7',size=(40,40),pos=(10,posy))
		wx.Button(panel,8,'8',size=(40,40),pos=(50,posy))
		wx.Button(panel,9,'9',size=(40,40),pos=(90,posy))
		wx.Button(panel,112,'+',size=(40,40),pos=(140,posy))
		wx.Button(panel,113,'-',size=(40,40),pos=(180,posy))
		wx.Button(panel,114,'C',size=(40,40),pos=(220,posy))
		wx.Button(panel,115,'x!',size=(40,40),pos=(270,posy))
		wx.Button(panel,116,'MR',size=(40,40),pos=(310,posy))
		


		#Criando Barra de menu:
		menuBar = wx.MenuBar()
		fileMenu = wx.Menu()

		#Adicionando o item sair ao menu:
		menuBar.Append(fileMenu,'Ferramentas')
		subMenu = wx.Menu()
		vtkItem = fileMenu.Append(wx.ID_ANY,'Figuras 3D','Interação com figuras 3D')
		matrizItem = fileMenu.Append(wx.ID_ANY,'Calculadora de Matrizes','Opcões para operações com 2 matrizes')
		exitItem = fileMenu.Append(wx.ID_EXIT,'Sair','Fecha o aplicativo')

		#adicionando barra ao app
		self.SetMenuBar(menuBar)

		#bindando evento:
		#self.Bind(tipo de evento, método chamado, nome do botão associado / id do botão)
		self.Bind(wx.EVT_MENU, self.onQuit, exitItem)
		self.Bind(wx.EVT_MENU, self.FrmMatriz, matrizItem)
		self.Bind(wx.EVT_MENU, self.vtkUse, vtkItem)
		
		self.Bind(wx.EVT_BUTTON, self.calcular, id=128)

		self.Bind(wx.EVT_BUTTON, self.setNum1, id=1)
		self.Bind(wx.EVT_BUTTON, self.setNum2, id=2)
		self.Bind(wx.EVT_BUTTON, self.setNum3, id=3)
		self.Bind(wx.EVT_BUTTON, self.setNum4, id=4)
		self.Bind(wx.EVT_BUTTON, self.setNum5, id=5)
		self.Bind(wx.EVT_BUTTON, self.setNum6, id=6)
		self.Bind(wx.EVT_BUTTON, self.setNum7, id=7)
		self.Bind(wx.EVT_BUTTON, self.setNum8, id=8)
		self.Bind(wx.EVT_BUTTON, self.setNum9, id=9)
		self.Bind(wx.EVT_BUTTON, self.setNum0, id=0)

		self.Bind(wx.EVT_BUTTON, self.setPlus, id=112)
		self.Bind(wx.EVT_BUTTON, self.setMinus, id=113)
		self.Bind(wx.EVT_BUTTON, self.setMult, id=117)
		self.Bind(wx.EVT_BUTTON, self.setDiv, id=118)

		self.Bind(wx.EVT_BUTTON, self.setClean, id=114)


		self.Bind(wx.EVT_BUTTON, self.setDot, id=110)
		self.Bind(wx.EVT_BUTTON, self.setSignal, id=111)
		self.Bind(wx.EVT_BUTTON, self.setFator, id=115)
		self.Bind(wx.EVT_BUTTON, self.setMR, id=116)
		self.Bind(wx.EVT_BUTTON, self.setBcksp, id=119)
		self.Bind(wx.EVT_BUTTON, self.setSqrt, id=120)
		self.Bind(wx.EVT_BUTTON, self.setMP, id=121)
		self.Bind(wx.EVT_BUTTON, self.setAP, id=122)
		self.Bind(wx.EVT_BUTTON, self.setFP, id=123)
		self.Bind(wx.EVT_BUTTON, self.setPowY, id=125)
		self.Bind(wx.EVT_BUTTON, self.setMM, id=126)
		self.Bind(wx.EVT_BUTTON, self.setVirg, id=127)
		self.Bind(wx.EVT_BUTTON, self.setPerC, id=129)
		self.Bind(wx.EVT_BUTTON, self.setMC, id=130)

		

		#configurando Frame:
		self.SetSize(380,330)
		self.SetTitle("Calculadora")
		self.Centre()
		self.Show(True)

	def onQuit(self,e):
		self.Close()

	def FrmMatriz(self,e):
		self.new = Matriz(parent=None,id=-1)

	def vtkUse(self,e):
		self.new = VtkClasse(parent=None, id=-1)
		

	def calcular(self,e):
		try:
			self.resultado = eval(self.text.GetValue(), {'pow': pow,'sqrt': sqrt,'fat':fat})
			self.text.ChangeValue('{}'.format(self.resultado))
			return(self.resultado)
		except:
			self.text.ChangeValue("Erro!")

	def setNum1(self,e):
		self.text.AppendText('1')
	def setNum2(self,e):
		self.text.AppendText('2')
	def setNum3(self,e):
		self.text.AppendText('3')
	def setNum4(self,e):
		self.text.AppendText('4')
	def setNum5(self,e):
		self.text.AppendText('5')
	def setNum6(self,e):
		self.text.AppendText('6')
	def setNum7(self,e):
		self.text.AppendText('7')
	def setNum8(self,e):
		self.text.AppendText('8')
	def setNum9(self,e):
		self.text.AppendText('9')
	def setNum0(self,e):
		self.text.AppendText('0')

	def setPlus(self,e):
		self.text.AppendText('+')
	def setMinus(self,e):
		self.text.AppendText('-')
	def setMult(self,e):
		self.text.AppendText('*')
	def setDiv(self,e):
		self.text.AppendText('/')
	
	def setClean(self,e):
		self.text.ChangeValue('')
	
	def setDot(self,e):
		self.text.AppendText('.')

	def setSignal(self,e):
		aux = self.text.GetValue()
		
		if(aux[0]=='-'):
			final = ['']
			for i in range(1,len(aux)):
				final.append(aux[i])

			final = ''.join(final)
		else:
			final = ['-']
			for i in range(len(aux)):
				final.append(aux[i])

			final = ''.join(final)

		self.text.ChangeValue(final)
	
	def setFator(self,e):
		self.text.AppendText('fat(')

	def setBcksp(self,e):
		aux = self.text.GetValue()
		corte = []
		for i in range(len(aux)-1):
			corte.append(aux[i])

		final = ''.join(corte)
		self.text.ChangeValue(final)

	def setSqrt(self,e):
		self.text.AppendText('sqrt(')
	def setAP(self,e):
		self.text.AppendText('(')
	def setFP(self,e):
		self.text.AppendText(')')
	def setPerC(self,e):
		self.text.AppendText('/100')

	def setPowY(self,e):
		self.text.AppendText('pow(')
	def setVirg(self,e):
		self.text.AppendText(',')

	def setMM(self,e):
		self.aux = self.calcular(None)
		self.memoria = self.memoria - self.aux
		self.text.ChangeValue("{}".format(self.memoria))
	def setMP(self,e):
		self.aux = self.calcular(None)
		self.memoria = self.memoria + self.aux
		self.text.ChangeValue("{}".format(self.memoria))
	def setMR(self,e):
		self.text.AppendText("{}".format(self.memoria))
	def setMC(self,e):
		self.memoria = 0
	

#Criando métodos para calculos especificos:
def fat(x):
	res = 1
	for i in range(x):
		res = (x-i)*res

	return res





app = wx.App()

Calculadora(None)

app.MainLoop()