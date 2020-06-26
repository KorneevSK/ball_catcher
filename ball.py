import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    """Представление одного пришельца"""
    def __init__(self, ai_settings, screen):
        """Инициализация пришельца и задание начальной позиции"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('ball.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает каплю вниз"""
        self.rect.y += self.ai_settings.ball_speed_factor
        # self.rect.y = self.y

    def check_edges(self):
        """Возвращает True, если капля находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True


    def blitme(self):
        """Выводит пришельца в текущем положении"""
        self.screen.blit(self.image, self.rect)
