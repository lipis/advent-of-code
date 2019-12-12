class Planet(object):
    vX = 0
    vY = 0
    vZ = 0

    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z

    def move(self):
        self.X += self.vX
        self.Y += self.vY
        self.Z += self.vZ

    def update_velocity(self, other):
        self.vX += 0 if other.X == self.X else 1 if other.X > self.X else -1
        self.vY += 0 if other.Y == self.Y else 1 if other.Y > self.Y else -1
        self.vZ += 0 if other.Z == self.Z else 1 if other.Z > self.Z else -1

    def energy(self):
        return (abs(self.X) + abs(self.Y) + abs(self.Z)) * (
            abs(self.vX) + abs(self.vY) + abs(self.vZ)
        )

    def __str__(self):
        return "%4.0f %4.0f %4.0f    %4.0f %4.0f %4.0f" % (
            self.X,
            self.Y,
            self.Z,
            self.vX,
            self.vY,
            self.vZ,
        )


data = [
    Planet(1, 3, -11),
    Planet(17, -10, -8),
    Planet(-1, -15, 2),
    Planet(12, -4, -4),
]

data1 = [
    Planet(-1, 0, 2),
    Planet(2, -10, -7),
    Planet(4, -8, 8),
    Planet(3, 5, -1),
]

for index in range(1000):
    for planet_a in data:
        for planet_b in data:
            if planet_a != planet_b:
                planet_a.update_velocity(planet_b)

    for planet in data:
        planet.move()

part1 = 0
for planet in data:
    part1 += planet.energy()

print(part1)
