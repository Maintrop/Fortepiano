# Імпортування модулей
import pygame
pygame.init()
pygame.mixer.init()

# Імпортування класів та функцій з інших файлів
from button import Button
from settings import WIDTH, HEIGHT, FPS, BLACK, WHITE, GRAY, LIGHT_GRAY

# Вікно
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Заголовок
pygame.display.set_caption("Fortepiano")

# Годинник
clock = pygame.time.Clock()

# Зображення
bg = pygame.image.load("assets/images/bg.jpeg").convert_alpha()
bg_size = (WIDTH, HEIGHT)
bg = pygame.transform.scale(bg, bg_size)

# Звуки
sound_a = pygame.mixer.Sound("assets/sounds/a6.mp3")
sound_b = pygame.mixer.Sound("assets/sounds/b6.mp3")
sound_c = pygame.mixer.Sound("assets/sounds/c6.mp3")
sound_d = pygame.mixer.Sound("assets/sounds/d6.mp3")
sound_e = pygame.mixer.Sound("assets/sounds/e6.mp3")
sound_f = pygame.mixer.Sound("assets/sounds/f6.mp3")
sound_g = pygame.mixer.Sound("assets/sounds/g6.mp3")

# Кнопка settings
font_btn_settings = pygame.font.SysFont(None, 40)
btn_settings = Button(20, 20, 200, 70, GRAY, font_btn_settings, "Settings", BLACK, 8)

# Кнопки фортепіано
font_none = pygame.font.SysFont(None, 0)
btn_a = Button(150, 200, 100, 200, LIGHT_GRAY, font_none, "", BLACK, 16)
btn_b = Button(250, 200, 100, 200, LIGHT_GRAY, font_none, "", BLACK, 16)
btn_c = Button(350, 200, 100, 200, LIGHT_GRAY, font_none, "", BLACK, 16)
btn_d = Button(450, 200, 100, 200, LIGHT_GRAY, font_none, "", BLACK, 16)
btn_e = Button(550, 200, 100, 200, LIGHT_GRAY, font_none, "", BLACK, 16)
btn_f = Button(650, 200, 100, 200, LIGHT_GRAY, font_none, "", BLACK, 16)
btn_g = Button(750, 200, 100, 200, LIGHT_GRAY, font_none, "", BLACK, 16)

# Список кнопок
buttons = [btn_settings, btn_a, btn_b, btn_c, btn_d, btn_e, btn_f, btn_g]

# Гра
game = True
while game:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game = False

    window.blit(bg, (0, 0))

    btn_hover = False

    for btn in buttons:
        btn.show(window)

        if btn.is_hovered():
            btn_hover = True
    
    if btn_a.is_clicked(events):
        sound_a.play()
    
    elif btn_b.is_clicked(events):
        sound_b.play()

    elif btn_c.is_clicked(events):
        sound_c.play()

    elif btn_d.is_clicked(events):
        sound_d.play()
    
    elif btn_e.is_clicked(events):
        sound_e.play()

    elif btn_f.is_clicked(events):
        sound_f.play()

    elif btn_g.is_clicked(events):
        sound_g.play()

    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND if btn_hover else pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.flip()
    clock.tick(FPS)

# Вихід з гри
pygame.quit()
