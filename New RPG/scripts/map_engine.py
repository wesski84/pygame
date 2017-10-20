import pygame
from scripts.textures import *


class map_engine:

    def add_tile(tile, pos, addTo):
        addTo.blit(tile, (pos[0] * Tiles.Size, pos[1] * Tiles.Size))


    def load_map(file):
        with open(file, "r") as mapfile:
            map_data = mapfile.read()

        # Read Map Data
        map_data = map_data.split("-")   # Split into list of tiles

        map_size = map_data[len(map_data) - 1]   # Get map dimensions
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0]) * Tiles.Size
        map_size[1] = int(map_size[1]) * Tiles.Size

        tiles = []

        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":"))   # Split pos from texture

        for tile in tiles:
            tile[0] = tile[0].split(",")   # Split pos into list
            pos = tile[0]
            for p in pos:
                pos[pos.index(p)] = int(p)   # Convert to integer

            tiles[tiles.index(tile)] = (pos, tile[1])   # Save to tile list


        # Create Terrain
        terrain = pygame.Surface(map_size, pygame.HWSURFACE)

        for tile in tiles:
            if tile[1] in Tiles.texture_tags:
                map_engine.add_tile(Tiles.texture_tags[tile[1]], tile[0], terrain)


            if tile[1] in Tiles.blocked_types:
                Tiles.blocked.append(tile[0])

        return terrain
