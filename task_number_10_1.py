# Задание №1 - сделано
def count_points(win, draw, loss) -> int:
    total = win * 3 + draw + loss * 0
    return total


print(count_points(3, 2, 2))
