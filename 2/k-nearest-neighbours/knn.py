# k nearest neighbours classifier
from collections import Counter
import matplotlib.pyplot as plt

def make_plot(filename, graph_title, xs, ys):
	plt.title(graph_title)
	plt.xlabel('k')
	plt.ylabel('accuracy')
	plt.plot(xs, ys)
	plt.savefig(filename)
	plt.close()

training_set = []
validation_set = []

with open('iris.data.txt', 'r') as f:
	for index, line in enumerate(f.readlines()):
		if (0 <= index < 25) or (50 <= index < 75) or (100 <= index < 125):
			training_set.append(tuple(line[:-1].split(',')))
		elif (25 <= index < 50) or (75 <= index < 100) or (125 <= index < 150):
			validation_set.append(tuple(line[:-1].split(',')))

training_set = [(tuple(float(x) for x in pair[:-1]), pair[-1]) for pair in training_set]
validation_set = [(tuple(float(x) for x in pair[:-1]), pair[-1]) for pair in validation_set]

# euclidean distance metric
def distance(tuple1, tuple2):
	return (sum((x-y)**2 for x,y in zip(tuple1, tuple2))) ** 0.5

def find_distances(dataset):
	# distances = {i[0]:[] for i in dataset}
	distances = [[] for i in dataset]
	for i in xrange(len(dataset)):
		for j in xrange(len(training_set)):
			t, u = dataset[i][0], training_set[j][0]
			distances[i].append(distance(t,u))
	return distances

# k nearest neighbours majority voting is easy
def knn(k,dataset):
	result = []
	# training set accuracy
	dset_distances = find_distances(dataset)
	for i in xrange(len(dataset)):
		i_data = dset_distances[i]
		sorted_distances = sorted([(index,data) for index,data in enumerate(i_data)], key=lambda x: x[1])
		k_nearest = sorted_distances[1:k+1] if dataset == training_set else sorted_distances[:k]
		labels = [dataset[x[0]][1] for x in k_nearest]
		result.append(list(Counter(labels))[0])
	return result

tset_xs, vset_xs = range(1,51), range(1,51)
tset_ys, vset_ys = [], []
for k in xrange(1,51): tset_ys.append(sum([x == y[1] for x,y in zip(knn(k,training_set), training_set)]))
for k in xrange(1,51): vset_ys.append(sum([x == y[1] for x,y in zip(knn(k,validation_set), validation_set)]))

make_plot('knn-tset.png', 'Training set accuracy', tset_xs, tset_ys)
make_plot('knn-vset.png', 'Validation_set set accuracy', vset_xs, vset_ys)
	# setosa_accuracy = sum([x == y[1] for x,y in zip(knn(k), training_set[:25])])
	# versicolor_accuracy = sum([x == y[1] for x,y in zip(knn(k), training_set[25:50])])
	# virginica_accuracy = sum([x == y[1] for x,y in zip(knn(k), training_set[50:75])])
	# in this case, average for each class is easier to calculate because the number of samples
	# for each class is the same (i.e. 25)

# sanity tests

# print len([x for x in training_set if x[4] == 'Iris-virginica'])
# print len([x for x in training_set if x[4] == 'Iris-setosa'])
# print len([x for x in training_set if x[4] == 'Iris-versicolor'])
# print len([x for x in validation_set if x[4] == 'Iris-virginica'])
# print len([x for x in validation_set if x[4] == 'Iris-setosa'])
# print len([x for x in validation_set if x[4] == 'Iris-versicolor'])
# print len(distances)
# print len(training_set)
# print len(distances[training_set[0][0]])
