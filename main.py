#task_3
#random_password_generator
from random import *
print("*"*80)
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=}{[]?/\|~`"
pas_len=int(input("Please, enter number of characters you want for this password: "))
for x in range(0,pas_len+1):
    print(f"{choice(chars)}" ,end="")
print(f"\n Thanks for using...")
print("*"*80)