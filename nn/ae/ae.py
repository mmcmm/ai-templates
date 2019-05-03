# AutoEncoders

# Importing the libraries
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable

# Importing the dataset
movies = pd.read_csv('datasets/movies.dat', sep='::',
                     header=None, engine='python', encoding='latin-1')
users = pd.read_csv('datasets/users.dat', sep='::', header=None,
                    engine='python', encoding='latin-1')
ratings = pd.read_csv('datasets/ratings.dat', sep='::',
                      header=None, engine='python', encoding='latin-1')

