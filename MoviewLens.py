import pandas as pd

unames=['user_id','gender','age','occupation', 'zip']

users=pd.read_table('/Users/NIT/Documents/python/safari/ml-1m/users.dat', sep='::', header=None, names=unames,engine = 'python')

rnames=['user_id','movie_id','rating', 'timestamp']
ratings=pd.read_table('/Users/NIT/Documents/python/safari/ml-1m/ratings.dat', sep='::', header=None, names=rnames,engine = 'python')

mnames=['movie_id','title','genres']
movies=pd.read_table('/Users/NIT/Documents/python/safari/ml-1m/movies.dat', sep='::', header=None, names=mnames,engine = 'python')

data=pd.merge(pd.merge(ratings, users),movies)
mean_ratings = data.pivot_table('rating', index='title', columns='gender',aggfunc = 'mean')

rating_by_title=data.groupby('title').size()
active_title=rating_by_title.index[rating_by_title>=250]
mean_ratings=mean_ratings.ix[active_title]
#top films among female viewers
top_female_rating=mean_ratings.sort_values(by='F', ascending=False)

#mean diff
mean_ratings['diff']=mean_ratings['M']-mean_ratings['F']

sorted_by_diff=mean_ratings.sort_index(by='diff')

#rating grouped by title
rating_std_by_title=data.groupby('title')['rating'].std()
active_titles=rating_std_by_title.index[rating_by_title>=250]
rating_std_by_title=rating_std_by_title.ix[active_titles]

