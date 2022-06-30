from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'Japan', 36.9, (35.390, 139.69))

print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)

# get the fields of the named tuple
print(City._fields)

# example of using _make function using existing data
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.61, 77.20)) # data in a tuple
delhi = City._make(delhi_data) # cool!
print("--- PRINTING DELHI EXAMPLE ---")
for key, value in delhi._asdict().items():
    print(key + ':', value)