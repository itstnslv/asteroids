import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") 
        dt = clock.tick(60) / 1000
            
        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.collides(player):
                print("Game over!")
                sys.exit()
            for s in shots:
                if a.collides(s):
                    a.split()
                    s.kill()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()