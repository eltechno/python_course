import pgzrun
# Spacewalk   # by Sean McManus   # www.sean.co.uk / www.nostarch.com
WIDTH = 800
HEIGHT = 600
player_x = 600
player_y = 350
def draw():
    screen.blit(images.backdrop, (0, 0))
pgzrun.go()