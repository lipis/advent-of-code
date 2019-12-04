def validate_part1(password):
    same = False
    increase = True
    last_char = "0"
    for char in str(password):
        if char == last_char:
            same = True
        if last_char > char:
            increase = False
            break
        last_char = char
    return same and increase


def validate_part2(password):
    same = {}
    increase = True
    last_char = "0"
    for char in str(password):
        if char == last_char:
            if char not in same:
                same[char] = 1
            same[char] += 1
        if last_char > char:
            increase = False
            break
        last_char = char

    group = False
    for char in same:
        if same[char] == 2:
            group = True
            break

    return increase and group


part1 = 0
part2 = 0
for password in range(254032, 789860):
    if validate_part1(password):
        part1 += 1
    if validate_part2(password):
        part2 += 1

print part1, part2
