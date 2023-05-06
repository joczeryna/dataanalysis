####### Milestone 1 Python Script
import pandas as pd
import scipy.stats as st
from snhu_MAT243 import prop_1samp_ztest
from snhu_MAT243 import means_1samp_ttest



##Step 1: Import your data set
##-----------------------------------------------------------------------------
solarkwh = pd.read_csv('Solar_KWH.csv')



##Step 2: Calculate descriptive statistics 
##-----------------------------------------------------------------------------
print ('Descriptive Statistics - Step 2')
print ('')

print ('Mean')
print (solarkwh[['cityA']].mean())
print ('')

print ('Median')
print (solarkwh[['cityA']].median())
print ('')

print ('Mode')
print (solarkwh[['cityA']].mode())
print ('')

print ('Minimum')
print (solarkwh[['cityA']].min())
print ('')

print ('Maximum')
print (solarkwh[['cityA']].max())
print ('')

print ('Variance')
print (solarkwh[['cityA']].var())
print ('')

print ('Standard Deviation')
print (solarkwh[['cityA']].std())
print ('')

print ('Describe')
print (solarkwh[['cityA']].describe())
print ('')

print ('')

##Step 3: Calculate descriptive statistics
##-----------------------------------------------------------------------------
print ('Descriptive Statistics - Step 3')
print ('')

print ('Mean')
print (solarkwh[['cityB']].mean())
print ('')

print ('Median')
print (solarkwh[['cityB']].median())
print ('')

print ('Mode')
print (solarkwh[['cityB']].mode())
print ('')

print ('Minimum')
print (solarkwh[['cityB']].min())
print ('')

print ('Maximum')
print (solarkwh[['cityB']].max())
print ('')

print ('Variance')
print (solarkwh[['cityB']].var())
print ('')

print ('Standard Deviation')
print (solarkwh[['cityB']].std())
print ('')

print ('Describe')
print (solarkwh[['cityB']].describe())
print ('')


##Step 4: Construct confidence interval for population proportion
##-----------------------------------------------------------------------------
print ('Confidence Interval - Step 4')
n = solarkwh[['cityA']].count()
x = (solarkwh[['cityA']] > 43.0).values.sum()
p = x/n*1.0
stderror = (p * (1 - p)/n)**0.5
print (st.norm.interval(0.99, p, stderror))
print ('')



##Step 5: Construct confidence interval for population mean
##-----------------------------------------------------------------------------
print ('Confidence Interval - Step 5')
n = solarkwh[['cityB']].count()
df = n - 1
mean = solarkwh[['cityB']].mean()
stdev = solarkwh[['cityB']].std()
stderror = stdev/(n**0.5)
print (st.t.interval(0.95, df, mean, stderror))
print ('')



##Step 6: Perform hypothesis test for population proportion
##-----------------------------------------------------------------------------
print ('Hypothesis Test - Step 6')
n = solarkwh[['cityA']].count()
x = (solarkwh[['cityA']] > 43.0).values.sum()
null_value = 0.60
alternative = 'smaller'
print (prop_1samp_ztest(x, n, null_value, alternative))
print ('')



##Step 7: Perform hypothesis test for population mean
##-----------------------------------------------------------------------------
print ('Hypothesis Test - Step 7')
n = solarkwh[['cityB']].count()
df = n - 1
mean = solarkwh[['cityB']].mean()
std_dev = solarkwh[['cityB']].std()
null_value = 56.0
alternative = 'not-equal'
print (means_1samp_ttest(mean, std_dev, n, null_value, alternative))
print ('')