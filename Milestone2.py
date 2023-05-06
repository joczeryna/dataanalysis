####### Milestone 2 Python Script
import pandas as pd
import scipy.stats as st
from snhu_MAT243 import prop_1samp_ztest
from snhu_MAT243 import means_1samp_ttest
from statsmodels.stats.proportion import proportions_ztest


##Step 1: Import your data set
##-----------------------------------------------------------------------------
solarkwh = pd.read_csv('Solar_KWH.csv')

####### Step 2: Perform hypothesis test for the difference of two population proportions
##-------------------------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population proportions - Step 2')
n1 = solarkwh.loc[solarkwh['Month'] == 6]['cityA'].count()
n2 = solarkwh.loc[solarkwh['Month'] == 7]['cityA'].count()
x1 = (solarkwh.loc[solarkwh['Month'] == 6]['cityA'] > 44.4).values.sum()
x2 = (solarkwh.loc[solarkwh['Month'] == 7]['cityA'] > 44.4).values.sum()
counts = [x1, x2]
n = [n1, n2]
print (proportions_ztest(counts, n))
print ('')

####### Step 3: Perform hypothesis test for the difference of two population proportions
##-------------------------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population proportions - Step 3')
n1 = solarkwh.loc[solarkwh['Month'] == 6]['cityB'].count()
n2 = solarkwh.loc[solarkwh['Month'] == 7]['cityB'].count()
x1 = (solarkwh.loc[solarkwh['Month'] == 6]['cityB'] > 55.2).values.sum()
x2 = (solarkwh.loc[solarkwh['Month'] == 7]['cityB'] > 55.2).values.sum()
counts = [x1, x2]
n = [n1, n2]
print (proportions_ztest(counts, n))
print ('')

####### Step 4: Perform hypothesis test for the difference of two population means
##----------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population means - Step 4')
jul_data = solarkwh.loc[solarkwh['Month'] == 6]['cityA']
aug_data = solarkwh.loc[solarkwh['Month'] == 7]['cityB']
print (st.ttest_ind(jul_data, aug_data, equal_var=False))
print ('')


####### Step 5: Perform hypothesis test for the difference of two population means
##----------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population means - Step 5')
feb_data = solarkwh.loc[solarkwh['Month'] == 2]['cityA']
aug_data = solarkwh.loc[solarkwh['Month'] == 8]['cityB']
print (st.ttest_ind(feb_data, aug_data, equal_var=False))
print ('')
