import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout,Flatten,Dense,Activation
from tensorflow.python.keras.layers import Convolution2D,MaxPooling2D
from tensorflow.python.keras import backend as K
#para la validacion de una imagen
import numpy as np
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.models import load_model
from entrenamiento.models import Imagenes as Img
#creacion del directorio de imagenes
import cv2
def almacenar_imagenes(nombre,Imagenes,Imagenes2):
    dir='imagenes_pruebas/'
    dir1=dir+nombre+'/'
    dir2=dir1+'data/'
    dir3=dir1+'validacion/'
    os.mkdir(dir1)
    os.mkdir(dir2)
    os.mkdir(dir3)
    os.mkdir(dir2+'enferma/')
    os.mkdir(dir2+'sana/')
    os.mkdir(dir3+'enferma/')
    os.mkdir(dir3+'sana/')
    if len(Imagenes)<len(Imagenes2):
        tam=len(Imagenes)
    else:
        tam=len(Imagenes2)
    division=int(round(tam*0.8))
    print(division)
    for i in range(tam):
        if i<division:
            a=cv2.imread('media/'+str(Imagenes[i].imagen_normalizada))
            cv2.imwrite(dir2+'enferma/'+str(i)+'.jpg',a)
        else:
            a=cv2.imread('media/'+str(Imagenes[i].imagen_normalizada))
            cv2.imwrite(dir3+'enferma/'+str(i)+'.jpg',a)
    for j in range(tam):
        if j<division:
            a=cv2.imread('media/'+str(Imagenes2[j].imagen_normalizada))
            cv2.imwrite(dir2+'sana/'+str(j)+'.jpg',a)
        else:
            a=cv2.imread('media/'+str(Imagenes2[j].imagen_normalizada))
            cv2.imwrite(dir3+'sana/'+str(j)+'.jpg',a)
    return dir1,dir2,dir3
def creacion_red(nombre,Imagenes,Imagenes2,epocas,pasos,pasos_validacion,batch_size,filtrosConv1,filtrosConv2):
    general,data,validacion=almacenar_imagenes(nombre,Imagenes,Imagenes2)
    K.clear_session()
    data_entrenamiento=data
    data_validacion=validacion
    #filtros estaticos 
    altura,longitud=100,100
    tam_filtro1=(3,3)
    tam_filtro2=(2,2)
    tam_pool=(2,2)
    clases=2
    lr=0.0005

    #Preposesamiento de imagenes
    entrenamiento_datagen=ImageDataGenerator(
        rescale=1./255,
        shear_range=0.3,
        zoom_range=0.3,
        horizontal_flip=True
    )
    validacion_datagen=ImageDataGenerator(
        rescale=1./255
    )
    imagen_entrenamiento=entrenamiento_datagen.flow_from_directory(
        data_entrenamiento,
        target_size=(altura,longitud),
        batch_size=batch_size,
        class_mode='categorical'
    )
    imagen_validacion=validacion_datagen.flow_from_directory(
        data_validacion,
        target_size=(altura,longitud),
        batch_size=batch_size,
        class_mode='categorical'
    )
    #Creacion de la red neuronal
    cnn=Sequential()
    cnn.add(Convolution2D(filtrosConv1,tam_filtro1,padding='same',input_shape=(altura,longitud,3),activation='relu'))
    cnn.add(MaxPooling2D(pool_size=tam_pool))
    cnn.add(Convolution2D(filtrosConv2,tam_filtro2,padding='same',activation='relu'))
    cnn.add(MaxPooling2D(pool_size=tam_pool))
    cnn.add(Flatten())
    cnn.add(Dense(256,activation='relu'))
    cnn.add(Dropout(0.5))
    cnn.add(Dense(clases,activation='softmax'))
    cnn.compile(loss='categorical_crossentropy',optimizer=optimizers.Adam(lr=lr),metrics=['accuracy','mse'])
    hist=cnn.fit_generator(imagen_entrenamiento,steps_per_epoch=pasos,epochs=epocas,validation_data=imagen_validacion,validation_steps=pasos_validacion)
    print(hist.history.keys())
    cal=hist.history['acc']
    perdido=hist.history['loss']
    calidad=hist.history['val_acc']
    error=hist.history['val_loss']
    mse=hist.history['mean_squared_error']
    mse_val=hist.history['val_mean_squared_error']
    clases=imagen_validacion.class_indices
    dir=general+'modelo/'
    if not os.path.exists(dir):
        os.mkdir(dir)
    cnn.save(dir+'modelo.h5')
    cnn.save_weights(dir+'pesos.h5')
    return cal,perdido,calidad,error,mse,mse_val,hist,dir



