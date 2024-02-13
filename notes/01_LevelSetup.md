# Level Setup

## settings.py

- import modules
- Set the window dimensions
- Size of the level tiles

## main.py

We check if this module is 'main' and create a `Game` object and call the `run` method

`Game` - `__init__`

- Initializes pygame
- Sets up the window size, caption, icon etc
- load map data using pytmx

`Game - `run()`

- Starts the game loop
- Record the change in time between each loop (delta time)
- Check events for 'quit' event
- calls the run method of the current level
- updates the display

## level.py

Defines a class that deals with rendering levels

`Level` - `__init__`

- gets a reference to the display surface
- gets a reference to all the sprites
- calls the setup method

`Level` - `setup()`

- gets level data for layers provided by the tmx_map
  - creates sprite objects for each tile and adds them to all_sprites group
- gets data for the player from the tmx_map
  - creates player object and adds it to the all_sprites group

`Level - `run()`

- calls the update method for every sprite in the all_sprites group
- sets the background display surface to be black
- calls the draw method of each sprite

## sprites.py

A class that defines Sprite objects which inherit from pygame.sprite.Sprite

- `Sprite` - `__init__`

- calls the super class's init method and passes a reference to the sprite's group
- creates an surface of the TILE_SIZE constant
- sets that image to be white
- creates a rect object

## player.py

A class that defines the display and movement of the player

- `Player` - `__init__`

- calls the super class's init method and passes a reference to the sprite's group
- creates a surface object and makes it red
- creates a rect object from the surface
- defines a direction vector and a speed

- `Player` - `update()`

- check for player input `self.input()`
- updates the rect for player's position `self.move()`

- `Player` - `input()`

- gets a dictionary of keys that are currently pressed
- creates an instance of 2D vector class
- Checks for left-right arrow keypresses and updates vector accordingly
- sets direction based on this vector

- `Player` - `move()`

- Sets the position of the rect object based on direction, speed and deltatime
