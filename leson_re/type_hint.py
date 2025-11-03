"""
augmenter la lisibilité du code
checker les erreurs de types avant l'execution
"""
s: str = 3
x: float = True
a: int = 10
b: bool = False
print(a)
"""
auther: yassine
date:07/01/2025
description: 
    calculer la factorielle
args: 
    - n int
return : factorial
"""
def fact(n: int) -> int:
    f = 1
    for i in range (1,n):
        f = f*i
    return f

cities:list[str]
cities=["fes","rabat",10]
payment:tuple[str,...]=("cheque","cash",10)
score:dict[str,float]={"a":20,"b":3.4,"c":True,2:1}
def findUserByName(name:str)->str|None:
    return None
from typing import Final,Any
MAX : Final[int] = 36
MAX = 37
var : Any 
var = 1
var = True
var = "yassine"
Vector = list[float]
v:Vector=[1,2]
w:Vector=[3,4]
AnyVector = list[object]
s:AnyVector=["",1,True,[]]



s = str(fact(5))