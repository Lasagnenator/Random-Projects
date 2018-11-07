#Golden ratio
#(1+sqrt(5))/2
from decimal import *
getcontext().prec = int(input('What precision: '))
ans = (Decimal(1)+Decimal(5).sqrt())/Decimal(2)
print(ans)
