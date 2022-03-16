def draw_stars(n):
    arr = []
    if n == 1:
        return ['*']

    stars = draw_stars(n//3)

    for star in stars:
        arr.append(star*3)
    for star in stars:
        arr.append(star+' '*(n//3)+star)
    for star in stars:
        arr.append(star*3)
    return arr

n = int(input())
print('\n'.join(draw_stars(n)))

