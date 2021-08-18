import shelve

with shelve.open("FileIO\Shelf") as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['lapple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow, citrus fruit"
    fruit['grape'] = "a small, sweet frruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])