#!/usr/bin/python3
import os

os.system("clear")

t_G="\033[32m"
t_Y="\033[33m"
def_col="\033[0m" #- сбросить все до значений по умолчанию

str_line = input(f"\n{t_G}Напишите ( вставте ) переменные: {def_col}")

def fun_make_constructor(str_line):
        
    global list_clean 
    list_clean = []
    list_ignore_elements = ['->', 'self', '__init__', 'def', 'None:']
    dicionary  = ",.()"
    str_line_clean = ""

    for i in str_line:
        if i in dicionary:
            i = i.replace(i, " ")
        str_line_clean += i

    list_elements = str_line_clean.split()
    for i in range(len(list_elements)):
        if not list_elements[i] in list_ignore_elements:
            
            list_clean.append(list_elements[i])

    str_line = "" 
    for i in list_clean:
        str_line += i + ", "

    str_result = f"def __init__(self, {str_line}) -> None: \n"
    

    list_clean_L2 = []
    for element in list_clean:
        for i in element:
            if i == "=" and i != element[-1]:
                copy_element = element.split("=")
                list_clean_L2.append(copy_element[0])
                break
        else:
                list_clean_L2.append(element)

    list_clean = list_clean_L2 # Оставить т.к. "list_clean" используется в других методах
    
    for i in list_clean:
        str_result += f"\tself.__{i} = {i}\n"
        
    
    return str_result


print("\n",fun_make_constructor(str_line))

