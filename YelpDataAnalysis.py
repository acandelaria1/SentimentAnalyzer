from __future__ import print_function
from matplotlib import pyplot as plt
import json
from collections import Counter
from datetime import datetime
import pandas as pd
import numpy as np
import time

with open ("yelp_dataset_challenge_round9/yelp_academic_dataset_review.json") as f:#"yelp_dataset_challenge_round9/yelp_academic_dataset_review.json") as f:
    #comma delimited json requires read_json method to set lines parameter to true
    fr_start_time = time.clock()
    filer = f.read()
    print("file read: ", time.clock()-fr_start_time)
    jd_start_time = time.clock()
    json_dump = json.dumps(filer)
    print("json dump: ", time.clock() - jd_start_time)
    jl_start_time = time.clock()
    json_load = json.loads(json_dump)
    print("json load: ", time.clock() - jl_start_time)
    rj = time.clock()
    df = pd.read_json(json_load)
    print("read json into pandas: ", time.clock()-rj)
                                                            #df = pd.read_json(json.loads(json.dumps(f.read())), lines=True)
                                                                
print("completed upload of dataset")
