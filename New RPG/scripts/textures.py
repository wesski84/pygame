import pygame

pygame.init()

class Tiles:

    Size = 32

    blocked = []

    blocked_types = ["3", "4", "6"]

    def blocked_at(pos):
        if list(pos) in Tiles.blocked:
            return True
        else:
            return False

    def load_texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size,Size), pygame.HWSURFACE|pygame.SRCALPHA)

        surface.blit(bitmap, (0, 0))
        return surface

# Exterior Textures
    grass = load_texture('graphics/grass.png', Size)
    stone = load_texture('graphics/stone.png', Size)
    water = load_texture('graphics/water.png', Size)
    bush = load_texture('graphics/bush.png', Size)

# Interior Textures
    floor1 = load_texture('graphics/floor1.png', Size)
    plant1 = load_texture('graphics/plant1.png', Size)

    texture_tags = {"1": grass,
                    "2": stone,
                    "3": water,
                    "4": bush,
                    "5": floor1,
                    "6": plant1,
                    }

