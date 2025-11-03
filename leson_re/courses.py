
r'''
    Regular expression
    . : any char
    [a-z] : interval lower case char
    [uX] : u or X
    (expr)? :expr optionnal
    (expr)* : expr 0 or n times
    (expr)+ : expr 1 or n times
    (expr){n,m} : expr between n and m times
    (expr1|expr2) : expr1 or expr2
    (expr)$ :end with expr
    ^(expr) : start with expr
    \d : digit [0-9]
    \w : char
    \s : space or \t or \n
    \D : not \d
    \W : not \w
    \S : not \s
'''
import re,os
from os import path
from re import Match
def extract(url:str)->list[str]:
    emails:list[str]=[]
    try:
        with open(url) as f:
            data:str=f.read()
            results=re.finditer(r'((\w)+(\.)?(\w|\d)*)@((\w|\d)+(\.(\w|\d)+)*(\.)(\w{2,3}))',data)
            for match in results:
                
                emails.append(match.group(1))
                emails.append(match.group(5))
            r""" match:Match[str]|None=re.search(r'(\d){4}',data)
            assert match,'year not found'
            print(match.group()) """
            """ if match !=None:
                print(match.group())
            else:
                print('year not found') """
    except FileNotFoundError as e:
        print(f'{url} not found')
    return emails

if __name__=='__main__':
    print(extract('C:/Users/yy064/Desktop/python/3rd year/python avance/leson_re/data.csv'))