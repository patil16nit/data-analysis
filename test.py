import numpy as np
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt

import json

from collections import defaultdict



path='/Users/NIT/Documents/python/safari/pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'


#print(open(path).readline())

records=[json.loads(line) for line in open(path)]

#print(records[0]['tz'])

zones=[rec['tz'] for rec in records if 'tz' in rec]
#print(zones[:10])


frame=DataFrame(records)

clean_tz= frame['tz'].fillna('Missing')

clean_tz[clean_tz == '']='unknown'

tz_count=clean_tz.value_counts()
#tz_count[0:10].plot(kind='barh', rot=0)
#plt.show()

#print(frame['a'][1])

cframe=frame[frame.a.notnull()]

operating_system=np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os=cframe.groupby(['tz', operating_system])

agg_counts=by_tz_os.size().unstack().fillna(0)
indexer=agg_counts.sum(1).argsort()
count_subset=agg_counts.take(indexer)[-10:]
count_subset.plot(kind='barh', stacked=True)
plt.show()