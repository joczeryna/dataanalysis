####### Milestone 3 Python Script
import pandas as pd
import scipy.stats as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")



##Step 1: Import your data set
##-----------------------------------------------------------------------------
solarkwh = pd.read_csv('Solar_KWH.csv')

####### Step 2: Analysis of Variance for five population means
##----------------------------------------------------------------------------------------------------------------
print ('Analysis of Variance for five population means - Step 2')
may_data = solarkwh.loc[solarkwh['Month'] == 5]['cityA']
jun_data = solarkwh.loc[solarkwh['Month'] == 6]['cityA']
jul_data = solarkwh.loc[solarkwh['Month'] == 7]['cityA']
aug_data = solarkwh.loc[solarkwh['Month'] == 8]['cityA']
sep_data = solarkwh.loc[solarkwh['Month'] == 9]['cityA']
print (st.f_oneway(may_data, jun_data, jul_data, aug_data, sep_data))
print ('')


####### Step 3: Analysis of Variance for six population means
##----------------------------------------------------------------------------------------------------------------
print ('Analysis of Variance for six population means - Step 3')
jul_data = solarkwh.loc[solarkwh['Month'] == 7]['cityB']
aug_data = solarkwh.loc[solarkwh['Month'] == 8]['cityB']
sep_data = solarkwh.loc[solarkwh['Month'] == 9]['cityB']
print (st.f_oneway(jul_data, aug_data, sep_data))
print ('')


####### Step 4: Plot boxplots to evaluate any significant differences (5 Means).
##----------------------------------------------------------------------------------------------------------------
print ('Boxplots for five population means - Step 4 (NOTE: Boxplots will be saved in a file called step4_5_means.png)')
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib as mpl
import matplotlib.pyplot as plt
may_data = solarkwh.loc[solarkwh['Month'] == 5]['cityA']
jun_data = solarkwh.loc[solarkwh['Month'] == 6]['cityA']
jul_data = solarkwh.loc[solarkwh['Month'] == 7]['cityA']
aug_data = solarkwh.loc[solarkwh['Month'] == 8]['cityA']
sep_data = solarkwh.loc[solarkwh['Month'] == 9]['cityA'] 
data = [may_data, jun_data, jul_data, aug_data, sep_data]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(data)
plt.xticks([1, 2, 3, 4, 5], ['May', 'Jun', 'Jul', 'Aug', 'Sep'])
fig.savefig('step4_5_means.png')
print ('')


####### Step 5: Plot boxplots to evaluate any significant differences (3 Means).
##----------------------------------------------------------------------------------------------------------------
print ('Boxplots for five population means - Step 5 (NOTE: Boxplots will be saved in a file called step5_3_means.png)')
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib as mpl
import matplotlib.pyplot as plt
jul_data = solarkwh.loc[solarkwh['Month'] == 7]['cityB']
aug_data = solarkwh.loc[solarkwh['Month'] == 8]['cityB']
sep_data = solarkwh.loc[solarkwh['Month'] == 9]['cityB'] 
data = [jul_data, aug_data, sep_data]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(data)
plt.xticks([1, 2, 3], ['Jul', 'Aug', 'Sep'])
fig.savefig('step5_3_means.png')