import pickle


def save_pkl(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)

def read_pkl(path):
    with open(path, 'rb') as f:
        return pickle.load(f)