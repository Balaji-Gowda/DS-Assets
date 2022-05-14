import pandas as pd
import pickle
df=pd.read_csv("C:\\Users\\894524\\Downloads\\SMSSpamCollection.txt",sep='\t',names=["Labels",'Message'])


#cleaning data
import nltk
import re

nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps=PorterStemmer()
corpus=[]
for i in range(0,len(df)):
    rev=re.sub('[^a-zA-Z]',' ',df['Message'][i])
    rev=rev.lower()
    rev=rev.split()
    
    rev=[ps.stem(word) for word in rev if not word in set(stopwords.words('english'))]
    rev=' '.join(rev)
    corpus.append(rev)
    
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000)
x=cv.fit_transform(corpus).toarray()


y=pd.get_dummies(df['Labels'])
y=y.iloc[:,1].values


#train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)


from sklearn.naive_bayes import MultinomialNB
nb=MultinomialNB()
mod=nb.fit(x_train,y_train)

pred=mod.predict(x_test)
from sklearn.metrics import confusion_matrix,accuracy_score
con_mat=confusion_matrix(y_test, pred)
score=accuracy_score(y_test,pred)


#if we have imbalnced dataset(unequal prop of spam and ham) use
#lemmetization and Tf Idf vectoriser














