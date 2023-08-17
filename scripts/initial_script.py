#!/usr/bin/python
import os
import configmypy
import pandas as pd 
import torch
import torch.nn.functional as F
import torchvision
import pickle
import numpy as np
from datetime import datetime
import scipy.io
import tensorboardX



config_name = 'default'
pipe = configmypy.ConfigPipeline(
    [
        configmypy.YamlConfig(
            "../config/sc_params.yaml",
            config_name="default",
            config_folder="../config",
        ),
        configmypy.ArgparseConfig(
            infer_types=True, config_name=None, config_file=None
        ),
        configmypy.YamlConfig(config_folder="../config"),
    ]
)
# parse params in yaml file
params = pipe.read_conf()

#params = {}
# add designated params that require packages
params["device"] = "cuda:0" if torch.cuda.is_available() else "cpu"
params["random_date"] = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

# make necessary directories to store results
os.makedirs("../results/" + params["random_date"] + "/tensorboard")
# point tensorboard to where it will store data
writer = tensorboardX.SummaryWriter("../results/" + params["random_date"] + "/tensorboard")
writer.add_text("params", str(params))
writer.flush()

# save parameters as pickle
pickle_path = os.getcwd() + "/../results/" + params["random_date"] + "/params.pickle"



# with open('params.pickle', 'wb') as f:
#     pickle.dump(params, f)
with open(pickle_path, 'wb') as f:
    pickle.dump(str(params), f)



personInfo = pickle.load(open(pickle_path, "rb"))
print(personInfo)


#print(type(params))
test = np.random.standard_normal(size=(1000,500) )


