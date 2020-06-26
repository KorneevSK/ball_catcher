import sys
import pygame
from random import randint
from catcher import Catcher
from ball import Ball

def check_keydown_events(event, catcher):
    """Обработка нажатия клавиш"""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, catcher):
    """Обработка отпускания клавиш"""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = False
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = False

def check_events(catcher):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, catcher)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, catcher)

def update_screen(ai_settings, screen, catcher, balls):
    """Обновляет изображения на экране и отображает новый экран"""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев
    catcher.blitme()
    balls.draw(screen)
    # Отображение последнего прорисованного окна
    pygame.display.flip()

def check_balls_collisions(ai_settings, screen, catcher, balls):
    """Обработка коллизий пуль с пришельцами"""
    # Удаление пуль и пришельцев, участвующих в коллизиях
    collisions = pygame.sprite.spritecollide(catcher, balls, True)

    if len(balls) == 0:
        # Уничтожение существующих пуль и создание нового флота
        create_ball(ai_settings, screen, balls)

def create_ball(ai_settings, screen, balls):
    """Создание пришельца и размещение его в ряду"""
    ball = Ball(ai_settings, screen)
    ball_width = ball.rect.width
    ball.x = randint(0, ai_settings.screen_width)
    ball.rect.x = ball.x
    ball.rect.y = ball.rect.height
    balls.add(ball)


def update_balls(ai_settings, screen, balls, catcher):
    """Проверяет, достиг ли дождь края экрана, после чего обновляет позиции всех капель на экране"""
    balls.update()
    for ball in balls.copy():
        if ball.rect.top >= ai_settings.screen_height:
            balls.remove(ball)
        check_balls_collisions(ai_settings, screen, catcher, balls)
