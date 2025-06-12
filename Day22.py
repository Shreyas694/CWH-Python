# Sets 31 cwh
s = {2, 3, 3, 34, 4, 2, 8}
print(s)
# sets eliminates the duplicates
# sets are unchangeable,order may or may not be mentained
info = {"carla", 18, True, 7.9, 4, 6, 89}
print(info)

shreyas = {}
print(type(shreyas))  # dic

shreyas = set()
print(type(shreyas))  # set

# set methods 32 cwh
s1 = {1, 2, 4, 6, 3, 8, 9}
s2 = {3, 5, 6, 2, 32, 89}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

cities = {"Tokyo", "Madrid", "Delhi", "Kabul", "Moscow"}
cities_1 = {"Seoul", "Shanghai", "Bankok", " Moscow", "Tokyo"}
cities.update(cities_1)  # Update gives union and the set we are calling
print(cities, cities_1)
cities_2 = cities.union(cities_1)
print(cities_2)

print(cities.intersection(cities_1))
cities.intersection_update(cities_1)
print(cities)

# symmetric_difference is the value which is not common in both the set
cities_3 = cities.symmetric_difference(cities_1)
print(cities_3)

cities_4 = cities.difference(cities_1)
print(cities_4)

# isdisjoint indicate that there is no elements in common
print(cities.isdisjoint(cities_1))

# Superset the set where one set has every values of another set
print(cities.issuperset(cities_1)) # True
print(cities_1.issubset(cities)) # True

# Superset is a reverse of subset 
