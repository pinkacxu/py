import requests
import  RPi.GPIO as GPIO
import  time
COUNT=5
PIN = 11
GPIO.setmode( GPIO.BOARD ) 
GPIO.setup( PIN, GPIO.OUT )
def  low(COUNT):
    for i in range( COUNT ):
            GPIO.output( PIN,True ) 
            time.sleep( 1 )
            GPIO.output( PIN,False )
            time.sleep( 1 )
            GPIO.cleanup()
           
    
    
url = "https://api.openweathermap.org/data/2.5/forecast?q="
cood = "lat=35.0186&lon=135.75553"
city = "Kyoto,JP"
key =  "b87a75ea8b7164ec2b221d58c85ea7ed" 
cnt = 1 # Next 24 hours
r = requests.get( url + city + "&cnt=" + str(cnt) +
"&units=metric" + "&appid=" + key )
rj = r.json()
print( "City =", rj['city']['name'] )
for i in range( rj[ 'cnt' ] ):
    dt = rj['list'][i]['dt_txt']
    id = rj['list'][i]['weather'][0]['id']
    wd = rj['list'][i]['weather'][0]['description']
    print( dt, ":", id, wd )
    if id >=200 and id<300:
        print("thunderstorm will come")
    elif id >=300 and id<500:
        print("Drizzle will come")
    elif id >=500 and id<600:
        low(5)
        print("Rain will come")
    elif id >=600 and id<700:
        print("Snow will come")
    elif id >=700 and id<800:
        print("Atmosphere")
    elif id>800:
        print("Clouds will come")
