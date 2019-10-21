import gtk

class PyApp(gtk.Window):
	def __init__(self):
		super(PyApp,self).__init__()
		self.set_default_size(640,480)
		self.set_title("Coffee!")
		self.btn=gtk.Button("Jai")
		self.btn.connect("button_press_event",self.jai)
		screen=gtk.Fixed()
		screen.put(self.btn,50,50)
		self.add(screen)
		self.show_all()
	def jai(self,widget,event):
		print("Buttom is Clicked...")
PyApp()
gtk.main()
