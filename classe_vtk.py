import wx
import os
import vtk
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor

class VtkClasse(wx.Frame):
	def __init__(self,parent,id):


		wx.Frame.__init__(self, parent, id, 'Figuras 3D', size=(400,400))
		frm = wx.Frame(self,-1, 'Figuras 3D', size=(800,600))
		panel = wx.Panel(frm)

		#Elementos do VTK:
		self.widget = wxVTKRenderWindowInteractor(panel,-1,'Objetos 3D', size = (600,600))
		self.widget.Enable(1)

		self.ren = vtk.vtkRenderer()
		self.widget.GetRenderWindow().AddRenderer(self.ren)

		self.cam = vtk.vtkCamera()
		self.cam = self.ren.GetActiveCamera()
		self.cam.SetPosition(-8,-2,0)

		#Elementos do frame:
		self.Cesfera = wx.Button(panel,1,'Criar Esfera',size=(120,30),pos=(620,10))
		self.Desfera = wx.Button(panel,2,'Destruir Esfera',size=(120,30),pos=(620,40))
		self.Ccone   = wx.Button(panel,3,'Criar Cone',size=(120,30),pos=(620,70))
		self.Dcone   =wx.Button(panel,4,'Destruir Cone',size=(120,30),pos=(620,100))
		self.clean   =wx.Button(panel,5,'Limpar',size=(120,30),pos=(620,130))

		self.Dcone.Disable()
		self.Desfera.Disable()
		
		#Bind de elementos:
		self.Bind(wx.EVT_BUTTON , self.criaE    , id = 1)
		self.Bind(wx.EVT_BUTTON , self.destE    , id = 2)
		self.Bind(wx.EVT_BUTTON , self.criaC    , id = 3)
		self.Bind(wx.EVT_BUTTON , self.destC    , id = 4)
		self.Bind(wx.EVT_BUTTON , self.limpa    , id = 5)

		frm.Show()

	def criaE(self,e):
		#CRIANDO ESFERA
		esf = vtk.vtkSphereSource()
		esf.SetPhiResolution(1000)
		esf.SetThetaResolution(1000)
		mapper = vtk.vtkPolyDataMapper()
		mapper.SetInputConnection(esf.GetOutputPort())
		self.actorE = vtk.vtkActor()
		self.actorE.SetPosition(0,0.5,1)
		self.actorE.SetMapper(mapper)
		self.ren.AddActor(self.actorE)
		self.widget.Render()

		self.Cesfera.Disable()
		self.Desfera.Enable()

	def destE(self,e):
		self.ren.RemoveActor(self.actorE)
		self.widget.Update()
		self.widget.Render()
		self.Cesfera.Enable()
		self.Desfera.Disable()

	def criaC(self,e):
		#CRIANDO CONE
		cone = vtk.vtkConeSource()
		cone.SetResolution(1000)
		mapper = vtk.vtkPolyDataMapper()
		mapper.SetInputConnection(cone.GetOutputPort())
		self.actorC = vtk.vtkActor()
		self.actorC.SetMapper(mapper)
		self.ren.AddActor(self.actorC)
		self.widget.Update()
		self.widget.Render()
		self.Ccone.Disable()
		self.Dcone.Enable()

	def destC(self,e):
		self.ren.RemoveActor(self.actorC)
		self.widget.Render()
		self.Ccone.Enable()
		self.Dcone.Disable()

	def limpa(self,e):
		self.ren.RemoveAllViewProps() #remove todos os actors do renderer 'ren'
		self.ren.GetRenderWindow().Finalize() #Limpa a janela de interface
		self.widget.Render()

		self.Ccone.Enable()
		self.Dcone.Disable()
		self.Cesfera.Enable()
		self.Desfera.Disable()