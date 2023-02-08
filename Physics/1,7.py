from cmu_graphics import *

fire=Rect(100,100,100,100)

def OnMouseDrag(MouseX, MouseY):
    fire.centerX=MouseX
    fire.centerY=MouseY

cmu_graphics.run()