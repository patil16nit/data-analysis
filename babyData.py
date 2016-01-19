import pandas as pd
import matplotlib.pyplot as plt

names1880=pd.read_csv('/Users/NIT/Documents/python/safari/pydata-book/ch02/names/yob1880.txt', names=['name', 'sex', 'births'])


years=range(1880,2011)

pieces=[]

columns=['name', 'sex', 'births']
for year in years:
    path='/Users/NIT/Documents/python/safari/pydata-book/ch02/names/yob%d.txt'%year
    frame=pd.read_csv(path, names=columns)
    frame['year']=year
    pieces.append(frame)
    
#concating everything into single dataframe
names=pd.concat(pieces, ignore_index=True)
#print(names[:10])

total_births=names.pivot_table('births', index='year', columns='sex', aggfunc=sum)

total_births.plot(title='Total births by sex and year')
plt.show()
