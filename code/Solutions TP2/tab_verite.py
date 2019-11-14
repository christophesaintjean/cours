b1 = True
b2 = True
tab_TT = (b1 == True and b2 == False) or (b1 == False and b2 == True)
## version courte
## tab_TT = (b1 and not b2) or (not b1 and b2)

b1 = True
b2 = False
tab_TF = (b1 == True and b2 == False) or (b1 == False and b2 == True)
b1 = False
b2 = True
tab_FT = (b1 == True and b2 == False) or (b1 == False and b2 == True)
b1 = False
b2 = False
tab_FF = (b1 == True and b2 == False) or (b1 == False and b2 == True)

print('b2 \\ b1 |', True, ' |', False)
print('-'*22)
print(True,  '   |', tab_TT, '|', tab_FT)
print(False,  '  |', tab_TF, ' |', tab_FF)

# cet operateur est le ou exclusif (xor)
# il peut s'écrire simplement  b1 != b2

