import pygame

from client.event_dispatcher import game_dispatcher as dispatcher
from client.events import events as Events


class Cursor:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.radius = 8

        self.color = [255, 0, 0]
        dispatcher.subscribe(Events.UPDATE_GAME, self.update)
        dispatcher.subscribe(Events.DRAW_GAME, self.draw)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def update(self):
        pos = pygame.mouse.get_pos()

        self.x = pos[0]
        self.y = pos[1]
