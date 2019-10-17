import pickle
with open('pickled_fruit.pkl', 'rb') as file:
    #read only in binary : rb 
    data = pickle.load(file)
print(data)
print(type(data))