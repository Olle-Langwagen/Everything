from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader
app = Ursina()
#DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))
#player & camera
editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(model='cube', z=-10, color=color.light_gray, origin_y=-.5, speed=8)

#gun
playergun = Entity(model="cube", position=(0.25,-0.25,1), parent=camera, scale=(0.1,0.1,1), origin_z=0.5, on_cooldown=False, color=color.light_gray,shader=basic_lighting_shader)

#obstacles and ground
ground = Entity(model='plane', collider='box', scale=64, texture='Assets/pexels-stefwithanf-3580088-1920x1080-25fps.mp4',shader=basic_lighting_shader)
for i in range(10):
    Entity(model='cube', origin_y=-.5, scale=3, texture='vertical_gradient',
        x=random.uniform(-24,24),
        z=random.uniform(-24,24),
        collider='box',
        scale_y = random.uniform(4,7),
        shader=basic_lighting_shader,
        )

#main update for shooting input
def update():
    if held_keys['left mouse']:
        
        shoot()

def shoot():
    if not playergun.on_cooldown:
        playergun.on_cooldown = True
        print_on_screen('shoot',position=playergun.position, duration=0.15)
        invoke(setattr, playergun, 'on_cooldown', False, delay=0.3)

enemy = Entity(model='Assets/ToughGuy.obj', scale_y=2,scale_x=2,scale_z=2, origin_y=-0.75, color=color.light_gray, collider='box',shader=basic_lighting_shader)


#lighting
sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))
Sky()





app.run()