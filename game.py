import pygame
import sys

pygame.init()

# Window settings
WIDTH, HEIGHT = 640, 760
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# Colors
BG = (18, 22, 34)
PANEL = (30, 36, 54)
CARD = (42, 50, 72)
ACCENT = (94, 234, 212)
ACCENT_2 = (129, 140, 248)
TEXT = (233, 236, 244)
MUTED = (148, 163, 184)
X_COLOR = (255, 107, 107)
O_COLOR = (86, 204, 242)
WIN_COLOR = (250, 204, 21)
INPUT_BG = (24, 30, 45)
INPUT_BORDER = (94, 234, 212)
BUTTON = (94, 234, 212)
BUTTON_TEXT = (12, 20, 30)

# Fonts
font_title = pygame.font.SysFont("arial", 54, bold=True)
font_medium = pygame.font.SysFont("arial", 30, bold=True)
font_small = pygame.font.SysFont("arial", 24)
font_input = pygame.font.SysFont("arial", 30)

# Game settings
CELL = 150
BOARD_SIZE = CELL * 3
BOARD_X = (WIDTH - BOARD_SIZE) // 2
BOARD_Y = 130

# Game state
SCREEN = "start"
player_x_name = ""
player_o_name = ""
active_input = 1
board = [""] * 9
current_player = "X"
game_over = False
winner_symbol = None
winner_name = ""
winning_line = None

# Start screen boxes
x_input_box = pygame.Rect(170, 300, 300, 58)
o_input_box = pygame.Rect(170, 410, 300, 58)
start_button = pygame.Rect(220, 520, 200, 62)

# Game screen button
restart_button = pygame.Rect(220, 670, 200, 56)


def draw_rounded_rect(surface, rect, color, radius=18, border=0, border_color=None):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

    if border:
        pygame.draw.rect(
            surface,
            border_color,
            rect,
            border,
            border_radius=radius
        )


def draw_centered_text(surface, text, font, color, center):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=center)
    surface.blit(rendered, rect)


def start_new_game():
    global board, current_player, game_over, winner_symbol, winner_name, winning_line, active_input

    board = [""] * 9
    current_player = "X"
    game_over = False
    winner_symbol = None
    winner_name = ""
    winning_line = None
    active_input = 1


def check_winner():
    global game_over, winner_symbol, winner_name, winning_line

    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in lines:
        if board[a] != "" and board[a] == board[b] == board[c]:
            winner_symbol = board[a]
            winning_line = (a, b, c)
            winner_name = player_x_name if winner_symbol == "X" else player_o_name
            game_over = True
            return

    if all(cell != "" for cell in board):
        game_over = True


def get_clicked_cell(pos):
    x, y = pos

    for index in range(9):
        row = index // 3
        col = index % 3

        rect = pygame.Rect(
            BOARD_X + col * CELL,
            BOARD_Y + row * CELL,
            CELL,
            CELL
        )

        if rect.collidepoint(x, y):
            return index

    return None


