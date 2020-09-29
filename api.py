import flask
from flask import request, jsonify
import mysql.connector
import serial





app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/UseLED', methods=['GET'])
def home():
    query_parameters = request.args
    cpt=0
    dst = query_parameters.get('dst')
    RColor = query_parameters.get('RColor')
    GColor = query_parameters.get('GColor')
    BColor = query_parameters.get('BColor')
  
    
    if (int(RColor)  > 255):
        cpt=cpt+1
    if (int(RColor) < 0):
        cpt=cpt+1
    if (int(GColor)  > 255 ):
        cpt=cpt+1
    if ( int(GColor) < 0):
        cpt=cpt+1
    if (int(BColor) > 255):
        cpt=cpt+1
    if ( int(BColor) < 0):
        cpt=cpt+1
    if ( dst == 0):
        cpt=cpt+1    
    
    if (cpt== 0):
        ser = serial.Serial('/dev/ttyUSB0',115200)
        data='{'+str.encode(str(dst)+';'+'3'+';'+str(RColor)+';'+str(GColor)+';'+str(BColor))+';0}'
        print data
        ser.write(data)
       
        return "ok"
    else:
        return "Error: params invalid"
    
    
@app.route('/RunBtn', methods=['GET'])
def RunBtn():
    mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from matrice;")
    myresult = mycursor.fetchall()
    #push to Kevin 
    return str(myresult)

        
@app.route('/newID', methods=['GET'])
def newID():
    query_parameters = request.args
    cpt=0
    value=0
    dst = query_parameters.get('dst')
    
    if ( dst == 0):
        cpt=cpt+1    
    
    if (cpt== 0):
        mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT (id_box +1)as new_id FROM `box_list` WHERE `is_connected` = 1 and id_box not like 255 order by id_box desc limit 1")
        myresult = mycursor.fetchone()

        for x in myresult:
            value= str(x)
            
        ser = serial.Serial('/dev/ttyUSB0',115200)
        ser.write('{'+str.encode(str(dst)+';'+'1'+';'+str(value)+';0;0;0}'))
        mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
        mycursor= mydb.cursor()
        query="UPDATE `box_list` SET `id_box`= "+value+" WHERE `id_box` ="+str(dst)
        print query
        mycursor.execute(query)
        query="UPDATE `matrice` SET `id_box`= "+value+" WHERE `id_box` ="+str(dst)
        print query
        mycursor.execute(query)
        mydb.commit()
        mydb.disconnect()
        return str(value)
    else:
        return "Error: params invalid"


