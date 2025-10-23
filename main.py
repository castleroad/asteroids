import pygame
from constants import *
from shot import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
 
        dt = clock.tick(60) / 1000

        screen.fill((0,0,0))
        updatable.update(dt)

        for astr in asteroids:
            if(player.isCollide(astr)):
                exit("Game over!")

            for shot in shots:
                if(astr.isCollide(shot)):
                    astr.split()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
