for i in range (0,101):
    if i%10 == 1:
        print (i)

efrain_item = 10
print (efrain_item)
print (type(efrain_item))

print (str(efrain_item))
add_0 = len(str(efrain_item))
print (add_0)
if add_0 == 1:
    print ("0"+str(efrain_item))
else:
    print (efrain_item)