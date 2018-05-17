import pickle

data = pickle.load(open('data.p', 'rb'))

cust = {}


for i in range(len(data)):
    cust[data['Customer ID'][i]]=data['Customer Name'][i]

pickle.dump(cust, open('cust_idname.p', 'wb'))   