import pickle

def loadpicklked(fn_pickle):
    file = open(fn_pickle, 'rb')
    # dump information to that file
    data = pickle.load(file)
    # close the file
    file.close()

    data_training = data[0]
    labels_training = data[1]  #trainy
    data_test = data[2]  #testX
    labels_test = data[3] #testy
    class_name_pub = data[4] 
    feature_name = data[5] 
    vtt_avg = data[6]   # 클래스별 시간 정보 포함
    dname = data[7] 
    tstring = data[8]
    scaler = data[9]    #20201222 
                        # scaler = preprocessing.StandardScaler().fit(datac_all)
    len_data = data_training.shape[0]+ data_test.shape[0]


    


    return len_data, data_test, labels_test, feature_name