import pickle
print('Load dataset..', flags_obj.pickle_path)
dataset = pickle.load(open(flags_obj.pickle_path, 'rb'))