from cmu_graphics import *

#Create a fire
fire=Rect(100,100,100,100, fill="red")
material=Circle(300,600,40,fill=(gradient('red','orange')))
#Create a thermometer
thermometerScale=Rect(700,100,50,400,fill=(gradient('blue','red')))

#Create a thermometer pointer
thermometerPointer=Rect(700,500,50,10,fill='black')

#The temperature of the material
temperature=0

#Move the material with the mouse, if the mouse is inside the fire, the temperature of the material increases, if the mouse is outside the fire, the temperature of the material decreases
def onMouseDrag(MouseX, MouseY):
    material.centerX=MouseX
    material.centerY=MouseY
    
    print(temperature)

#Move the thermometer pointer according to the temperature of the material
def onFrame():
    thermometerPointer.centerY=500-temperature*4

def onstep():
    if fire.contains(material.centerX,material.centerY):
        pass
    temperature+=1
    thermometerPointer.centerY=500-temperature*4
    print(temperature)
    

#Run the program
cmu_graphics.run()