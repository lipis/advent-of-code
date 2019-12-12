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

################################################################################
# Part 2
################################################################################
data = [
    Planet(1, 3, -11),
    Planet(17, -10, -8),
    Planet(-1, -15, 2),
    Planet(12, -4, -4),
]


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


visited_x = set()
visited_y = set()
visited_z = set()

while True:
    for planet_a in data:
        for planet_b in data:
            if planet_a != planet_b:
                planet_a.update_velocity(planet_b)

    hash_x = "|".join(
        [str(planet.X) for planet in data] + [str(planet.vX) for planet in data]
    )
    hash_y = "|".join(
        [str(planet.Y) for planet in data] + [str(planet.vY) for planet in data]
    )
    hash_z = "|".join(
        [str(planet.Z) for planet in data] + [str(planet.vZ) for planet in data]
    )

    if hash_x in visited_x and hash_y in visited_y and hash_z in visited_z:
        break
    if hash_x not in visited_x:
        visited_x.add(hash_x)
    if hash_y not in visited_y:
        visited_y.add(hash_y)
    if hash_z not in visited_z:
        visited_z.add(hash_z)

    for planet in data:
        planet.move()

part2 = lcm(len(visited_x), lcm(len(visited_y), len(visited_z)))
print(part1, part2)
