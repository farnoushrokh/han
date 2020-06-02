from datetime import datetime
import numpy as np
import os
import pickle
# from sklearn.metrics import classification_report
# import tensorflow as tf
# from tensorflow.python.framework import random_seed
# from tensorflow.python.ops import clip_ops
# import time
# from dataset import SnP500Dataset
from model import HAN
# from bert.optimization import AdamWeightDecayOptimizer
import config


dataset = pickle.load(open('/Users/m.s.beni/PycharmProjects/han/data/sp500glove.pkl', 'rb'))
train_ds, dev_ds, test_ds = dataset.get_dataset(
    batch_size=32, max_date_len=40, max_news_len=30)
model = HAN(dataset.wordvec, config.args)