@app.route('/EventFacesCo', methods=['GET'])
def EventFacesCo():
    query_parameters = request.args
    cpt=0
    value=0
    b0 = query_parameters.get('b0')
    f0 = query_parameters.get('f0')
    b1 = query_parameters.get('b1')
    f1 = query_parameters.get('f1')
    
    print 'b0 '+b0
    print 'f0 '+f0
    print 'b1 '+b1
    print 'f1 '+f1
    print 'passe'

    if(b0=='255'):
	if b1!='255':
		mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
		mycursor= mydb.cursor()
		query="INSERT INTO `box_list`( `id_box`, `date_last_connection`, `is_connected`) VALUES ("+str(b1)+",NOW(),1);"
		print query
		mycursor.execute(query)
		mydb.commit()
		query="INSERT INTO `matrice`( `id_box`, `coord_x`, `coord_y`) VALUES ("+str(b1)+","+str(0)+","+str(0)+");"
		print query
		mycursor.execute(query)
		mydb.commit()
		return 'ok'

    else:
   
	    mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
	    mycursor = mydb.cursor()
	    mycursor.execute("SELECT (count(*)) as boite_pere FROM `box_list` WHERE `is_connected` = 1 and (id_box ='"+b0+"' or id_box ='"+b1+"')")
	    myresult = mycursor.fetchone()
	    print'c passe'
	    value=( myresult[0]) 
	    print('value')
	    print(value)
	    if(value>0):
		
		mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
		mycursor = mydb.cursor()
		mycursor.execute("SELECT id_box as boite_pere FROM `box_list` WHERE `is_connected` = 1 and (id_box ='"+b0+"' or id_box ='"+b1+"') limit 1")
		myresult = mycursor.fetchone()

		boite_mere=( myresult[0])
		print str(boite_mere)
		print b0


		

		if(str(boite_mere)==str(b0)):
		    print 'b0'
		    boite_mere=b0
		    boite_fille=b1
		    face_mere=f0
		    face_fille=f1
		else:
		    print 'b1'
		    boite_mere=b1
		    boite_fille=b0
		    face_mere=f1
		    face_fille=f0
		print 'face mere :'
		print face_mere

		
		db = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
		mycursor = mydb.cursor()
		query="SELECT (count(*))  FROM `box_list` WHERE (id_box ='"+boite_fille+"')limit 1"
		mycursor.execute(query)
		myresult = mycursor.fetchone()
		boite_fille_existe=( myresult[0])
		print 'exite ?'
		print boite_fille_existe
		
		print 'recuperation coord pere'
		query="SELECT coord_x,coord_y FROM `matrice` WHERE `id_box` ='"+boite_mere+"'"
		print query
		mycursor.execute(query)
		myresult = mycursor.fetchone()
		print 'coord pere recupere : '
		print myresult
		x=( myresult[0])
		y=( myresult[1])
		cpt_err=0;
		new_x=x
		new_y=y
		print 'getcoor'

		print x
		print y

		if(boite_mere=='255'):
		    face_mere="2";
		
		if (face_mere=='0'):
		    print 'y :'
		    print y
		    if(y!=0):
		        new_y=int(y)-1;
		    else :
		        cpt_err=cpt_err+1;
		if (face_mere=='3'):
		    if(y!=0):
		        new_x=int(x)-1;
		    else :
		        cpt_err=cpt_err+1;
		if (face_mere=='2'):
		    new_y=int(y)+1;

		if (face_mere=='1'):
		    new_x=int(x)+1;

		
		if(cpt_err==0):
		    mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
		    mycursor= mydb.cursor()
		    query="INSERT INTO `matrice`( `id_box`, `coord_x`, `coord_y`) VALUES ("+str(boite_fille)+","+str(new_x)+","+str(new_y)+");"
		    print query
		    mycursor.execute(query)
		    mydb.commit()
		    mydb.disconnect()
		    print boite_fille_existe
		    if(boite_fille_existe==0):
		        mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
		        mycursor= mydb.cursor()
		        query="INSERT INTO `box_list`( `id_box`, `date_last_connection`, `is_connected`) VALUES ("+str(boite_fille)+",NOW(),1);"
		        print query
		        mycursor.execute(query)
		        mydb.commit()
		        mydb.disconnect()
		    else :
		        mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
		        mycursor= mydb.cursor()
		        query="UPDATE `box_list` SET `date_last_connection`= NOW(),`is_connected`= 1 WHERE `id_box` ="+str(boite_fille)
		        print query
		        mycursor.execute(query)
		        mydb.commit()
		        mydb.disconnect()

		return 'ok'

    
    
@app.route('/EventFacesDisco', methods=['GET'])
def EventFacesDisco():
    query_parameters = request.args
    cpt=0
    value=0
    b0 = query_parameters.get('b0')
    f0 = query_parameters.get('f0')
    mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT coord_x,coord_y FROM `matrice` WHERE `id_box` ='"+b0+"'")
    myresult = mycursor.fetchone()
    x=( myresult[0])
    y=( myresult[1])
    cpt_err=0;
    new_x=x
    new_y=y
    if(b0=='255'):
        f0="1";
    print f0
    if (f0=='0'):
        
        if(y!=0):
            new_y=int(y)-1;
    if (f0=='1'):
        new_x=int(x)+1;
    if (f0=='2'):
        print 'ici'
        new_y=int(y)+1;
    if (f0=='3'):
        if(y!=0):
            new_x=int(x)-1;
        
    print new_x            
    print 'ici'
    print new_y
    if(cpt_err==0):
        mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
        mycursor = mydb.cursor()
        
        query="SELECT id_box FROM `matrice` WHERE `coord_x` ="+str(new_x)+" and `coord_y` ="+str(new_y)+" limit 1;"
        print query
        mycursor.execute(query)
        myresult = mycursor.fetchone()
        id_b=( myresult[0])
        mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
        mycursor= mydb.cursor()
        query="delete from `matrice` where id_box ="+str(id_b)
        mycursor.execute(query)
        mydb.commit()
        mydb.disconnect()
        
        mydb = mysql.connector.connect(host="localhost",user="admin",passwd="tesserakt",database="tesseraktbdd")
        mycursor= mydb.cursor()
        query="UPDATE `box_list` SET `is_connected`= 0 WHERE `id_box` ="+str(id_b)
        mycursor.execute(query)
        mydb.commit()
        mydb.disconnect()
        
               
        return str(id_b)
    else:
        return str("error")

app.run()