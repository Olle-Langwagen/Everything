from ursina import *
import random

app = Ursina()

# Create the player
player = FirstPersonController()

# Create a gun entity and attach it to the player's hand
gun = Entity(model='cube', scale=(0.1, 0.3, 0.5), position=(0.5, -0.25, 1))
gun.parent = player.right_arm

# Create a list to store the enemy entities
enemies = []

# Create a counter variable to keep track of how many enemies have been spawned
num_enemies_spawned = 0

# Create a counter variable to keep track of how many enemies are remaining
num_enemies_remaining = 0

# Create a function to spawn a new wave of enemies
def spawn_wave():
    global num_enemies_spawned, num_enemies_remaining
    num_enemies_spawned = 0
    num_enemies_remaining = 10 # spawn 10 enemies in each wave
    for i in range(num_enemies_remaining):
        enemy = Entity(model='sphere', scale=(0.3, 0.3, 0.3), position=(random.uniform(-10, 10), 0, random.uniform(-10, 10)))
        enemies.append(enemy)
        num_enemies_spawned += 1

# Call the spawn_wave function to start the first wave of enemies
spawn_wave()

# Create a function to detect collisions between the gun and enemies
def update():
    global num_enemies_remaining
    for enemy in enemies:
        if gun.intersects(enemy).hit:
            enemies.remove(enemy)
            destroy(enemy)
            num_enemies_remaining -= 1
    if num_enemies_remaining == 0:
        spawn_wave()

app.run()