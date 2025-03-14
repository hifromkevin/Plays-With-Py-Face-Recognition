import pickle

with open('faces.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)