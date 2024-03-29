import math

data = [
    ".#..#..##.#...###.#............#.",
    ".....#..........##..#..#####.#..#",
    "#....#...#..#.......#...........#",
    ".#....#....#....#.#...#.#.#.#....",
    "..#..#.....#.......###.#.#.##....",
    "...#.##.###..#....#........#..#.#",
    "..#.##..#.#.#...##..........#...#",
    "..#..#.......................#..#",
    "...#..#.#...##.#...#.#..#.#......",
    "......#......#.....#.............",
    ".###..#.#..#...#..#.#.......##..#",
    ".#...#.................###......#",
    "#.#.......#..####.#..##.###.....#",
    ".#.#..#.#...##.#.#..#..##.#.#.#..",
    "##...#....#...#....##....#.#....#",
    "......#..#......#.#.....##..#.#..",
    "##.###.....#.#.###.#..#..#..###..",
    "#...........#.#..#..#..#....#....",
    "..........#.#.#..#.###...#.....#.",
    "...#.###........##..#..##........",
    ".###.....#.#.###...##.........#..",
    "#.#...##.....#.#.........#..#.###",
    "..##..##........#........#......#",
    "..####......#...#..........#.#...",
    "......##...##.#........#...##.##.",
    ".#..###...#.......#........#....#",
    "...##...#..#...#..#..#.#.#...#...",
    "....#......#.#............##.....",
    "#......####...#.....#...#......#.",
    "...#............#...#..#.#.#..#.#",
    ".#...#....###.####....#.#........",
    "#.#...##...#.##...#....#.#..##.#.",
    ".#....#.###..#..##.#.##...#.#..##",
]

asteroids = []


def angle(point1, point2):
    result = (
        math.atan2(point2[1] - point1[1], point2[0] - point1[0]) * 180 / math.pi + 90
    ) % 360
    return round(result, 2)


for y, row in enumerate(data):
    for x, pos in enumerate(row):
        if pos == "#":
            asteroids.append((x, y))

angles = set()
part1 = 0
station = asteroids[0]

for asteroid1 in asteroids:
    angles = set()
    for asteroid2 in asteroids:
        if asteroid1 != asteroid2:
            angles.add(angle(asteroid1, asteroid2))
    if part1 < len(angles):
        part1 = len(angles)
        station = asteroid1


def dist(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


angles = {}
for asteroid in asteroids:
    if station != asteroid:
        angle_ = angle(station, asteroid)
        if angle_ not in angles:
            angles[angle_] = asteroid
            continue
        if dist(station, angles[angle_]) > dist(station, asteroid):
            angles[angle_] = asteroid


key200 = sorted(angles.keys())[199]
part2 = angles[key200][0] * 100 + angles[key200][1]

print(part1, part2)
