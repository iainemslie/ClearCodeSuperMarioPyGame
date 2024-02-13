# Collisions

## level.py

We create two groups, one to hold all sprites and one to hold the level tiles

- `self.all_sprites`
- `self.collision_sprites`

Then when we add the `Sprite` objects we add them to both groups.

For the player we only add it to `all_sprites` but give it access to the `collision_sprites` by passing them as a parameter.

## player.py

We assign a member variable `self.collision_sprites` which is assigned the paramter we passed in.

We split the players move into vertical and horizontal directions and add a `self.gravity` attribute to control the speed that the player falls when they are not on a surface.

The movement in the x direction is controlled by the input from the player as the `self.direction.x` part of the vector is set based on this.

The movement in the y direction is controlled by the gravity attribute we added. This is continuously increased to account for acceleration.

In the move method, after moving the player we call the `collision()` method to check for overlaps between the player's rect object and the rect objects in the collision_sprites collection. This is done for both the x and y directions.

We iterate through all of the rects in the `self.collision_sprites` collection and check if there is overlap between the player and each rect. If there is we then determine from which direction the player moved. We do this be checking which side of the rects are overlapping. We keep track of the previous position of the player object by using `self.old_rect` which is updated at the start of every call to the `update()` method.
