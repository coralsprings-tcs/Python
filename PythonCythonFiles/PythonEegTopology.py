#whatever you set the EEG file to in directory in .edf format
#import modules that reads EEG and make into usable array import mne
import numpy as np
from numpy import mean
from numpy import std
from itertools import product
from sklearn import datasets
from scipy.stats import multivariate_normal as mvn
from scipy import stats
from sklearn.decomposition import PCA
from ripser import Rips 
from persim import PersImage
import matplotlib.pyplot as plt
import mne

file = 'dummyData.txt'
data = mne.io.read_raw_edf(file) 
raw_data = data.get_data()
info = data.info
channels = data.ch_names 
transf_data = raw_data.transpose()
#shape of array
#assess how many data points are within array config_data = raw_data.shape
#--------
#print('The shape of the data is '+repr(transf_data)) 

#transpose data for use in subsequent calculations transf_data=raw_data.transpose() 
#des_len can be changed depending on how many data points are desired
#this may be useful if quick calculations are desired (sampling of EEG as opposed to using whole thing)
des_len=200
edf_data=transf_data[0:des_len] 
#change threshold as desired
#a value of 0.95 indicates channels that contribute to 95% of PCA
#ideally use two to three channels for quicker results (threshold = 0.95 - 0.99)
#this is useful only with normal EEGs as it is assumed normal EEGs will have similar channel patterns while seizures can have only several channel patterns be abnormal
threshold = 0.95

pca = PCA(threshold).fit(transf_data)
components = pca.transform(transf_data)
filtered = pca.inverse_transform(components)
edf_data = filtered

#Lets you know how many channels can be used with transformed components print('The number of channels that were used was '+repr(pca.n_components_)) 
#Rips complex for EEG
#this will save a text file of (birth, death) for analysis of the persistent homology in EEG to the desktop
#the savetxt is set to work with Macs
#the file path needed to successfully save is different with Windows 
def r_complex(edf_data): 
    rips = Rips()
    dgms = rips.fit_transform(edf_data) 
#    np.savetxt('Desktop/dgms.txt',dgms) 
#run basic statistical analysis of standard EEG (standard) and the seizure EEG (test) #t-test is included to verify there is a significant difference between the normal EEG and the EEG being tested
# def stats(standard_data, test_data):
#     mean_test=np.mean(test_data)
#     std_test = np.std(test_data)
#     count_test = len(test_data)
#     mean_standard = np.mean(standard_data)
#     std_standard = np.std(standard_data)
#     count_standard = len(standard_data)
#     t_test = stats.ttest_ind(standard_data, test_data, equal_var=False)
#     #--------
#     print('Test mean is '+repr(mean_test),'and standard mean is '+repr(mean_standard)) 
#     print('Test std is '+repr(std_test),'and standard std is '+repr(std_standard)) 
#     print('Test population is '+repr(count_test),'and standard population is '+repr(count_standard))
#     print('Assuming unequal variance the t-test p-value is '+repr(t_test.pvalue)) 
#     #--------
#     #barcode of data
#     #this assumes Gaussian distribution to barcodes
#     #the cutoffs can be tweaked by changing cutoff, lower, and upper
#     #loaded (birth, death) values need to be saved as dgms using values obtained from r_complex(edf_data) otherwise dgms = dgms[1] will need to be removed from code def barc(dgms): 
#     dgms = dgms[1]
#     bar_dist = dgms[:,1]-dgms[:,0]
#     data_mean, data_std = mean(bar_dist), std(bar_dist)
#     lower, upper = data_mean - 3*data_std, data_mean + 3*data_std 
#     x=dgms[:,0]
#     y=dgms[:,1]
#     points = np.stack((x, y, bar_dist), axis=-1)
#     cutoff = np.mean(bar_dist)+3*np.std(bar_dist)
#     p = points[points[:,2]>=lower]
#     p = p[p[:,2]>=upper]
#     p = np.sort(p,-2)[::-1]
#     x = [x for x , y, bar_dist in p]
#     y = [y for x , y, bar_dist in p]
#     len_x=len(x)
#     y_axis = np.arange(1,10, 10/len_x)
#     y_axis_inv = y_axis[::-1]
#     factor = -1*int(np.log10(np.min(x)))
#     correc = np.full((1, len_x), (10**factor))
#     x = np.multiply(x, correc)
#     y = np.multiply(y, correc)
#     plt.hlines(y_axis_inv, xmin = x,xmax = y,colors = 'b')
#     ax = plt.axes()
#     ax.yaxis.set_major_locator(plt.NullLocator())
#     #--------
#     plt.show() 