def inicializacion():
    K.clear_session()
    data_entrenamiento='imagenes_pruebas/data'
    data_validacion='imagenes_pruebas/validacion'

    #Parametros
    epocas=20
    altura,longitud=100,100
    #potencia de dos 
    batch_size=32
    pasos=1000
    pasos_validacion=200
    #potencias de dos 
    filtrosConv1=32
    filtrosConv2=64
    ###se quedan estaticos
    tam_filtro1=(3,3)
    tam_filtro2=(2,2)
    tam_pool=(2,2)
    clases=2
    lr=0.0005
    #Preposesamiento de imagenes
    entrenamiento_datagen=ImageDataGenerator(
        rescale=1./255,
        shear_range=0.3,
        zoom_range=0.3,
        horizontal_flip=True
    )
    validacion_datagen=ImageDataGenerator(
        rescale=1./255
    )
    imagen_entrenamiento=entrenamiento_datagen.flow_from_directory(
        data_entrenamiento,
        target_size=(altura,longitud),
        batch_size=batch_size,
        class_mode='categorical'
    )
    imagen_validacion=validacion_datagen.flow_from_directory(
        data_validacion,
        target_size=(altura,longitud),
        batch_size=batch_size,
        class_mode='categorical'
    )
    #Creacion de la red neuronal
    cnn=Sequential()
    cnn.add(Convolution2D(filtrosConv1,tam_filtro1,padding='same',input_shape=(altura,longitud,3),activation='relu'))
    cnn.add(MaxPooling2D(pool_size=tam_pool))
    cnn.add(Convolution2D(filtrosConv2,tam_filtro2,padding='same',activation='relu'))
    cnn.add(MaxPooling2D(pool_size=tam_pool))
    cnn.add(Flatten())
    cnn.add(Dense(256,activation='relu'))
    cnn.add(Dropout(0.5))
    cnn.add(Dense(clases,activation='softmax'))
    cnn.compile(loss='categorical_crossentropy',optimizer=optimizers.Adam(lr=lr),metrics=['accuracy'])
    hist=cnn.fit_generator(imagen_entrenamiento,steps_per_epoch=pasos,epochs=epocas,validation_data=imagen_validacion,validation_steps=pasos_validacion)
    calidad=hist.history['val_acc']
    error=hist.history['val_loss']
    clases=imagen_validacion.class_indices
    print(clases)
    dir='imagenes_pruebas/modelo'
    if not os.path.exists(dir):
        os.mkdir(dir)
    cnn.save('imagenes_pruebas/modelo/modelo.h5')
    cnn.save_weights('imagenes_pruebas/modelo/pesos.h5')

    return calidad,error,clases

def resultado(file,longitud,altura,cnn):
    x=load_img(file,target_size=(longitud,altura))
    x=img_to_array(x)/255.
    x=np.expand_dims(x,axis=0)
    arreglo=cnn.predict(x)
    
    print(arreglo)
    result=arreglo[0]
    respuesta=np.argmax(result)
    if respuesta==0:
        return 'enferma'
    else:
        return 'sana'

    #print(respuesta)
    #probabilidades=cnn.predict_proba(x)
    #clase=cnn.predict_classes(x)

def comprobacion(file):
    longitud,altura=100,100
    modelo='imagenes_pruebas/modelo/modelo.h5'
    pesos='imagenes_pruebas/modelo/pesos.h5'
    cnn=load_model(modelo)
    cnn.load_weights(pesos)
    resultado(file,longitud,altura,cnn)

def Analisis_Comprobacion(file,modelo,pesos):
    longitud,altura=100,100
    cnn=load_model(modelo)
    cnn.load_weights(pesos)
    r=resultado(file,longitud,altura,cnn)
    return r

    