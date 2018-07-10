import wx
import os
import numpy as np

class Matriz(wx.Frame):
	def __init__(self,parent,id):
		self.mat1 = np.zeros((3,3))
		self.mat2 = np.zeros((3,3))
		self.mat = [0,0,0,0,0,0,0,0,0]

		wx.Frame.__init__(self, parent, id, 'Calculadora de matrizes', size=(400,250))
		wx.Frame.CenterOnScreen(self)
		panel = wx.Panel(self)

		#Criando pop-up de pergunta:
		yesNoDialog = wx.MessageDialog(None,'Criar novas matrizes 3x3 ?','Pergunta',wx.YES_NO)
		yesNoAnswer = yesNoDialog.ShowModal() #Exibe a caixa de pertgunta
		yesNoDialog.Destroy()

		if(yesNoAnswer==wx.ID_YES):
			self.createM(self)
		else:
			self.existentM(self)

		#Elementos do frame:
		wx.StaticText(panel,-1,'Resposta:',(135,65))
		wx.Button(panel,1,'Somar',size=(120,30),pos=(10,10))
		wx.Button(panel,2,'Subtrair',size=(120,30),pos=(10,40))
		wx.Button(panel,3,'Mult. Ponto a ponto',size=(120,30),pos=(10,70))
		wx.Button(panel,4,'Mult. Matrizes',size=(120,30),pos=(10,100))
		wx.Button(panel,5,'Matriz 1',size=(120,30),pos=(10,130))
		wx.Button(panel,6,'Matriz 2',size=(120,30),pos=(10,160))

		self.mat[0] = wx.TextCtrl(panel, size=(40,40), pos=(200,10))
		self.mat[1] = wx.TextCtrl(panel, size=(40,40), pos=(240,10))
		self.mat[2] = wx.TextCtrl(panel, size=(40,40), pos=(280,10))
		self.mat[3] = wx.TextCtrl(panel, size=(40,40), pos=(200,50))
		self.mat[4] = wx.TextCtrl(panel, size=(40,40), pos=(240,50))
		self.mat[5] = wx.TextCtrl(panel, size=(40,40), pos=(280,50))
		self.mat[6] = wx.TextCtrl(panel, size=(40,40), pos=(200,90))
		self.mat[7] = wx.TextCtrl(panel, size=(40,40), pos=(240,90))
		self.mat[8] = wx.TextCtrl(panel, size=(40,40), pos=(280,90))

		#Bind de elementos:
		self.Bind(wx.EVT_BUTTON , self.SomaM    , id = 1)
		self.Bind(wx.EVT_BUTTON , self.SubtM    , id = 2)
		self.Bind(wx.EVT_BUTTON , self.MPAP     , id = 3)
		self.Bind(wx.EVT_BUTTON , self.MDot     , id = 4)
		self.Bind(wx.EVT_BUTTON , self.showMat1 , id = 5)
		self.Bind(wx.EVT_BUTTON , self.showMat2 , id = 6)

	def showMat1(self,e):
		count=0
		for i in range(3):
			for j in range(3):
				self.mat[count].ChangeValue("{}".format(self.mat1[i][j]))
				count = count+1

	def showMat2(self,e):
		count=0
		for i in range(3):
			for j in range(3):
				self.mat[count].ChangeValue("{}".format(self.mat2[i][j]))
				count = count+1

	def SomaM(self,e):
		res=(self.mat1+self.mat2)
		count=0
		for i in range(3):
			for j in range(3):
				self.mat[count].ChangeValue("{}".format(res[i][j]))
				count = count+1

	def SubtM(self,e):
		res=(self.mat1-self.mat2)
		count=0
		for i in range(3):
			for j in range(3):
				self.mat[count].ChangeValue("{}".format(res[i][j]))
				count = count+1

	def MPAP(self,e):
		res=(self.mat1*self.mat2)
		count=0
		for i in range(3):
			for j in range(3):
				self.mat[count].ChangeValue("{}".format(res[i][j]))
				count = count+1

	def MDot(self,e):
		res=np.dot(self.mat1,self.mat2)
		count=0
		for i in range(3):
			for j in range(3):
				self.mat[count].ChangeValue("{}".format(res[i][j]))
				count = count+1

	def createM(self,e):
		 self.frm2 = wx.Frame(None,wx.ID_ANY,'Entre com as novas matrizes:',size=(360,225))
		 panel2 = wx.Panel(self.frm2)
		 self.frm2.CenterOnScreen()
		 self.a = [0,0,0,0,0,0,0,0,0]
		 self.b = [0,0,0,0,0,0,0,0,0]
		 self.a[0] = wx.TextCtrl(panel2, size=(40,40), pos=(10,10))
		 self.a[1] = wx.TextCtrl(panel2, size=(40,40), pos=(50,10))
		 self.a[2] = wx.TextCtrl(panel2, size=(40,40), pos=(90,10))
		 self.a[3] = wx.TextCtrl(panel2, size=(40,40), pos=(10,50))
		 self.a[4] = wx.TextCtrl(panel2, size=(40,40), pos=(50,50))
		 self.a[5] = wx.TextCtrl(panel2, size=(40,40), pos=(90,50))
		 self.a[6] = wx.TextCtrl(panel2, size=(40,40), pos=(10,90))
		 self.a[7] = wx.TextCtrl(panel2, size=(40,40), pos=(50,90))
		 self.a[8] = wx.TextCtrl(panel2, size=(40,40), pos=(90,90))
		 wx.StaticText(panel2,-1,'MATRIZ 1',(45,135))

		 self.b[0] = wx.TextCtrl(panel2, size=(40,40), pos=(200,10))
		 self.b[1] = wx.TextCtrl(panel2, size=(40,40), pos=(240,10))
		 self.b[2] = wx.TextCtrl(panel2, size=(40,40), pos=(280,10))
		 self.b[3] = wx.TextCtrl(panel2, size=(40,40), pos=(200,50))
		 self.b[4] = wx.TextCtrl(panel2, size=(40,40), pos=(240,50))
		 self.b[5] = wx.TextCtrl(panel2, size=(40,40), pos=(280,50))
		 self.b[6] = wx.TextCtrl(panel2, size=(40,40), pos=(200,90))
		 self.b[7] = wx.TextCtrl(panel2, size=(40,40), pos=(240,90))
		 self.b[8] = wx.TextCtrl(panel2, size=(40,40), pos=(280,90))
		 wx.StaticText(panel2,-1,'MATRIZ 2',(235,135))

		 wx.Button(panel2,100,'Pronto!',pos=(120,150))
		 self.frm2.Bind(wx.EVT_BUTTON, self.getMValue, id=100)
		 self.frm2.Show()



	def getMValue(self,e):
		try:
			count = 0
			for i in range(3):
				for j in range(3):
					self.mat1[i][j] = self.a[count].GetValue()
					self.mat2[i][j] = self.b[count].GetValue()
					count = count+1

			self.Show()
			self.frm2.Close()
		except:
			wx.PopupWindow()

	def existentM(self,e):
		aux = []
		aux2 =[]

		wildcard = "TXT files (*.txt)|*.txt"
		dialog = wx.FileDialog(self, "Abrir arquivo .txt com matrizes", wildcard=wildcard,style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

		if dialog.ShowModal() == wx.ID_CANCEL:
			return

		path = dialog.GetPath()

		if os.path.exists(path):
			with open(path) as arq:
				mat1 = arq.readline()
				mat2 = arq.readline()

				arq.close()


				for i in range(len(mat1)):
					if (mat1[i].isnumeric()):
						aux.append(mat1[i])

				for i in range(len(mat2)):
					if (mat2[i].isnumeric()):
						aux2.append(mat2[i])

				count = 0
				for i in range(3):
					for j in range(3):
						self.mat1[i][j]= aux[count]
						self.mat2[i][j] = aux2[count]
						count = count+1
		self.Show()