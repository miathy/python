import matplotlib.pyplot as plt 
plt.scatter(2,4, s=50)

squares = [1,4,9,16,25]
plt.plot(squares, linewidth=1)
plt.title(' Square Numbers', fontsize=20)
plt.xlabel('Value', fontsize=14)
plt.ylabel("Square of Value", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
