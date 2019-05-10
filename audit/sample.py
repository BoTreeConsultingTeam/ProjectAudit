from .models import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
 
# data
def xyz():
	df=Audits.objects.all().values('date','average_rating')
	print(df)
 # plot
#plt.plot( 'x', 'y', data=df, linestyle='-', marker='o')
#plt.show()