import pandas as pd
import numpy as np
from Reuters import *
# read and parse the data
# this will download the data if it's not yet available locally
data_streamer = ReutersStreamReader('reuters').iterdocs()
data = get_minibatch(data_streamer, 50000)
title_body=list(data[data.columns[0]])
print title_body[0]