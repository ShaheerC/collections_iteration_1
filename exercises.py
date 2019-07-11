#EXERCISE 0

#LISTS

fav_colors = ['purple', 'black', 'grey']
fam_age = [28, 64, 68, 34]
coin_flip = ['heads', 'heads', 'heads', 'tails', 'heads']
artists = ['tool', 'wutang', 'sigurros']

#DICTIONARIES

definitions = {
    'python': 'a big snake',
    'cat': 'fluffy friend',
    'sheep': 'like a cloud'
}
fav_movies = {
    'City of God': 2002,
    'OldBoy': 2003,
    'Interstellar': 2014
}
city_pop = {
    'Toronto': 2930000,
    'Boston': 685094,
    'Dhaka': 8906000
}
friends = {
    'Ricky': 29,
    'Hirad': 28,
    'Atindra': 31
}

#EXERCISE 1
print("===START OF EXERCISE 1===")

print(coin_flip)

print(fav_colors[0])

fam_age.sort()
print(fam_age)

fam_age.append(0)
print(fam_age)

print(fav_movies['OldBoy'])

#EXERCISE 2
print("===START OF EXERCISE 2===")

print(fav_colors[-1])

city_pop ['Tokyo'] = 9273000
print(city_pop)

coin_flip.reverse()
print(coin_flip)

print(city_pop['Toronto'])

for artist in artists:
    print("The band, {} is life changing.".format(artist))

#EXERCISE 3
print("===START OF EXERCISE 3===")

print(artists[0:2])

for key, val in fav_movies.items():
    print ("{} was released in {}.".format(key, val))

print(fam_age)
fam_age.sort()
fam_age.reverse()
print(fam_age)

print(list(reversed(sorted(fam_age))))

fav_movies ['Beauty and the Beast'] = 1991, 2017
print(fav_movies)

#EXERCISE4
print("===START OF EXERCISE 4===")