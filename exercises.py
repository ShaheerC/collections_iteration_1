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

#1.1
print(coin_flip)

#1.2
print(fav_colors[0])

#1.3
fam_age.sort()
print(fam_age)

#1.4
fam_age.append(0)
print(fam_age)

#1.5
print(fav_movies['OldBoy'])

#EXERCISE 2
print("===START OF EXERCISE 2===")

#2.1
print(fav_colors[-1])

#2.2
city_pop ['Tokyo'] = 9273000
print(city_pop)

#2.3
coin_flip.reverse()
print(coin_flip)

#2.4
print(city_pop['Toronto'])

#2.5
for artist in artists:
    print("The band, {} is life changing.".format(artist))

#EXERCISE 3
print("===START OF EXERCISE 3===")

#3.1
print(artists[0:2])

#3.2
for key, val in fav_movies.items():
    print ("{} was released in {}.".format(key, val))

#3.3
print(fam_age)
fam_age.sort()
fam_age.reverse()
print(fam_age)

print(list(reversed(sorted(fam_age))))

#3.4
fav_movies ['Beauty and the Beast'] = 1991, 2017
print(fav_movies)

#EXERCISE4
print("===START OF EXERCISE 4===")

#4.1
for age in fam_age:
    if age < 30:
        print(age)

#4.2
print(max(fam_age))

#4.3
print(coin_flip.count('heads'))

#4.4
print(artists)
artists.pop(2)
print(artists)

#4.5
print(city_pop)
city_pop['Toronto'] = 3000000
print(city_pop)

#EXERCISE 5
print("===START OF EXERCISE 5===")

#5.1
population = 0
for pop in city_pop.values():
    population += pop
print(population)

#5.2
for friend ,friend_age in friends.items():
    if friend_age >= 30:
        print ("{} is old.".format(friend))
    else:
        print ("{} is young.".format(friend))

#5.3
print(fav_colors[1:3])

#5.4
for age_add, age in enumerate(fam_age):
    fam_age[age_add] = age + 1
print(fam_age)

#5.5
fav_colors.extend(('blue', 'yellow'))
print(fav_colors)

#EXERCISE 6
print("===START OF EXERCISE 6===")

#6.1
movies_by_year = {
1999 : ['The Matrix', 'Star Wars: Episode 1', 'The Mummy'],
2009 : ['Avatar', 'Star Trek', 'District 9'],
2019 : ['How to Train Your Dragon 3', 'Toy Story 4', 'Star Wars: Episode 9']
}
print(movies_by_year)

#6.2
phone_buttons = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
print(phone_buttons)

#6.3
country_info = [
    {
        'Name': 'Canada',
        'Continent': 'North America',
        'Island': False
    },
    {
        'Name': 'Italy',
        'Continent': 'Europe',
        'Island': False
    },
    {
        'Name': 'Indonesia',
        'Continent': 'Asia',
        'Island': True
    }
]
print(country_info)

#EXERCISE 7
print("===START OF EXERCISE 7===")

#7.1
for msg in range(20):
    print("I will not skateboard in the halls")

#7.2
msg_lists = []
for x in range(20):
    msg_lists.append("I will not skateboard in the halls")
print(msg_lists)

#7.3
numbers_lists = range(1,51)
for number in list(numbers_lists):
    print(number)

#7.4
total_numlist = 0
for number in numbers_lists:
    total_numlist += number
print(total_numlist)

#7.5
super_list = []
for sup in range (1,51): # This for loop will go through the code 50 times
    for y in range(3): # Will go through the loop till under but not above 3 times, before going back above and the above code runs a total 50 times.
        super_list.append(sup)
print (super_list)

#7.6
no_island = []
for variable in country_info:
    if variable['Island'] == False:
        no_island.append(variable)
print(no_island)
print(country_info)

#EXERCISE 8
print("===START OF EXERCISE 8===")

#8
expenses1 = [350.00, 450.00, 500.05, 505.55, 995.75, 1150,50]
expenses2 = [702.00, 475.55, 1400.05, 378.75, 900.50]

def sum_of_expenses(input_expense):
    total_expenses = 0
    for expense in input_expense:
        total_expenses += expense
    return total_expenses

print(sum_of_expenses(expenses1))
print(sum_of_expenses(expenses2))