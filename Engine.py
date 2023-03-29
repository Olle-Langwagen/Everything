from ursina import *
app = Ursina()

player = Entity(model='player_model.fbx', scale=(1, 1, 1), position=(0, 0, 0))
camera = Camera()

app.run()
