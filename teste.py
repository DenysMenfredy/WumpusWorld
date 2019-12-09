# import numpy as np
# from matplotlib import pyplot as plt 

# n = 3
# dim = 10
# a = np.random.uniform(0,10,dim)
# b = np.random.uniform(0,10,dim)
# c = np.random.uniform(0,10,dim)

# x = np.arange(dim)

# color = ["yellow", "blue", "green"]
# labels = ["maximo", "media", "minimo"]
# data = [a, b, c]
# for col,l,y in zip(color, labels, data):
#     plt.plot(x,y,label = l, c = col)
# plt.legend(loc = "best")
# plt.grid(True)

# plt.show()
# for i in range(n):
#     a = np.random.uniform(0,50,dim)

# with open("test.npy", "wb") as file:
#     for i in range(n):
#         a = np.random.uniform(0,50,dim)
#         np.save(file,a)
#     #np.save(file,a1)
#     #np.save(file,a2)
    

# with open("test.npy", "rb") as file:
#     b = np.ndarray((1))
#     for _ in range(n):
#         b = np.append(b, np.load(file))
#     print(b)
