from settings import *
from sprites import Sprite, AnimatedSprite
from groups import WorldSprites
from random import randint


class Overworld:
    def __init__(self, tmx_map, data, overworld_frames):
        self.display_surface = pygame.display.get_surface()
        self.data = data

        # groups
        self.all_sprites = WorldSprites(data)

        self.setup(tmx_map, overworld_frames)

    def setup(self, tmx_map, overworld_frames):
        # tiles
        for layer in ['main', 'top']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf,
                       self.all_sprites, Z_LAYERS['bg tiles'])

        # water
        for col in range(tmx_map.width):
            for row in range(tmx_map.height):
                AnimatedSprite((col * TILE_SIZE, row * TILE_SIZE),
                               overworld_frames['water'], self.all_sprites, Z_LAYERS['bg'])

        # objects
        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'palm':
                AnimatedSprite(
                    (obj.x, obj.y), overworld_frames['palms'], self.all_sprites, Z_LAYERS['main'], animation_speed=randint(4, 6))
            else:
                z = Z_LAYERS[f"{'bg details' if obj.name == 'grass' else 'bg tiles'}"]
                Sprite((obj.x, obj.y), obj.image, self.all_sprites, z)

        # nodes & player
        # for obj in tmx_map.get_layer_by_name('Nodes'):
        #     # nodes
        #     if obj.name == 'Node':
        #         Node()

    def run(self, dt):
        self.all_sprites.update(dt)
        self.all_sprites.draw((1000, 800))
