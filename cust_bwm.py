# customers best, moderate and worst based on categories
import pandas
import pickle

data = pickle.load(open('pcat.p', 'rb'))
last3 = pickle.load(open('last3mon.p', 'rb'))

off_b = []
off_m = []
off_w = []
fur_b = []
fur_m = []
fur_w = []
tec_b = []
tec_m = []
tec_w = []

h1=last3[:370]
h2=last3[370:1500]
h2 = h2.reset_index(drop = True)
h3=last3[1500:]
h3 = h3.reset_index(drop = True)

for i in range(len(h1)):
    
    if h1['d_category'][i] == 'Office Supplies':
        off_b.append(h1['d_product'][i])
    elif h1['d_category'][i] == 'Furniture':
        fur_b.append(h1['d_product'][i])
    else:
        tec_b.append(h1['d_product'][i])

for i in range(len(h2)):
    if h2['d_category'][i] == 'Office Supplies':
        off_m.append(h2['d_product'][i])
    elif h2['d_category'][i] == 'Furniture':
        fur_m.append(h2['d_product'][i])
    else:
        tec_m.append(h2['d_product'][i])
        
for i in range(len(h3)):
    if h3['d_category'][i] == 'Office Supplies':
        off_w.append(h3['d_product'][i])
    elif h3['d_category'][i] == 'Furniture':
        fur_w.append(h3['d_product'][i])
    else:
        tec_w.append(h3['d_product'][i])
        
off = [sorted(off_b),sorted(off_m),sorted(off_w)]
fur = [sorted(fur_b),sorted(fur_m),sorted(fur_w)]
tec = [sorted(tec_b),sorted(tec_m),sorted(tec_w)]

pickle.dump(off,open("off_prod.p", "wb"))
pickle.dump(fur,open("fur_prod.p", "wb"))
pickle.dump(tec,open("tec_prod.p", "wb"))