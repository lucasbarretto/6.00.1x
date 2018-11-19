#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:33:04 2018

@author: josebarretto
"""

file = open("curriculum.txt", "w+")


print('CURRICULUM GENERATOR:')
print('----------------------------------------------------')


name = input('Please enter your full name: ')
print()
education = input('Describe your education level (high school, college, ...): ')
print()
languages = input('Enlist the languages that you speak: ')
print()
experience = input('Describe your previous professional experiences: ')
print()
extra = input('Tell me about your extracurricular activities (hobbies, sports, ...): ')
print()

file.write("CURRICULUM VITAE: " + name + "\n\n")
file.write("-----------------------------------------------")
file.write("\n\n")
file.write("EDUCATION:\n\n")
file.write(education)
file.write("\n\n")
file.write("-----------------------------------------------")
file.write("\n\n")
file.write("LANGUAGES SPOKEN:\n\n")
file.write(languages)
file.write("\n\n")
file.write("-----------------------------------------------")
file.write("\n\n")
file.write("PROFESSIONAL EXPERIENCE:\n\n")
file.write(experience)
file.write("\n\n")
file.write("-----------------------------------------------")
file.write("\n\n")
file.write("EXTRA-CURRICULAR ACTIVITIES:\n\n")
file.write(extra)
file.write("\n\n")
file.write("-----------------------------------------------")

file.close()

print("That's it! Thanks for using the Curriculum Generator!")




