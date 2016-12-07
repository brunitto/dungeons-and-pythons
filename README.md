# DUNGEONS AND PYTHONS

Explore dungeons, fight monsters and avoid traps.

This is a simple RPG game written in python, as defined in exercise 36 at
[Learn Python the Hard Way](https://learnpythonthehardway.org/book/ex36.html)

## Features

1. Console based game: read some text, choose an action
2. Simple battle system: attack or defend, kill or die
3. Player and monster stats: health points (HP), attack points (AP), defense
points (DP) and gold pieces (GP)

## Backlog

1. Player inventory: list of gathered items
2. Levels and XP: experience points to level up
3. Quick time events: choose an action within a short period of time

## How to play

TODO define a quickstart guide

## Battle system

1. Rolls a D6 (a random value between 1 and 6)
2. Add the player/monster attack points
3. Subtract the playermonster defense points
4. Calculate the damage, apply to the player/monster HP
5. If player HP < 1, game over
6. If monster HP < 1, victory

## Console layout

The console layout defines how information is rendered in the console.

### General screen

The general screen shows useful information about the game, as the current
dungeon, room and player stats.

    DUNGEONS AND PYTHONS
    ----------------------------------------------------------------------------
    Dungeon: --, Room: --
    Player: PLAYER NAME, HP: --, AP: --, DP: --, GP: --

### Rooms screen

In rooms, the dungeon master tells what is happening, and the player should
take an action.

    DM: You enter a dark room, there are two open doors...

    1 - Open the left door
    2 - Open the right door

### Battles screen

In battles, you can attack or defend.

    Monster: Ugly Orc, HP: --, AP: --, DP: --

    Player/Monster attacks, rolls --, dealing -- of damage!

    1 - Attack
    2 - Defend

## The game map

The game map defines the events and actions available, structured as a linked
list. Each event is defined by an unique ID, and actions are also handled as
events.

### Dungeon 1

#### Room 1

You wake up in a dark and dry room. You look around and it's looks like a cell.
Right in front of you, close to the cell bars, there is a guard, drop dead...

1 - Scream for help
No one listens to you, you are on your own.

2 - Check the guard body
You find the cell key in his pocket. You can leave the cell.
Go to room 2

#### Room 2

This look like a corridor full of cells. There is an open door on the right and
a long corridor on the left...

1 - Enter the open door on the right
Go to Room 3

2 - Run through the corridor on the left
You run as fast as you can through the corridor. You can hear the sounds of a
heat battle nearby. You enter the only door available at the end of the
corridor, and it looks like the main hall, with a huge half open port at the
end of it. You can feel a weak breeze and the sound of the external world...
Go to Room 4

#### Room 3

You enter a messy and dry room, there are a interesting desk in the corner,
covered with papers and a shiny drawer...

1 - Check the drawer
You found 2GP

2 - Leave the room
Go to Room 2

#### Room 4

You enter the main hall. You fell a huge shade coming from nowhere, weaving a
big axe at you, time to battle...

Ugly Orc, HP: 10, AP: 2, DP: 2, GP: 4
Go to Room 5

#### Room 5

After a heat battle, you still have energy to run. At the end of the hall,
you enter the half opened port and can see the light again...
Go to Dungeon 2

## Issues

(https://github.com/brunitto/dungeons-and-pythons/issues)[https://github.com/brunitto/dungeons-and-pythons/issues]

## Contribute

(https://github.com/brunitto/dungeons-and-pythons)[https://github.com/brunitto/dungeons-and-pythons]

