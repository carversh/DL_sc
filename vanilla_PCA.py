#!/usr/bin/python

from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

df = = pd.read_csv(filename, sep='\t', header=0, index_col=0) # read in file

mean = np.mean(df, axis=0) # compute mean of each column
std = np.std(df, axis=0) # compute standard deviation of each column

df_standardized = (df - mean) / std # standardize

# perform PCA
pca = PCA(n_components=200) # instantiate PCA with hyperparameters
sample_embeddings = pca.fit_transform(df_standardized) # projections (of input data onto eigenvectors)
feature_loadings = pca.components_ # retrieve eigenvectors
