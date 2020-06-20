import requests
import  RPi.GPIO as GPIO
import  time
def  low(COUNT,S1,S2):
    PIN = 11
    GPIO.setmode( GPIO.BOARD ) 
    GPIO.setup( PIN, GPIO.OUT )
    
    for i in range(COUNT):
            GPIO.output( PIN,True ) 
            time.sleep( S1)
            GPIO.output( PIN,False )
            time.sleep( S2 )
            
    GPIO.cleanup()

def  snow(COUNT,S1,S2):
    PIN = 11
    GPIO.setmode( GPIO.BOARD ) 
    GPIO.setup( PIN, GPIO.OUT )
    
    for j in range(2):
        time.sleep( 2 ) 
        for i in range(COUNT):
            GPIO.output( PIN,True ) 
            time.sleep( S1)
            GPIO.output( PIN,False )
            time.sleep( S2 )
         
    GPIO.cleanup()
    
def  opew(cnt,i) :   
    url = "https://api.openweathermap.org/data/2.5/forecast?q="
    cood = "lat=35.0186&lon=135.75553"
    city = "Kyoto,JP"
    key =  "b87a75ea8b7164ec2b221d58c85ea7ed" 
    # Next 24 hours
    r = requests.get( url + city + "&cnt=" + str(cnt) +
    "&units=metric" + "&appid=" + key )
    rj = r.json()
    print( "City =", rj['city']['name'] )
    dt = rj['list'][i]['dt_txt']
    id = rj['list'][i]['weather'][0]['id']
    wd = rj['list'][i]['weather'][0]['description']
    print( dt, ":", id, wd )
    if id >=200 and id<300:
            print("thunderstorm will come")
            low(5,0.2,0.2)
    elif id >=300 and id<500:
            print("Drizzle will come")
            low(5,2,2)
    elif id >=500 and id<600:
            print("Rain will come")
            low(5,1,1)
    elif id >=600 and id<700:
            print("Snow will come")
            snow(3,0.5,0.2)
    elif id>=700:
            print("Clouds will come")
            low(2,0.5,0.5)
opew(8,1)
time.sleep( 6 )
opew(8,6)
