# DUNGEONS AND PYTHONS

Explore dungeons, fight monsters and avoid traps.

This is a simple RPG game written in python, as defined in exercise 36 at
[https://learnpythonthehardway.org](Learn Python the Hard Way) book.

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

1. Dungeon 1

1.1. Room 1
Lorem ipsum dolor sit amet...

1.1.1. Take action 1
1.1.2. Take action 2

## Issues

TODO link to Github issues

## Contribute

TODO link to Github repository

