#%%
import matplotlib.pyplot as plt

#%%
x=[1,2,3,4]
y=[10,24,50,69]
x1=[2,4,6,8]
y1=[10,2,24,60]

# create a figure and axis handle using "plt.subplots" fn
fig, ax = plt.subplots()
la1, = ax.plot(x,y)
la2, = ax.plot(x1,y1)

# set title
ax.set_title('Basic Title')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
# to name a line
la1.set_label('Awesome Line')
la2.set_label('Normal Line')

ax.legend(loc='best')

#%%
plt.show()


# %%
