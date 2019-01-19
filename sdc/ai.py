import numpy as np
import random  # for experience replay
import os  # to load/save the model
import torch  # pytorch for dynamic graphics
import torch.nn  # neural network
import torch.nn.functional as F
import torch.optim as optim  # optimizer for stochastic gradient descent
import torch.autograd as autograd  # tensor to variables
from torch.autograd import Variable
