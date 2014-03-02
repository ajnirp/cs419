from __future__ import division

import numpy as np
import random
import matplotlib.pyplot as plt

def plot_errors(filename, graph_title, y_axis):
	plt.title(graph_title)
	plt.xlabel('m')
	plt.ylabel('error')
	plt.plot(range(6000),y_axis)
	plt.savefig('plots/'+filename)
	plt.close()

p = [1/12.,1/4.,1/12.,1/4.,1/12.,1/4.] # actual probability
training_set = [list(x).index(1) for x in np.random.multinomial(1,p,size=6000)]

def mle(d):
	dlen = len(d)
	return [d.count(x) / dlen for x in xrange(6)]

def error(p_estimated, p_actual):
	error_vector = [x[0] - x[1] for x in zip(p_estimated, p_actual)]
	return np.sqrt(sum(x*x for x in error_vector))

def counts(d):
	return [d.count(x) for x in xrange(6)]

def map_estimate(d, alpha):
	cnts = counts(d)
	cnts_sum = len(d)
	alpha_sum = sum(alpha)
	return [(cnts[x]+alpha[x]-1)/(cnts_sum+alpha_sum-6) for x in xrange(6)]

def bam_estimate(d, alpha):
	cnts = counts(d)
	cnts_sum = len(d)
	alpha_sum = sum(alpha)
	return [(cnts[x]+alpha[x])/(cnts_sum+alpha_sum) for x in xrange(6)]

alph_even_dominates = [1,2,2,8,3,4] # sum of odd = 6, sum of even = 18
alph_odd_dominates = [2,1,8,2,4,3] # sum of odd = 18, sum of even = 6

errors_mle = [error(mle(training_set[:(1+i)]), p) for i in xrange(6000)]

errors_odd_dominates_map = [error(map_estimate(training_set[:(i+1)], alph_odd_dominates), p) for i in xrange(6000)]
errors_even_dominates_map = [error(map_estimate(training_set[:(i+1)], alph_even_dominates), p) for i in xrange(6000)]

errors_odd_dominates_bam = [error(bam_estimate(training_set[:(i+1)], alph_odd_dominates), p) for i in xrange(6000)]
errors_even_dominates_bam = [error(bam_estimate(training_set[:(i+1)], alph_even_dominates), p) for i in xrange(6000)]

plot_errors('2_1.png', 'Maximum Likelihood Estimator', errors_mle)
plot_errors('2_2_map.png', 'Maximum A Posteriori Estimator', errors_odd_dominates_map)
plot_errors('2_3_map.png', 'Maximum A Posteriori Estimator', errors_even_dominates_map)
plot_errors('2_2_bam.png', 'Bayesian Average Model', errors_odd_dominates_bam)
plot_errors('2_3_bam.png', 'Bayesian Average Model', errors_even_dominates_bam)