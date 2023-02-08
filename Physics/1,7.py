from cmu_graphics import *

fire=Rect(100,100,100,100)
material=Circle(300,600,40,fill='red')

def onMouseDrag(MouseX, MouseY):
    material.centerX=MouseX
    material.centerY=MouseY
    if fire.contains(material.centerX, material.centerY):
        pass

#Increase the temperature of the material if the fire contains material
#def increaseTemperature():
    
running = True
while running:
    if fire.contains(material.centerX, material.centerY):
        material.fill='orange'
    else:
        material.fill='red'
    
cmu_graphics.run()