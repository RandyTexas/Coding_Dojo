# # 1
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# x[1][0] = 15
# print(x)
# students[0]['last_name'] = 'Bryant'
# print(students[0]['last_name'])

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'][0])

# z = [ {'x': 10, 'y': 20} ]
# z[0]['x'] = 20
# z[0]['y'] = 30
# print(z)



# # 2 
# def iterateDictionary(some_list):
#     for dictionary in some_list:
#         print(f"first_name - {dictionary['first_name']}, last_name - {dictionary['last_name']}")

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# iterateDictionary(students) 
# # # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel


# # 3
# def iterateDictionary2(key_name, some_list):
#     for dictionary in some_list:
#         if key_name in dictionary:
#             print(dictionary[key_name])

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# # Example usage:
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# # 4
# def printInfo(some_dict):
#     for key in some_dict:
#         print(f"{key} ({len(some_dict[key])})")
#         for item in some_dict[key]:
#             print(item)
#         print()  # Adds an empty line for better readability

# dojo = {
# 'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
# 'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# printInfo(dojo)


# # output:
# # 7 LOCATIONS
# # San Jose
# # Seattle
# # Dallas
# # Chicago
# # Tulsa
# # DC
# # Burbank
    
# # 8 INSTRUCTORS
# # Michael
# # Amy
# # Eduardo
# # Josh
# # Graham
# # Patrick
# # Minh
# # Devon
