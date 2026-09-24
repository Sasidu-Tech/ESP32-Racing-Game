import pygame
import random
import serial
import time

# ==============================
# ESP32 CONNECTION
# ==============================

ESP32_PORT = "COM8"
BAUD_RATE = 115200

esp32 = serial.Serial(ESP32_PORT, BAUD_RATE, timeout=0.01)
time.sleep(2)

print("ESP32 Connected!")


# ==============================
# PYGAME
# ==============================

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ESP32 Racing Game")

clock = pygame.time.Clock()


# ==============================
# COLORS
# ==============================

ROAD = (55, 55, 55)
GRASS = (30, 120, 30)
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
RED = (220, 40, 40)
BLUE = (40, 100, 220)


# ==============================
# ROAD
# ==============================

ROAD_X = 200
ROAD_WIDTH = 400

CAR_WIDTH = 50
CAR_HEIGHT = 80


# ==============================
# PLAYER
# ==============================

player_x = 375
player_y = 480
player_speed = 7


# ==============================
# ENEMIES
# ==============================

enemies = [
    {
        "x": 235,
        "y": -100,
        "speed": 5
    },
    {
        "x": 365,
        "y": -400,
        "speed": 6
    }
]


score = 0
game_over = False


# ==============================
# RESET GAME
# ==============================

def reset_game():

    global player_x
    global score
    global game_over

    player_x = 375
    score = 0
    game_over = False

    enemies[0]["y"] = -100
    enemies[1]["y"] = -400

    enemies[0]["speed"] = 5
    enemies[1]["speed"] = 6

    for enemy in enemies:
        enemy["x"] = random.choice([
            235,
            365,
            500
        ])


# ==============================
# MAIN LOOP
# ==============================

running = True

while running:

    # --------------------------
    # PYGAME EVENTS
    # --------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    # --------------------------
    # ESP32 BUTTON INPUT
    # --------------------------

    while esp32.in_waiting:

        command = esp32.readline().decode("utf-8", errors= "ignore").strip()

        print("ESP32:", command)

        if command == "LEFT":

            if not game_over:
                player_x -= player_speed

        elif command == "RIGHT":

            if not game_over:
                player_x += player_speed

        elif command == "START":

            reset_game()


    # --------------------------
    # KEYBOARD BACKUP
    # --------------------------

    keys = pygame.key.get_pressed()

    if not game_over:

        if keys[pygame.K_LEFT]:
            player_x -= player_speed

        if keys[pygame.K_RIGHT]:
            player_x += player_speed


    # --------------------------
    # ROAD LIMIT
    # --------------------------

    if player_x < ROAD_X:
        player_x = ROAD_X

    if player_x + CAR_WIDTH > ROAD_X + ROAD_WIDTH:
        player_x = ROAD_X + ROAD_WIDTH - CAR_WIDTH


    # --------------------------
    # GAME LOGIC
    # --------------------------

    if not game_over:

        for enemy in enemies:

            enemy["y"] += enemy["speed"]

            if enemy["y"] > HEIGHT:

                score += 1

                enemy["y"] = random.randint(-400, -100)

                enemy["x"] = random.choice([
                    235,
                    365,
                    500
                ])

                enemy["speed"] += 0.2


        # Player collision box

        player_rect = pygame.Rect(
            player_x,
            player_y,
            CAR_WIDTH,
            CAR_HEIGHT
        )


        # Enemy collision

        for enemy in enemies:

            enemy_rect = pygame.Rect(
                enemy["x"],
                enemy["y"],
                CAR_WIDTH,
                CAR_HEIGHT
            )

            if player_rect.colliderect(enemy_rect):

                game_over = True


    # ==========================
    # DRAW
    # ==========================

    screen.fill(GRASS)

    # Road

    pygame.draw.rect(
        screen,
        ROAD,
        (
            ROAD_X,
            0,
            ROAD_WIDTH,
            HEIGHT
        )
    )


    # Lane lines

    lane1 = ROAD_X + ROAD_WIDTH // 3
    lane2 = ROAD_X + (ROAD_WIDTH // 3) * 2

    for y in range(0, HEIGHT, 40):

        pygame.draw.rect(
            screen,
            WHITE,
            (
                lane1 - 3,
                y,
                6,
                25
            )
        )

        pygame.draw.rect(
            screen,
            WHITE,
            (
                lane2 - 3,
                y,
                6,
                25
            )
        )


    # ==========================
    # PLAYER CAR
    # ==========================

    pygame.draw.rect(
        screen,
        RED,
        (
            player_x,
            player_y,
            CAR_WIDTH,
            CAR_HEIGHT
        )
    )

    # Windshield

    pygame.draw.rect(
        screen,
        BLACK,
        (
            player_x + 10,
            player_y + 10,
            30,
            20
        )
    )


    # ==========================
    # ENEMY CARS
    # ==========================

    for enemy in enemies:

        pygame.draw.rect(
            screen,
            BLUE,
            (
                enemy["x"],
                enemy["y"],
                CAR_WIDTH,
                CAR_HEIGHT
            )
        )

        pygame.draw.rect(
            screen,
            BLACK,
            (
                enemy["x"] + 10,
                enemy["y"] + 10,
                30,
                20
            )
        )


    # ==========================
    # SCORE
    # ==========================

    font = pygame.font.Font(None, 45)

    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (20, 20)
    )


    # ==========================
    # GAME OVER
    # ==========================

    if game_over:

        big_font = pygame.font.Font(None, 80)

        game_over_text = big_font.render(
            "GAME OVER",
            True,
            RED
        )

        restart_text = font.render(
            "Press START Button",
            True,
            WHITE
        )

        screen.blit(
            game_over_text,
            (
                WIDTH // 2 -
                game_over_text.get_width() // 2,
                230
            )
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 -
                restart_text.get_width() // 2,
                320
            )
        )


    pygame.display.update()

    clock.tick(60)


# ==============================
# CLOSE
# ==============================

esp32.close()
pygame.quit()