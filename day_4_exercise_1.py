# # 1. FizzBuzz 

# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz 

# So if number divided by 5 then Fizz If divided by 7 then Buzz,
#  If divided by 5 AND 7 then FizzBuzz otherwise the same number

#  Note: such a task became popular as the first task to ask to determine 
#  whether a person knows about programming at all smile

# start = 1
# end = 100
# final_list = ""

# for i in range(start,end+1):
#     if i%5==0:
#         final_list += "FIZZ"
#     if i%7==0:
#         final_list += "BUZZ"
#     if not (i%5==0 or i%7==0):
#         final_list += str(i)
#     if i!=end:
#         final_list += ","  #Any other way to add comma?
# print(final_list)

#  2. Christmas tree 

# Ask user to enter the height of the tree 

# Then Print the tree: Ex. height == 3 

# The printout would be: 

#   * 

#  *** 

# ***** 

# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

height = 0
 
while True:
    request = ("Enter positive number for Christmas three height or quit ('q'): ")
    if request == "q":
        break
    elif request[0].isalpha():
        print("Height can't be a letter ")
        continue 
    for i in range(height):
        print(" " * (height-1-i) + ("*" * i * 2)
              