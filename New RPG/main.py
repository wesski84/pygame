import pygame, sys, time, math
from scripts.UltraColor import *
from scripts.textures import *
from scripts.globals import *
from scripts.map_engine import *
from scripts.NPC import *
from scripts.player import *
from scripts.meloonatic_gui import *

pygame.init()


icon = pygame.image.load('images/wizard_icon.png')

sky = pygame.image.load('graphics/sky.png')
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)

Sky.blit(sky, (0, 0))

del sky

logo_img_temp = pygame.image.load('graphics/logo.png')
logo_img_temp = pygame.transform.scale(logo_img_temp,(164, 232))
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0, 0))
del logo_img_temp


pygame.display.set_icon(icon)

cSec = 0
cFrame = 0
FPS = 0

terrain = map_engine.load_map('maps/level1.map')


clock = pygame.time.Clock()

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Calibri.ttf", 20)


def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.White)
    window.blit(fps_overlay, (0,0))


def show_mouse_pos():
    temp_mouse_pos = pygame.mouse.get_pos()
    # print(mouse_pos)
    # print(mouse_pos[0], mouse_pos[1])
    mouse_pos = str(temp_mouse_pos[0]) + ", " + str(temp_mouse_pos[1])
    mouse_pos = fps_font.render(mouse_pos, True, Color.White)
    window.blit(mouse_pos, (700, 0))


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "My RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width,window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)


def count_fps():
    global FPS

    FPS = clock.get_fps()
    if FPS > 0:
        Globals.deltatime = 1 / FPS


#     global cSec, cFrame, FPS, deltatime
#
#     if cSec == time.strftime("%S"):
#         cFrame += 1
#     else:
#         FPS = cFrame
#         cFrame = 0
#         cSec = time.strftime("%S")
#
#         if FPS > 0:
#             deltatime = 1 / FPS


create_window()


player = Player("Mark")
player_w, player_h = player.width, player.height
player_x = (window_width/2-player_w/2 - Globals.camera_x)/Tiles.Size
player_y = (window_height/2-player_h/2 - Globals.camera_y)/Tiles.Size

man1 = Male1(name="Tan Guy", pos=(200, 300))


# Initialize GUI

def Play():
    Globals.scene = 'game'


def Exit():
    global isRunning
    isRunning = False


btnPlay = Menu.Button(text = 'Play', rect = (0, 0, 300, 60), bg = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ('menu', None))
btnPlay.Left = window_width / 2 - btnPlay.Width / 2
btnPlay.Top = window_height / 2 - btnPlay.Height / 2
btnPlay.Command = Play

btnExit = Menu.Button(text = 'Exit', rect = (0, 0, 300, 60), bg = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ('menu', None))
btnExit.Left = btnPlay.Left
btnExit.Top = btnPlay.Top + btnExit.Height + 3
btnExit.Command = Exit

menuTitle = Menu.Text(text = 'Welcome to the RPG', color = Color.Cyan, font = Font.Large)
menuTitle.Left, menuTitle.Top = window_width / 2 - menuTitle.Width / 2, 0

logo = Menu.Image(bitmap = logo_img, pos = (0, 0))
logo.Left = window_width / 2 - logo.Width /2
logo.Top  = menuTitle.Top + menuTitle.Height - 5

isRunning = True


while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
                player.facing = "north"
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
                player.facing = "south"
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
                player.facing = "east"
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
                player.facing = "west"

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Globals.camera_move = 0
            elif event.key == pygame.K_s:
                Globals.camera_move = 0
            elif event.key == pygame.K_a:
                Globals.camera_move = 0
            elif event.key == pygame.K_d:
                Globals.camera_move = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left Click
                # Handle Button Click
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command() # Do Button event
                        btn.Rolling = False
                        break # Exit Loop

    # Render Scene
    if Globals.scene == "game":

            if Globals.camera_move == 1:
                #  LOGIC
                if not Tiles.blocked_at((round(player_x), math.floor(player_y))):
                    Globals.camera_y += 300 * Globals.deltatime
            elif Globals.camera_move == 2:
                if not Tiles.blocked_at((round(player_x), math.ceil(player_y))):
                    Globals.camera_y -= 300 * Globals.deltatime
            elif Globals.camera_move == 3:
                if not Tiles.blocked_at((math.floor(player_x), round(player_y))):
                    Globals.camera_x += 300 * Globals.deltatime
            elif Globals.camera_move == 4:
                if not Tiles.blocked_at((math.ceil(player_x), round(player_y))):
                    Globals.camera_x -= 300 * Globals.deltatime

            player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
            player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size

            # RENDER GRAPHICS
            # window.fill(Color.Black)
            window.blit(Sky, (0, 0))

            window.blit(terrain, (Globals.camera_x, Globals.camera_y))
            player.render(window, (window_width / 2 - player_w / 2, window_height / 2 - player_h / 2))

    # Process Menu
    elif Globals.scene == "menu":
        window.fill(Color.Fog)

        logo.Render(window)

        menuTitle.Render(window)

        for btn in Menu.Button.All:
            if btn.Tag[0] == 'menu':
                btn.Render(window)







    elif Globals.scene == 'house1':
        terrain = map_engine.load_map('maps/house1.map')
        if Globals.camera_move == 1:
            #  LOGIC
            if not Tiles.blocked_at((round(player_x), math.floor(player_y))):
                Globals.camera_y += 300 * Globals.deltatime
        elif Globals.camera_move == 2:
            if not Tiles.blocked_at((round(player_x), math.ceil(player_y))):
                Globals.camera_y -= 300 * Globals.deltatime
        elif Globals.camera_move == 3:
            if not Tiles.blocked_at((math.floor(player_x), round(player_y))):
                Globals.camera_x += 300 * Globals.deltatime
        elif Globals.camera_move == 4:
            if not Tiles.blocked_at((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= 300 * Globals.deltatime

        player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
        player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size

        # RENDER GRAPHICS
        # window.fill(Color.Black)
        window.blit(Sky, (0, 0))
        window.blit(terrain, (Globals.camera_x, Globals.camera_y))

        man1.render(window, (0, 0))
        # for NPC in NPC.allNPCs:
        #     NPC.render(window)

        player.render(window, (window_width / 2 - player_w / 2, window_height / 2 - player_h / 2))


    show_fps()
    show_mouse_pos()

    pygame.display.update()
    clock.tick()
    count_fps()


pygame.quit()

sys.exit()
