import pygame

class Button:
    def __init__(self, x, y, width, height, color, font, text, text_color, border_radius):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.font = font
        self.text = text
        self.text_color = text_color
        self.hover_color = tuple(min(255, i + 40) for i in self.color)
        self.hover_text_color = tuple(min(255, i + 40) for i in self.text_color)
        self.border_color = tuple(min(255, i - 40) for i in self.color)
        self.border_radius = border_radius

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def show(self, window):
        if self.is_hovered():
            pygame.draw.rect(window, self.hover_color, self.rect, border_radius=self.border_radius)
            text_btn = self.font.render(self.text, True, self.hover_text_color)
            text_rect = text_btn.get_rect(center=self.rect.center)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.draw.rect(window, self.color, self.rect, border_radius=self.border_radius)
            text_btn = self.font.render(self.text, True, self.text_color)
            text_rect = text_btn.get_rect(center=self.rect.center)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        window.blit(text_btn, text_rect)
        pygame.draw.rect(window, self.border_color, self.rect, 8, border_radius=self.border_radius)

    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered():
                return True
        return False