from cmu_graphics import *

#This program will have a material, like a ball, and a liquid, like water, and the ball will float in the water
#The ball will have a buoyancy force, and the liquid will have a density
#The buoyancy force will be equal to the density of the liquid times the volume of the ball times the acceleration due to gravity

#The ball will have a mass, and the liquid will have a density
#The mass of the ball will be equal to the density of the liquid times the volume of the ball

#The volume of the ball will be equal to the radius of the ball times the radius of the ball times pi

#The density of the liquid will be equal to the mass of the liquid divided by the volume of the liquid

#The mass of the liquid will be equal to the density of the liquid times the volume of the liquid

#The volume of the liquid will be equal to the area of the liquid times the depth of the liquid



#The ball will have a radius, and the liquid will have an area and a depth

#Create the ball using cmu_graphics
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        fill(*self.color)
        circle(self.x, self.y, self.radius)

    def update(self):
        self.y += 1

#Create the liquid using cmu_graphics
class Liquid:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        fill(*self.color)
        rect(self.x, self.y, self.width, self.height)

#Create the ball


cmu_graphics.run()
