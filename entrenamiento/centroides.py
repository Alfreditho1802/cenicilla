import numpy as np
import pandas as pd
import cv2
from sklearn import preprocessing
from sklearn.cluster import KMeans
def k_means_centros(neuronas):#se recibe la lista de neuronas 
    dicccionario={}# se crea un diccionario en cual servirá para entrenar el K-means
    n1,n2,n3,n4=[],[],[],[] #listas de cada uno de los canales de las neuronas 
    for i in range(len(neuronas)):#inicializacion de las listas
        n1.append(neuronas[i].w1)
        n2.append(neuronas[i].w2)
        n3.append(neuronas[i].w3)
        n4.append(neuronas[i].w4)
    #se agregan los datos al diccionario 
    dicccionario.update({'peso_1':n1})
    dicccionario.update({'peso_2':n2})
    dicccionario.update({'peso_3':n2})
    dicccionario.update({'peso_4':n4})
    #se crea un dataframe con ayuda de pandas 
    df=pd.DataFrame(data=dicccionario) #se crea el data frame con la informacion recopilada del diccionario 
    k_means=KMeans(n_clusters=3).fit(df)# se definen los clusters del kmeans
    labels=k_means.predict(df)#se hace una predicción para ver a cual de los tres clusters se adecua más 
    df['asiganacion']=labels#se añade al dataframe
    return df# se retorna el dataframe que posteriormente nos ayudará a segmentar las imagenes correctamente
    


def p():
    n=[
        [0.3508,0.6218,0.0846,0.0846,1850770],
        [0.3163,0.6207,0.1008,0.1008,636097],
        [0.3806,0.6578,0.1061,0.1061,545724],
        [0.3839,0.647,0.0821,0.0821,489316],
        [0.2919,0.5888,0.09,0.09,457170],
        [0.3623,0.599,0.0661,0.0661,275987],
        [0.3795,0.5179,0.0331,0.0331,238079],
        [0.3982,0.6549,0.0625,0.0625,116990]
    ]
    """
    n=[
        #BBHH
        [0.6378,0.6378,0.0898,0.0898,15],
        [0.6391,0.6391,0.0857,0.0857,10],
        [0.6457,0.6457,0.0838,0.0838,14],
        [0.6262,0.6262,0.0841,0.0841,6],
        [0.6325,0.6325,0.0947,0.0947,3],
        [0.6115,0.6115,0.0796,0.0796,4],
        [0.6284,0.6284,0.0929,0.0929,11],
        [0.6653,0.6653,0.0861,0.0861,3],
        [0.6667,0.6667,0.085,0.085,1]
    ]
    n=[
        #BBHH
        [0.5918,0.5918,0.0956,0.0956,13233],
        [0.6239,0.6239,0.0871,0.0871,7582],
        [0.6284,0.6284,0.0954,0.0954,16618],
        [0.6126,0.6126,0.1011,0.1011,48788],
        [0.6213,0.6213,0.1086,0.1086,31383],
        [0.5822,0.5822,0.0814,0.0814,57630],
        [0.6022,0.6022,0.102,0.102,28200],
        [0.6342,0.6342,0.1068,0.1068,45508],
        [0.6457,0.6457,0.0905,0.0905,15236]
    ]
    
    n=[
        #BBHH
        [0.649,0.649,0.0816,0.0816,1903712],
        [0.6197,0.6197,0.0986,0.0986,1826949],
        [0.6106,0.6106,0.0653,0.0653,1618891],
        [0.5865,0.5865,0.0735,0.0735,1188889],
        [0.5943,0.5943,0.0977,0.0977,891374],
        [0.645,0.645,0.1068,0.1068,872610],
        [0.5714,0.5714,0.0968,0.0968,308103]
        ]
   
    #bbhh
        [0.649,0.649,0.0816,0.0816,1879517],
        [0.6107,0.6107,0.0933,0.0933,1571856],
        [0.6106,0.6106,0.0653,0.0653,1525235],
        [0.6431,0.6431,0.1048,0.1048,906343],
        [0.6244,0.6244,0.1028,0.1028,865866],
        [0.5714,0.5714,0.0968,0.0968,364995]
    
    n=[
        #LABH
        [0.731,0.4159,0.6728,0.0962,204063],
        [0.5594,0.3386,0.6741,0.0995,124862],
        [0.8342,0.4244,0.6337,0.0521,109286],
        [0.4468,0.3935,0.612,0.0778,83323],
        [0.6384,0.3453,0.6804,0.0948,80478],
        [0.4025,0.3718,0.5154,0.0331,35787],
        [0.9186,0.3814,0.5314,0.0292,31046],
        [0.4,0.2974,0.5897,0.104,23383],
        [0.6979,0.4511,0.6553,0.0496,21483]
    ]
    """
    #n=sorted(n,key=lambda x: x[0])
    #print(n[1])
    nuevo={}
    c1,c2,c3,c4,c5=[],[],[],[],[]
    for i in range(len(n)):
        c1.append(n[i][0])
        c2.append(n[i][1])
        c3.append(n[i][2])
        c4.append(n[i][3])
        c5.append(n[i][4])
    nuevo.update({'C1':c1})
    nuevo.update({'C2':c2})
    nuevo.update({'C3':c3})
    nuevo.update({'C4':c4})
    #nuevo.update({'c5':c5})
    df=pd.DataFrame(data=nuevo)
    #print(df)
    k_means=KMeans(n_clusters=3).fit(df)
    centroids=k_means.labels_
    print(centroids)
    labels=k_means.predict(df)
    df['label']=labels
    """
    l=[]
    for i in range(9):
        a=cv2.imread(str(i)+'.jpg')
        cv2.imshow(str(i),a)
        l.append(a)
    #prueba=cv2.imread('media/hsv/imagen1_bCU4uzR.jpg')
    #prueba1=cv2.imread('media/lab/imagen1_bCU4uzR.jpg')
    #print(np.median(prueba[:,:,0]))
    #print(np.median(prueba1[:,:,2]))
    x=l[0]+l[5]+l[6]
    y=l[1]+l[2]+l[3]+l[4]+l[7]+l[8]
    cv2.imshow('xi',x)
    cv2.imshow('yi',y)
    cv2.imshow('z',x+y)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """