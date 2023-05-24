from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader

def openScoreboard():
    pass
#fullscreen
window.size = window.fullscreen_size
window.position = Vec2(0, 0)

#app
app = Ursina()
#DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))
#player & camera
editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(model='cube', position=(20,0,0), z=-10, color=color.light_gray, origin_y=-0.5, speed=8, has_pickup=False)
pickup = Entity(model='sphere', position=(1,.5,3))
pickup.visible = False

#gun
playergun = Entity(model="cube", position=(0.25,-0.25,1), parent=camera, scale=(0.1,0.1,1), origin_z=0.5, on_cooldown=False, color=color.light_gray,shader=basic_lighting_shader)
playergun.muzzle_flash = Entity(parent=playergun, z=1, y=-2, x=2, world_scale=.3, model='quad', color=color.yellow, enabled=False)
gun_damage = 10
damage_dealt = 0
damage_text = Text(text='0', position=(0, 0))


shootables_parent = Entity()
mouse.traverse_target = shootables_parent
#Buttons for the pause menu
quit_button = Button(text="Quit", on_click=application.quit, position=(0,0.4), scale=(0.1,0.05), color=color.red, ignore_paused=True, enabled=False)
scoreboard_button = Button(text="Scoreboard", on_click=openScoreboard, position=(0,0.3), scale=(0.2,0.05), color=color.green, ignore_paused=True, enabled=False)
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

#timer
timer = Text(text='0', position=(-0.87,0.47), t=0)
pickup_timer = Text(text='0', position=(-0.64,0.47), t=0)
pickup_text = Text(text='Pickup in: ', position=(-0.76,0.47))


#skjuta
def shoot():
    global damage_dealt, gun_damage
    if not playergun.on_cooldown:
        playergun.on_cooldown = True
        playergun.muzzle_flash.enabled = True
        invoke(playergun.muzzle_flash.disable, delay=.05)
        invoke(setattr, playergun, 'on_cooldown', False, delay=0.3)
        #If the player is looking at an enemy, the enemy will take damage
        if mouse.hovered_entity == enemy:
            damage_dealt += gun_damage
            damage_text.text = damage_dealt
            enemy.blink(color.white, duration=.1)


        

#main update for shooting input, timer
def update():
    if held_keys['left mouse']:
        
        shoot()
    #Timer
    timer.t += time.dt
    timer.text = str(round(timer.t, 2))
    pickup_timer.text = str(round(-timer.t+10, 2))

    if -timer.t+10 < 0:
        pickup.visible = True
        pickup_timer.visible = False
        pickup_text.text = "Pickup has Spawned"
    #if timer.t > 10:
        #pickup.visible = True

    if not player.has_pickup and distance(player, pickup) < pickup.scale_x / 2:
        print('pickup')

        player.has_pickup  = True
        pickup.animate_scale(0, duration=.1)
        destroy(pickup, delay=.1)
        player.speed = player.speed * 2
        pickup_text.visible = False
    
    


    

#enkelt sluta, kommer ändra sen
def input(key):
    if key == 'escape':
        quit()


    

def pause(key):
    #Tab will be used as a pause button, it will pause the enemy and the player, and unlock the mouse so you can access a menu
    if key =="tab":
        editor_camera.enabled = not editor_camera.enabled

        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        playergun.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position

        application.paused = editor_camera.enabled

        #enable all the menu/pause buttons
        quit_button.enabled = editor_camera.enabled
        scoreboard_button.enabled = editor_camera.enabled

pause_handler = Entity(ignore_paused=True, input=pause)



class Enemy(Entity):
    def __init__(self, **kwargs):
        
        super().__init__(parent=shootables_parent, model='Assets/ToughGuy.obj', scale_y=2,scale_x=2,scale_z=2, origin_y=-0.75, color=color.light_gray, collider='box',shader=basic_lighting_shader, enemyspeed=2, **kwargs)
        self.color = color.red
        self.max_hp = 100
        self.hp = self.max_hp



    def update(self):

        dist = distance_xz(player.position, self.position)
        if dist > 40:
            return

        self.look_at_2d(player, "y")
        distance_to_player = distance_xz(self.position, player.position)
        if distance_to_player >= 2.5:
            self.position += self.forward * time.dt * self.enemyspeed
        else:
            print_on_screen("hejdå", position=(0,0), scale=5, duration=1)


        hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
        if hit_info.entity == player:
            if dist > 2:
                self.position += self.forward * time.dt * 5
        

enemy = Enemy()














#lighting
sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))
Sky()





app.run()