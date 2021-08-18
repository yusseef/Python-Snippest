#Shallow copy: one level deep, only refrences in nested child objects
#deep copy: full indepentant copy
import copy
Org = [1, 2, 3]
cpy = Org #Will copy in place if we change in copy will change in original
cpy = copy.copy(Org) #Will copying it and if we change we will not change the original SHALLOW COPY
cpy = list(Org) #Will copying it and if we change we will not change the original SHALLOW COPY


