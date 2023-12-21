"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The title() method changes each word to title case, where each word begins with a capital letter
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
name = "ada lovelace"
print(name.title())

print(name.upper())
print(name.lower())

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# To insert a variable’s value into a string, place the letter f immediately. Put braces around the name or names of any 
# variable you want to use inside the string. Python will replace each variable with its value when the string is displayed
# before the opening quotation mark
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
# print(f"{first_name} {last_name}")
print(f"Hello, {full_name.title()}")

favorite_language = ' python '
print(favorite_language)
favorite_language = favorite_language.rstrip() # rstrip() to remove white space from right side
favorite_language = favorite_language.lstrip() # lstrip() to remove white space from left side
favorite_language = favorite_language.strip()  #strip() to remove white space from both side
print(favorite_language)