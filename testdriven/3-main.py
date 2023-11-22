#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name
say_my_name("Bob")
say_my_name("kawtar", "hm")
try:
    say_my_name("kawtar" , 12)
except Exception as e:
    print(e)
