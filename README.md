# remove_all_comments

Input: a python file my_code.py:

------------------------------------------

"""

This is a test code

 
"""

def main():

    # This is a comment
    
    print('Hello, world')
    
    return
 
# end of file

------------------------------------------
 
 
Please implement a method that removes all the comments and save to my_new_code.py:

1) lines starts with # (note that end of line comment is not allowed)

3) blocks between """ (note that """ can only be placed at beginning of a line or stands by itself)

 
Output:

------------------------------------------

def main():

    print('Hello, world')
    
    return
 
------------------------------------------
