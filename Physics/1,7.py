from cmu_graphics import *


#Temperature increase and decrease formula: T = T + 1 if the mouse is inside the fire, T = T - 1 if the mouse is inside the frigde, T = T + 0 if the mouse is outside the fire and the frigde
app.stepsPerSecond = 10

#Material values
mass = 1
c = 0.90

#Create a fire
fire=Rect(100,100,100,100, fill="red")

#Create a frigde
frigde=Rect(500,100,100,100,fill="blue")

#Create a thermometer
thermometerScale=Rect(700,100,50,400,fill=(gradient('blue','red', start='bottom')))

#Create a temperature variable
temperature = Label(0, 20, 20, size=50)

#Create a thermometer pointer
thermometerPointer=Rect(700,300,50,10,fill='black')

#Create the material
material=Circle(300,600,40,fill=(gradient('red','orange')))


#Move the material with the mouse, if the mouse is inside the fire, the temperature of the material increases, if the mouse is outside the fire, the temperature of the material decreases
def onMouseDrag(MouseX, MouseY):
    global temperature
    material.centerX=MouseX
    material.centerY=MouseY
    
def onStep():
    if fire.contains(material.centerX,material.centerY):
        temperature.value += 1
        thermometerPointer.centerY = 300 - temperature.value * 4
        print(temperature.value)
    elif frigde.contains(material.centerX,material.centerY):
        temperature.value -= 1
        thermometerPointer.centerY = 300 - temperature.value * 4
        print(temperature.value)
    #Increase the thermometer pointer according to the temperature of the material, but the thermometer pointer can't go above the top of the thermometer scale and below the bottom of the thermometer scale
    if thermometerPointer.centerY > 500:
        thermometerPointer.centerY = 500
    elif thermometerPointer.centerY < 100:
        thermometerPointer.centerY = 100
        
    

    
    
    #Change the color of the material according to the temperature of the material
    #material.fill=(gradient('red','orange',start=temperature.value/100))

    

#Run the program
cmu_graphics.run()