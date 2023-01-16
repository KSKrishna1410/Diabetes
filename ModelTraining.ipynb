{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fcea04f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "22e7df0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('diabetes.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6854962c",
   "metadata": {},
   "outputs": [],
   "source": [
    "X=df.iloc[:,:-1]\n",
    "y=df.iloc[:,-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "467ffa7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9dd55bc7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier()"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "classifier=RandomForestClassifier()\n",
    "classifier.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e847a012",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred=classifier.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8d701ca1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "score=accuracy_score(y_test,y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "59283711",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7272727272727273"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "94ce4b08",
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle_out = open(\"classifier.pkl\",\"wb\")\n",
    "pickle.dump(classifier, pickle_out)\n",
    "pickle_out.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "85a93620",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0], dtype=int64)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "classifier.predict([[2,3,4,1]])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
