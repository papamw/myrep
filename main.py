from direct.showbase.ShowBase import ShowBase
from panda3d.core import LVector3

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Charger un modèle 3D
        self.model = self.loader.loadModel("models/panda")
        self.model.reparentTo(self.render)

        # Déplacer le modèle
        self.model.setPos(LVector3(0, 10, 0))

app = MyApp()
app.run()
