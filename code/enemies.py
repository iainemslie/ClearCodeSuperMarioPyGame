from settings import *
from random import choice
from timer import Timer


class Tooth(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, collision_sprites):
        super().__init__(groups)
        self.frames, self.frame_index = frames, 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(topleft=pos)
        self.z = Z_LAYERS['main']

        self.direction = choice((-1, 1))
        self.collision_rects = [sprite.rect for sprite in collision_sprites]
        self.speed = 200

    def update(self, dt):

        # animate
        self.frame_index += ANIMATION_SPEED * dt
        self.image = self.frames[int(self.frame_index % len(
            self.frames))]
        self.image = pygame.transform.flip(
            self.image, True, False) if self.direction < 0 else self.image

        # move
        self.rect.x += self.direction * self.speed * dt

        # reverse direction
        floor_rect_right = pygame.FRect(self.rect.bottomright, (1, 1))
        floor_rect_left = pygame.FRect(self.rect.bottomleft, (-1, 1))

        if floor_rect_right.collidelist(self.collision_rects) < 0 and self.direction > 0 or \
                floor_rect_left.collidelist(self.collision_rects) < 0 and self.direction < 0:
            self.direction *= -1


class Shell(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, reverse, player):
        super().__init__(groups)

        if reverse:
            # flip all frames in self.frames
            self.frames = {}
            for key, surfaces in frames.items():
                self.frames[key] = [pygame.transform.flip(
                    surf, True, False) for surf in surfaces]
            self.bullet_direction = -1
        else:
            self.frames = frames
            self.bullet_direction = 1

        self.frame_index = 0
        self.state = 'idle'
        self.image = self.frames[self.state][self.frame_index]
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()
        self.z = Z_LAYERS['main']
        self.player = player
        self.shoot_timer = Timer(3000)
        self.has_fired = False

    def state_management(self):
        player_pos, shell_pos = vector(
            self.player.hitbox_rect.center), vector(self.rect.center)
        player_near = shell_pos.distance_to(player_pos) < 500
        player_front = shell_pos.x < player_pos.x if self.bullet_direction > 0 else shell_pos.x > player_pos.x
        player_level = abs(shell_pos.y - player_pos.y) < 30

        if player_near and player_front and player_level and not self.shoot_timer.active:
            self.state = 'fire'
            self.frame_index = 0
            self.shoot_timer.activate()

    def update(self, dt):
        self.shoot_timer.update()
        self.state_management()

        # animation / attack
        self.frame_index += ANIMATION_SPEED * dt
        if self.frame_index < len(self.frames[self.state]):
            self.image = self.frames[self.state][int(self.frame_index)]

            # fire
            if self.state == 'fire' and int(self.frame_index) == 3 and not self.has_fired:
                print("shoot")
                self.has_fired = True

        else:
            self.frame_index = 0
            if self.state == 'fire':
                self.state = 'idle'
                self.has_fired = False
