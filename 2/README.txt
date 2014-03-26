+----------------------------+
| CS419 Assignment 2         |
| Comparison of Classifiers  |
| Rohan Prinja               |
| 110050011                  |
+----------------------------+


k-nearest neighbours classifier
-------------------------------

The code for this part can be found in the file 'knn.py'. It runs the k-nearest classifier on the unaltered Iris data for k = 1,2,3,4,....,50. It records the accuracy for both the training set and the validation set separately and draws the accuracy vs. k in two files, 'plots/knn-tset.png' and 'plots/knn-vset.png' for the training and validation sets respectively.

Logistic regression using LIBLINEAR
-----------------------------------

The code for this part involved a bash script to generate the model files. I manually split the IRIS data into two halves with equal number of samples for each class. One half was stored in the file 'iris.data.training.txt' and the other half was stored in 'iris.data.validation.txt'. Then I wrote the above-mentioned bash script. The script compiles the 'train', 'predict' and 'convert' programs and then runs the 'convert' program on the above two data sets. This is done because the files are in CSV format, whereas LIBLINEAR's programs expect their data to be in the format specified in the README for LIBSVM (The authors of LIBLINEAR provided the source code for the conversion program).

After converting the data sets to the LIBLINEAR data set format, the script runs the train and predict progams and generates a number of output files. The statistics and accuracy values are stored in a file named 'logistic-regression-outputs.txt'.