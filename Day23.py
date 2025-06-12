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

