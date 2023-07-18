inmport pickle

with open('testl.pkl', 'wb' ) as f:
    my_list = list(range(1,11))
    pickle.dump(my_list, f)
