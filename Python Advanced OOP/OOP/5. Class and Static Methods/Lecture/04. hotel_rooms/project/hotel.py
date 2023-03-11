from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        result = room.take_room(people)

        if result:
            return result

        self.guests += people

    def free_room(self, room_number):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        result = room.free_room()
        guests = room.guests

        if result:
            return result

        self.guests = 0

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n" \
                 f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n" \
                 f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"

        return result