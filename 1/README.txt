##############################################
#                                            #
#   CS419, Introduction to Machine Learning  #
#   Assignment 1                             #
#   Rohan Prinja                             #
#   Roll no. 110050011                       #
#                                            #
##############################################

This is the report for Assignment 1 of CS 419, Introduction to Machine Learning. It contains information about the submission and instructions on how to run the scripts.

Deliverables for Q1
===================

Means and Covariances
---------------------

These can be found in the file 'mean-covariances.txt'

Plots
-----

Plot for n = 1: 1_1.png
Plot for n = 5: 1_5.png
Plot for n = 10: 1_10.png
Plot for n = 50: 1_50.png
Plot for n = 100: 1_100.png

Q. Do your plots provide evidence for statistical consistency?
A. Yes, they do. As we increase the value of m from 10 to 10,000 the fraction of vectors with a significant error drops from almost 1 to almost 0. This implies that our minimizer is getting more and more accurate as we increase m (size of the training set).

Notes
-----

1. The value of p has been arbitrarily chosen to be 100.
2. Different thresholds have been used for different values of n. Here is the set of n values and the corresponding threshold values:

n_values   = 1     5     10     50     100
thresholds = 1e-3  5e-3  10e-3  20e-3  100e-3

This was done because imposing a uniform threshold makes no sense, since the error between the empirical risk minimizer theta vector and the true risk minimizer theta vector grows as a function of their lengths, which grow with n.

Deliverables for Q2
===================

Hyperparameters
---------------

alph_even_dominates = [1,2,2,8,3,4] # sum of odd = 6, sum of even = 18
alph_odd_dominates = [2,1,8,2,4,3] # sum of odd = 18, sum of even = 6

Plots
-----

Maximum Likelihood Estimator: 2_1.png
Bayesian Average Model: 2_2_bam.png and 2_3_bam.png
Maximum A Posteriori Estimator: 2_2_map.png and 2_3_map.png
Script to generate these plots: 2.py

Q. Is your observation from these plots intuitive?
A. Yes, it is. As the value of m increases, the estimator becomes more accurate as it has seen more data.

How to use the scripts
======================

I have written two Python scripts to solve the problems. Both of them depend upon Numpy for the matrix calculations, and Matplotlib for the plotting. Assuming those two are installed, to run the scripts simply do:

	python 1.py > file-to-store-values-of-mean-and-covariance.txt

and

	python 2.py

and the plots will be generated (in png format). Please refer to the table at the top of this file to see which plot corresponds to which subproblem.

For Q1, if you run the command as above, then the file 'file-to-store-values-of-mean-and-covariance.txt' has the values of the mean and covariance for n = 1, 5, 10, 50, 100.