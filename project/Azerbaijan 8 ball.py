
import pygame
import random
import sys

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Luca Maxim - Azerbaijan Technology.mp3")
pygame.mixer.music.play(-1) 

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Azerbaijan Elite 8 Ball")

font = pygame.font.SysFont('Times New Roman', 36)
input_font = pygame.font.SysFont(None, 28)

answers = [
    "Absolutely yes!", "Definitely yes!", "100% yes!", "Without a doubt yes!",
    "Maybe...", "Ask again later.", "No.", "Definitely no.", "Not likely.", "Ask again gang"
]

def draw_text(text, y, font_obj=font):
    txt_surface = font_obj.render(text, True, (255, 255, 255))
    rect = txt_surface.get_rect(center=(WIDTH//2, y))
    screen.blit(txt_surface, rect)

#essentials
input_box = pygame.Rect(WIDTH//2 - 200, 200, 400, 32)  
user_text = ""
active = False

running = True
answer = "Ask questions and let Yakub answer for you."
last_question = ""
background = pygame.image.load("ceo.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#to loop asf

while running:
    screen.blit(background, (0, 0))
    draw_text("Elite ball Questions", 50)
    draw_text(answer, 120)
    if last_question:
        draw_text(f"Q: {last_question}", 90, input_font)
        draw_text("Ask another, and let Yakub answer again.", 160, input_font)  # New message

    pygame.draw.rect(screen, (255, 255, 255), input_box, 2)
    draw_text(user_text, input_box.centery, input_font)
    draw_text("Type your question and press ENTER. ESC to quit.", 270, input_font)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                if last_question and not user_text.strip():
                    # Reset to default prompt
                    answer = "Ask your questions and let Yakub answer for you"
                    last_question = ""
                elif user_text.strip():
                    last_question = user_text
                    if user_text.strip().lower() == "67":
                        answer = "ts so tuff"
                    else:
                        answer = random.choice(answers)
                        user_text = ""
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                if len(user_text) < 50:
                    user_text += event.unicode


    pygame.display.flip()


pygame.quit()