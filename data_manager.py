# coding : utf-8
# author : ilkyu lee
# mail : xxjjvxb@gmail.com

import numpy as np
import pandas as pd
import glob

class data_manager(object):

    def __init__(self, batchsize=1):
        if batchsize == 1:
            print('batchsize is 1')

    def cifar10(self):
        train = "../../../bigdata/cifar-10-batches-py/data_batch*"
        test = "../../../bigdata/cifar-10-batches-py/test_batch*"

        self.trainList = glob.glob(train)
        self.testList = glob.glob(testi)

   def getTrain(self):

        for each in self.trainList:
            print(each)

        yield X, Y

    def getTest(self):

        return X, Y



if __name__ == "__main__":

    dm = data_manager()
    dm.cifar10()