def draw_start_screen():
    screen.fill(BG)

    # Background decoration
    pygame.draw.circle(screen, (35, 45, 68), (90, 120), 150)
    pygame.draw.circle(screen, (35, 45, 68), (570, 660), 170)

    # Title
    draw_centered_text(screen, "TIC TAC TOE", font_title, TEXT, (WIDTH // 2, 105))
    draw_centered_text(
        screen, "Enter player names and start the game",
        font_small, MUTED, (WIDTH // 2, 165)
    )

    # Player X card
    draw_rounded_rect(screen, pygame.Rect(90, 250, 460, 90), CARD, 20)
    draw_centered_text(screen, "Player X", font_medium, X_COLOR, (180, 295))

    pygame.draw.rect(screen, INPUT_BG, x_input_box, border_radius=14)
    pygame.draw.rect(
        screen,
        INPUT_BORDER if active_input == 1 else (70, 80, 105),
        x_input_box,
        3,
        border_radius=14
    )

    x_text = player_x_name
    if active_input == 1 and pygame.time.get_ticks() % 1000 < 500:
        x_text += "|"

    screen.blit(
        font_input.render(x_text, True, TEXT),
        (x_input_box.x + 15, x_input_box.y + 13)
    )

    # Player O card
    draw_rounded_rect(screen, pygame.Rect(90, 370, 460, 90), CARD, 20)
    draw_centered_text(screen, "Player O", font_medium, O_COLOR, (180, 415))

    pygame.draw.rect(screen, INPUT_BG, o_input_box, border_radius=14)
    pygame.draw.rect(
        screen,
        INPUT_BORDER if active_input == 2 else (70, 80, 105),
        o_input_box,
        3,
        border_radius=14
    )

    o_text = player_o_name
    if active_input == 2 and pygame.time.get_ticks() % 1000 < 500:
        o_text += "|"

    screen.blit(
        font_input.render(o_text, True, TEXT),
        (o_input_box.x + 15, o_input_box.y + 13)
    )

    # Start button
    mouse_pos = pygame.mouse.get_pos()
    button_color = (118, 245, 225) if start_button.collidepoint(mouse_pos) else BUTTON

    draw_rounded_rect(screen, start_button, button_color, 18)
    draw_centered_text(screen, "START GAME", font_medium, BUTTON_TEXT, start_button.center)

    draw_centered_text(
        screen,
        "Click a box, type the name, then press Enter",
        font_small,
        MUTED,
        (WIDTH // 2, 640)
    )


def draw_game_board():
    # Board background
    board_rect = pygame.Rect(
        BOARD_X - 18,
        BOARD_Y - 18,
        BOARD_SIZE + 36,
        BOARD_SIZE + 36
    )
    draw_rounded_rect(screen, board_rect, PANEL, 26)

    # Grid lines
    for i in range(1, 3):
        x = BOARD_X + i * CELL
        pygame.draw.line(
            screen,
            (70, 80, 105),
            (x, BOARD_Y + 12),
            (x, BOARD_Y + BOARD_SIZE - 12),
            5
        )

        y = BOARD_Y + i * CELL
        pygame.draw.line(
            screen,
            (70, 80, 105),
            (BOARD_X + 12, y),
            (BOARD_X + BOARD_SIZE - 12, y),
            5
        )

    # Cells
    for index, value in enumerate(board):
        row = index // 3
        col = index % 3

        center_x = BOARD_X + col * CELL + CELL // 2
        center_y = BOARD_Y + row * CELL + CELL // 2

        if value == "X":
            offset = 45

            pygame.draw.line(
                screen,
                X_COLOR,
                (center_x - offset, center_y - offset),
                (center_x + offset, center_y + offset),
                12
            )
            pygame.draw.line(
                screen,
                X_COLOR,
                (center_x - offset, center_y + offset),
                (center_x + offset, center_y - offset),
                12
            )

        elif value == "O":
            pygame.draw.circle(
                screen,
                O_COLOR,
                (center_x, center_y),
                50,
                12
            )

    # Winning line
    if winning_line:
        a, _, c = winning_line

        start_row, start_col = a // 3, a % 3
        end_row, end_col = c // 3, c % 3

        start = (
            BOARD_X + start_col * CELL + CELL // 2,
            BOARD_Y + start_row * CELL + CELL // 2
        )
        end = (
            BOARD_X + end_col * CELL + CELL // 2,
            BOARD_Y + end_row * CELL + CELL // 2
        )

        pygame.draw.line(screen, WIN_COLOR, start, end, 14)


def draw_game_screen():
    screen.fill(BG)

    # Background decoration
    pygame.draw.circle(screen, (35, 45, 68), (80, 90), 130)
    pygame.draw.circle(screen, (35, 45, 68), (580, 680), 150)

    # Header
    draw_centered_text(screen, "TIC TAC TOE", font_title, TEXT, (WIDTH // 2, 55))

    if game_over:
        if winner_name:
            status = f"{winner_name} won!"
            color = WIN_COLOR
        else:
            status = "It's a draw!"
            color = MUTED
    else:
        name = player_x_name if current_player == "X" else player_o_name
        symbol_color = X_COLOR if current_player == "X" else O_COLOR
        status = f"{name}'s turn ({current_player})"
        color = symbol_color

    draw_centered_text(screen, status, font_medium, color, (WIDTH // 2, 615))

    draw_game_board()

    # Restart button
    mouse_pos = pygame.mouse.get_pos()
    button_color = (118, 245, 225) if restart_button.collidepoint(mouse_pos) else BUTTON

    draw_rounded_rect(screen, restart_button, button_color, 16)
    draw_centered_text(screen, "PLAY AGAIN", font_medium, BUTTON_TEXT, restart_button.center)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos

            if SCREEN == "start":
                if x_input_box.collidepoint(mouse_pos):
                    active_input = 1

                elif o_input_box.collidepoint(mouse_pos):
                    active_input = 2

                elif start_button.collidepoint(mouse_pos):
                    if player_x_name.strip() == "":
                        player_x_name = "Player X"

                    if player_o_name.strip() == "":
                        player_o_name = "Player O"

                    start_new_game()
                    SCREEN = "game"

            elif SCREEN == "game":
                if restart_button.collidepoint(mouse_pos):
                    SCREEN = "start"
                    player_x_name = ""
                    player_o_name = ""
                    active_input = 1

                elif not game_over:
                    cell = get_clicked_cell(mouse_pos)

                    if cell is not None and board[cell] == "":
                        board[cell] = current_player
                        check_winner()

                        if not game_over:
                            current_player = "O" if current_player == "X" else "X"

        elif event.type == pygame.KEYDOWN and SCREEN == "start":
            if event.key == pygame.K_RETURN:
                if active_input == 1:
                    active_input = 2
                elif active_input == 2:
                    if player_x_name.strip() == "":
                        player_x_name = "Player X"

                    if player_o_name.strip() == "":
                        player_o_name = "Player O"

                    start_new_game()
                    SCREEN = "game"

            elif event.key == pygame.K_BACKSPACE:
                if active_input == 1:
                    player_x_name = player_x_name[:-1]
                else:
                    player_o_name = player_o_name[:-1]

            elif event.unicode.isalnum() or event.unicode == " ":
                if active_input == 1 and len(player_x_name) < 15:
                    player_x_name += event.unicode
                elif active_input == 2 and len(player_o_name) < 15:
                    player_o_name += event.unicode

    if SCREEN == "start":
        draw_start_screen()
    else:
        draw_game_screen()

    pygame.display.flip()
    clock.tick(60)