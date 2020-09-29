import os, sys
import serial
import time
import ast
import requests 


# api-endpoint 
URL_base = "http://localhost:5000"
Route_Disconnection = URL_base+"/EventFacesDisco?"
Route_Connection = URL_base+"/EventFacesCo?"
Route_NewID = URL_base+"/newID?"
Route_btn = URL_base+"/RunBtn?"

def askingNew_ID(fonction,origine):
    params_NewID="dst="+str(origine)
    URL= Route_NewID+params_NewID
    r = requests.get(url =URL) 
    print ("make request to API NewID_fct : "+str(fonction)+", origine:"+str(origine))

def ConnectionDetected(fonction,origine,face,origine2,face2):
    params_Connection="b0="+str(origine)+"&f0="+str(face)+"&b1="+str(origine2)+"&f1="+str(face2)
    URL= Route_Connection+params_Connection
    r = requests.get(url =URL)
    print ("make request to API Newconnection_fct : "+str(fonction)+", origine1:"+str(origine)+", origine2:"+str(origine2)+", face:"+str(face)+", face2:"+str(face2))

def DisconnectionDetected(fonction,origine,face):
    params_Disconnection="b0="+str(origine)+"&f0="+str(face)
    URL= Route_Disconnection+params_Disconnection
    r = requests.get(url =URL) 
    print ("make request to API Newdisconnection_fct : "+str(fonction)+", origine1:"+str(origine)+",from face:"+str(face))

def RunBTN():
    params_Disconnection=""
    URL= Route_btn+params_Disconnection
    r = requests.get(url =URL) 
    print ("make request to API run big button ")

ser = serial.Serial('/dev/ttyUSB0', 115200, 8, 'N', 1, timeout=1)

while True:
   line = ser.readline()
   if (len(line)>0 ):
        line= ast.literal_eval(line)
        print (line)
        cpt=0
        if(int(line[0])==0):
            fonction= (line[0])
            origine= (line[1])
            askingNew_ID(fonction,origine)
        elif((line[0])==4):
            state= (line[5])
            if (state==0):
                fonction= (line[0])
                origine= (line[1])
                face= (line[2])
                DisconnectionDetected(fonction,origine,face)
            elif(state==1):
                fonction= (line[0])
                origine= (line[1])
                face= (line[2])
                origine2= (line[3])
                face2= (line[4])
                ConnectionDetected(fonction,origine,face,origine2,face2)
        elif((line[0])==5):
            RunBTN()
            
                    
                                 
                    



                          

                 
                                   
          