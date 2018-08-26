#Function removes : or - characters from a set of times and replace them for . character
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

#Function opens a file, reads each line and returns a string removing white spaces and splitting the string every comma
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as err:
        print("Error: " + str(err))
        return(None)

#Replaced for get_coach_data function
"""try:
	
	with open("james.txt") as james_file:
		data = james_file.readline()
		james = data.strip().split(',')
	with open("julie.txt") as julie_file:
		data = julie_file.readline()
		julie = data.strip().split(',')
	with open("mikey.txt") as mikey_file:
		data = mikey_file.readline()
		mikey = data.strip().split(',')
	with open("sarah.txt") as sarah_file:
		data = sarah_file.readline()
		sarah = data.strip().split(',')"""

james = get_coach_data("james.txt")
julie = get_coach_data("julie.txt")
mikey = get_coach_data("mikey.txt")
sarah = get_coach_data("sarah.txt")

#List comprehension used to sort and sanitize the lists
#Changed for set factory function
"""james = sorted([sanitize(t) for t in james])
	julie = sorted([sanitize(t) for t in julie])
	mikey = sorted([sanitize(t) for t in mikey])
	sarah = sorted([sanitize(t) for t in sarah])

        unique_james = []
	for each_t in james:
		if each_t not in unique_james:
			unique_james.append(each_t)
	print(unique_james[0:3])

	unique_julie = []
	for each_t in julie:
		if each_t not in unique_julie:
			unique_julie.append(each_t)
	print(unique_julie[0:3])

	unique_mikey = []
	for each_t in mikey:
		if each_t not in unique_mikey:
			unique_mikey.append(each_t)
	print(unique_mikey[0:3])

	unique_sarah = []
	for each_t in sarah:
		if each_t not in unique_sarah:
			unique_sarah.append(each_t)
	print(unique_sarah[0:3])"""

#List comprehension avoided the use of extra lists
"""clean_james = []
	clean_julie = []
	clean_mikey = []
	clean_sarah = []"""

#This block was subtituted for list comprehesion in the printing block
"""for each_t in james:
		clean_james.append(sanitize(each_t))
	for each_t in julie:
		clean_julie.append(sanitize(each_t))
	for each_t in mikey:
		clean_mikey.append(sanitize(each_t))
	for each_t in sarah:
		 clean_sarah.append(sanitize(each_t))"""

#Used list comprehension
"""print(sorted([sanitize(t) for t in james]))
	print(sorted([sanitize(t) for t in julie]))
	print(sorted([sanitize(t) for t in mikey]))
	print(sorted([sanitize(t) for t in sarah]))"""
	
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])

print(james)
print(julie)
print(mikey)
print(sarah)

#Removed and added in the get_coach_data function
"""except IOError as err:
		print("File error: " + str(err))"""
