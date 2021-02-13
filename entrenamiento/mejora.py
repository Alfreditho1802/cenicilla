import cv2
import copy
from PIL import Image
import numpy as np
import colorsys

def ajuste_tam(ruta_in,ruta_fin):#se añadirá una ruta
    pil_img=Image.open("media/"+ruta_in)
    out=pil_img.resize((640,480))
    out.save("media_aux/"+ruta_fin)
    del pil_img

def cargar_imagen(ruta):
    imagen=cv2.imread("media_aux/"+ruta)
    return imagen

def transformacion_yiq(imagen):
    largo,ancho,c=imagen.shape
    aux=np.zeros((largo,ancho,3),np.float32)
    #print("largo",largo)
    #print("ancho",ancho)
    r,g,b=0,0,0
    y,i,q=0,0,0
    for a in range(largo):
        for c in range(ancho):
            b,g,r=imagen[a,c]
            b=float(b/255)
            g=float(g/255)
            r=float(r/255)
            y,i,q=colorsys.rgb_to_yiq(r, g, b)
            aux[a,c,0]=q
            aux[a,c,1]=i
            aux[a,c,2]=y
    return aux

def promedio(imagen):
    q=np.mean(imagen[:,:,0])
    i=np.mean(imagen[:,:,1])
    y=np.mean(imagen[:,:,2])
    return y,i,q

def nueva(imagen1,imagen2):
    y1,i1,q1=promedio(imagen1)
    y2,i2,q2=promedio(imagen2)
    y3=y1-y2
    i3=i1-i2
    q3=q1-q2
    nuevaimg=copy.copy(imagen2)
    largo,ancho,c=nuevaimg.shape
    for i in range(largo):
        for j in range(ancho):
            nuevaimg[i,j,0]=nuevaimg[i,j,0]+q3
            nuevaimg[i,j,1]=nuevaimg[i,j,1]+i3
            nuevaimg[i,j,2]=nuevaimg[i,j,2]+y3
    return nuevaimg

def transformarbgr(imagenp,image):
    largo,ancho,c=imagenp.shape
    aux=copy.copy(image)
    r,g,b=0,0,0
    y,i,q=0,0,0
    for a in range(largo):
        for c in range(ancho):
            q=imagenp[a,c,0]
            i=imagenp[a,c,1]
            y=imagenp[a,c,2]
            r,g,b=colorsys.yiq_to_rgb(y,i,q)
            r=r*255
            g=g*255
            b=b*255
            aux[a,c,0]=b
            aux[a,c,1]=g
            aux[a,c,2]=r
    return aux

def f_norm_ref(img_ref):
    ajuste_tam(img_ref,img_ref)
    a=cargar_imagen(img_ref)
    tam=len(img_ref)
    nueva_r=img_ref[11:tam]
    cv2.imwrite("media/normalizada_ref/"+nueva_r,a)
    ruta=str("normalizada_ref/"+nueva_r)
    return ruta



def funcion_principal(img_ref,img_ent):
   #ajuste_tam(img_ref,img_ref)
   ajuste_tam(img_ent,img_ent)
   a=cv2.imread("media/"+img_ref)
   b=cargar_imagen(img_ent)
   img_ref_yiq=transformacion_yiq(a)
   img_ent_yiq=transformacion_yiq(b)
   y,i,q=promedio(img_ref_yiq)
   nueva_ent_yiq=nueva(img_ref_yiq,img_ent_yiq)
   nueva_ent_bgr=transformarbgr(nueva_ent_yiq,b)
   nuevalab=cv2.cvtColor(nueva_ent_bgr,cv2.COLOR_BGR2LAB)
   nuevahvs=cv2.cvtColor(nueva_ent_bgr,cv2.COLOR_BGR2HSV)
   tam=len(img_ent)
   nueva_r=img_ent[9:tam]
   cv2.imwrite("media/normalizada/"+nueva_r,nueva_ent_bgr)
   cv2.imwrite("media/lab/"+nueva_r,nuevalab)
   cv2.imwrite("media/hsv/"+nueva_r,nuevahvs) 
   rutaa=str("normalizada/"+nueva_r)
   rutab=str("lab/"+nueva_r)
   rutac=str("hsv/"+nueva_r)
   """
   cv2.imshow("orinal",b)
   cv2.imshow("nueva",nueva_ent_bgr)
   cv2.imshow("lab",nuevalab)
   cv2.imshow("hvs",nuevahvs)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   """
   return rutaa,rutab,rutac
   


"""
Funcion para normalizar una imagen para analizar 
"""
def funcion_analizar(img_ref,img_new):#se pide la direccion de la imagen 
    referencia=cv2.imread('media/'+img_ref)
    ajuste_tam(img_new,img_new)
    nueva1=cargar_imagen(img_new)
    nueva_yiq=transformacion_yiq(nueva1)
    referencia_yiq=transformacion_yiq(referencia)
    #y,i,q=promedio(referencia_yiq)
    final_yiq=nueva(referencia_yiq,nueva_yiq)
    nueva_brg=transformarbgr(final_yiq,nueva1)
    cv2.imwrite('media_aux/'+img_new,nueva_brg)





