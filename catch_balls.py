import pygame
from settings import Settings
from catcher import Catcher
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Инициализация игры и создание объекта экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch Balls")
    # Создание корабля
    catcher = Catcher(ai_settings, screen)
    # catchers = Group()
    # catchers.add(catcher)
    # Создание группы пришельцев
    balls = Group()
    gf.create_ball(ai_settings, screen, balls)

    # Запуск основного цика игры
    while True:
        gf.check_events(catcher)
        catcher.update()
        gf.update_balls(ai_settings, screen, balls, catcher)
        gf.update_screen(ai_settings, screen, catcher, balls)


run_game()