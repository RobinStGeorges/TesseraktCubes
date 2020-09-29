import requests 
  
# api-endpoint 
URL_base = "http://localhost:5000"
Route_Disconnection = URL_base+"/EventFacesDisco?"
Route_Connection = URL_base+"/EventFacesCo?"
Route_NewID = URL_base+"/newID?"

b0="0"
b1="0"
f0="0"
f1="0"
params_Connection="b0="+b0+"&f0="+f0+"&b1="+b1+"&f1="+f1
params_Disconnection="b0="+b0+"&f0="+f0
params_NewID="dst="+b0

URL= Route_NewID+params_NewID
print URL
r = requests.get(url =URL) 
  
print r.json()