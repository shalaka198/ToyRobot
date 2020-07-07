from enum import Enum

class Direction(Enum):
    north = 'north'
    east = 'east'
    south = 'south'
    west = 'west'

    @staticmethod
    def get_values():
        return list(map(lambda x: x.value, Direction))

    @staticmethod
    def direction_changes():
        return {
                    Direction.north : { 'left':Direction.west, 'right':Direction.east},
                    Direction.east : { 'left':Direction.north, 'right':Direction.south},
                    Direction.south : { 'left':Direction.east, 'right':Direction.west},
                    Direction.west : { 'left':Direction.south, 'right':Direction.north},
                }

#print(Direction.get_values())
