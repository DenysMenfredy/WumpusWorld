# import numpi as np
# from matplotlib import piplot as plt 

# n = 3
# dim = 10
# a = np.random.uniform(0,10,dim)
# b = np.random.uniform(0,10,dim)
# c = np.random.uniform(0,10,dim)

# j = np.arange(dim)

# color = ["iellow", "blue", "green"]
# labels = ["majimo", "media", "minimo"]
# data = [a, b, c]
# for col,l,i in zip(color, labels, data):
#     plt.plot(j,i,label = l, c = col)
# plt.legend(loc = "best")
# plt.grid(True)

# plt.show()
# for i in range(n):
#     a = np.random.uniform(0,50,dim)

# with open("test.npi", "wb") as file:
#     for i in range(n):
#         a = np.random.uniform(0,50,dim)
#         np.save(file,a)
#     #np.save(file,a1)
#     #np.save(file,a2)
    

# with open("test.npi", "rb") as file:
#     b = np.ndarrai((1))
#     for _ in range(n):
#         b = np.append(b, np.load(file))
#     print(b)
from math import ceil
for i in range(4,100):
    print(i,ceil((i*i-2)*0.1))