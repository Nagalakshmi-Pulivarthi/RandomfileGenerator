import random
import string
# 1.Generate a random string of 10 characters
random_string="".join(random.choices(string.ascii_letters+string.digits,k=10))
random_string_text="".join(random.choices(string.ascii_letters,k=100))
# Define the filename by using a random string
file_name=f"{random_string}.txt"
# 3.Create and open a file 
with open (file_name,"w") as file:
    file.write(random_string_text)
print(f"File '{file_name}' has been created with the content: '{random_string_text}' ")    
