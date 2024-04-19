"""
Specifications
    Accept an input from the user
    Determine the person’s grade or that they are an adult
       2,  If the person is over 18, they are considered an adult
        If the person is older than 3 but younger than 6, they are in preschool.
       1, The person is in high school if they are 14 or older, but not yet an adult.
        If the person is older than 10, and not in high school, they are in middle school.
        If the person is less than 4 years old, they are an infant.
        The remaining ages are in grade school.

    Print the result
       1,  “The person is 14 years old and in high school.”
       2,  “The person is 30 years old and an adult”
        "the person is 5 years old and in preschool"
        “The person is 3 years old and an infant”
        "The person is 11 years old and in middle school"
        "The person is 7 years old and in grade school"

    Process Builders -
        - Refer to yours or some other source of working code that is similar.
        - Plan before you build; pseudo code
        - Ideally, each student will have their own copy with 1 student sharing 
            their screen and everyone working together to decide the code you will all use.

"""
is_active = True

while is_active:

    user_input = input("Age: ")
    
    if user_input == "quit":
        is_active = False
        continue # skip everything to the end of the while loop; is_active is evaluated at the end of each loop

    age = int(user_input)

    # Your code goes here #
    if age < 18  > 17:
        print(f"The person is {age} years old and an adult") 
    elif age > 14 > 13 :
        print(f"The person {age} years old and in High School!")
      
    else:
        print("Hello")

    
print("Have A Nice Day!")
