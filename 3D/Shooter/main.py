from ftf6 import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
life = 3
ground = Entity(model='plane', texture='grass', scale=100, collider='box')
player = FirstPersonController(model='cube', origin_y=-.5, color=color.orange, has_pickup=False)
enemy = Entity(model='cube', color=color.red, scale=(1,2,1), position=(0,1,2), collider='box')
camera.z = -5
liv = Text(f'Life: {life}', scale=3, origin=(3.5,5.5))
pickup = Entity(model='sphere', position=(1,.5,3))



def update():
    if not player.has_pickup and distance(player, pickup) < pickup.scale_x / 2:
        print('pickup')

        player.has_pickup = True
        pickup.animate_scale(0, duration=.1)
        destroy(pickup, delay=.1)

app.run()