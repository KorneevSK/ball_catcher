class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1080
        self.screen_height = 560
        self.bg_color = (255, 255, 255)

        # Настройки корабля
        self.catcher_speed_factor = 3

        self.ball_speed_factor = 1