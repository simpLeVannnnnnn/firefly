import numpy as np
import os
import random
import time
import datetime
from celery import task
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import neighbors
from sklearn import utils
from likes.models import Likes


def handle_uploaded_file(f):
    path = "library/library/files/"
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = path + f.name
    destination = open(file_name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()


def handle_uploaded_file_cover(f):
    path = "library/library/files/cover/"
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = path + f.name
    destination = open(file_name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()


def data_processing(predata,newdata):

    # process the enum data into onehot type
    data = []
    target = []
    ostypeEnums = []
    oss = []
    types = []
    enc = preprocessing.OneHotEncoder()



    for d in predata:
        os = d.support_system
        if os in oss:
            os = oss.index(os)
        else:
            oss.append(os)
            os = len(oss)-1
        type = d.tag
        if type in types:
            type = types.index(type)
        else:
            types.append(type)
            type = len(types)-1
        row = [os,type] 
        ostypeEnums.append(row)
    enc.fit(ostypeEnums)


    #  processing the data
    for d in predata:
        os = d.support_system
        data_updata_time = str(d.updata_time)[0:10]
        temp = data_updata_time.split("-")
        t = t = temp[0] + "-" + temp[1] + "-" + temp[2]
        t_time = datetime.datetime.strptime(t,'%Y-%m-%d')
        timeInterval = (datetime.datetime.now()-t_time).days
        size = d.size
        type = d.tag
        downloadNum = d.amount_of_downloads
        score = int(float(d.score))
        positive = Likes.objects.all().count()
        ostypes = enc.transform([[oss.index(os),types.index(type)]]).toarray().tolist()
        ostypes[0] = [int(i) for i in ostypes[0]]
        row = ostypes[0] + [timeInterval,size,downloadNum,positive]
        data.append(row)
        target.append(score)

    data = np.array(data)
    target = np.array(target)


    
    #Algorithm_1_Random_Forest

    Accuracy = []
    avg_Accuracy = []
    avg_Variance = []
    margin = []
    runtime = []
    avg_TimeCost = []

    sampleNumber = 30

    for s in range(0,sampleNumber):
        timecost = time.time()
        sampleSize = int(0.6*len(data))
        sampleIndex = random.sample(range(0,len(data)),sampleSize)
        testIndex = [item for item in range(0,len(data)) if item not in sampleIndex]

        trainData =[]
        trainResult=[]
        testData =[]
        testResult=[]

        for i in sampleIndex:
            trainData.append(data[i])
            trainResult.append(target[i])

        testData.append(data[-1])
        testResult.append(target[-1])

        clf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                                    max_depth=2, max_features='auto', max_leaf_nodes=None,
                                    min_impurity_split=0,
                                    min_samples_leaf=1, min_samples_split=2,
                                    min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
                                    oob_score=False, random_state=0, verbose=0, warm_start=False)
        clf.fit(trainData, trainResult)
        prediction = clf.predict(testData)

        timecost = time.time() - timecost
        runtime.append(timecost)

        error = []
        for i in range(0,len(testResult)):
            if(float(testResult[i])==0):
                continue;
            e = abs(float(prediction[i])-float(testResult[i]))/float(testResult[i])
            error.append(e)
        avg_eror = np.mean(error)
        Accuracy.append(avg_eror)

    newdata.score = prediction[0]
    newdata.save()

    avg_Accuracy = (1-np.mean(Accuracy))*100
    avg_Variance = np.var(Accuracy)
    margin = 1.96 * 100 * avg_Variance/np.sqrt(sampleNumber)
    avg_TimeCost = np.mean(runtime)



