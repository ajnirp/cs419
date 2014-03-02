from __future__ import division

import numpy as np
import random
import matplotlib.pyplot as plt

m_values = [10,50,100,500,750,1000,2500,5000,7500,10000]
n_values = [1, 5, 10, 50, 100]

def plot_errors(filename, graph_title, y_axis):
	plt.title(graph_title)
	plt.xlabel('m')
	plt.ylabel('fraction')
	plt.plot(m_values, y_axis)
	plt.savefig('plots/'+filename)
	plt.close()

# generate a random positive definite matrix for the covariance matrix
def random_mean_vector(n):
	return [random.random() for i in xrange(n+1)]

def random_cov_matrix(n):
	matrix = np.array([[random.random() for i in xrange(n+1)] for j in xrange(n+1)])
	symm_matrix = matrix + matrix.transpose()
	return (n+1)*np.identity(n+1) + symm_matrix

# explanation: to generate a random positive definite matrix, first generate a symmetric matrix
# then add nI to it where I is the identity matrix of order n
	
# make p = 100 training sets D1, D2, ... , Dp
# each training set has 10,000 elements

p = 100

def training_sets(n):
	mean = random_mean_vector(n)
	cov = random_cov_matrix(n)
	return [np.random.multivariate_normal(mean, cov, 10000) for i in xrange(p)], mean, cov

# empirical risk minimization
def w_empirical_minimzer(m, d):
	return [np.linalg.lstsq([x[:-1] for x in t_set[:m]], [x[-1] for x in t_set[:m]])[0] for t_set in d]

def w_error(w1, w2):
	return sum((x[0]-x[1])**2 for x in zip(w1,w2))


thresholds = [1e-3, 5e-3, 10e-3, 20e-3, 100e-3]
for n,threshold in zip(n_values,thresholds):
	d, m, c = training_sets(n)

	print 'Mean vector being used is:', m
	print 'Covariance matrix being used is:'
	for i in c: print i

	mean_x = np.array(m[:-1])
	mean_y = m[-1]

	var_x = [i[:-1] for i in c[:-1]]

	cov_xy = [i[-1] for i in c[:-1]]
	w_trm = np.linalg.pinv(var_x + (mean_x.transpose().reshape(n,1)*mean_x)).dot((cov_xy + mean_y*mean_x).reshape(n,1))

	f = []
	for m in m_values:
		w_erm = w_empirical_minimzer(m, d)
		more_than = sum(1 for i in xrange(p) if w_error(w_trm, w_erm[i]) > threshold)
		fraction = more_than / p
		f.append(fraction)

	plot_errors('1_'+str(n)+'.png', 'Fraction where error between TRM and ERM is > ' + str(threshold), f)
	# print 'Done for n = ', n