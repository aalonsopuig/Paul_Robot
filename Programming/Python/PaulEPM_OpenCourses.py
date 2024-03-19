# script for Paul's presentation
# http://myrobotlab.org/content/my-inmoov-parts-list-and-way-working
print ("Starting Paul's code...")


LeftPort = "COM3"

i01 = Runtime.createAndStart("i01", "InMoov")
head = i01.startHead(LeftPort)
i01.head.jaw.detach();
mouthControl = i01.startMouthControl(LeftPort)
mouth = Runtime.createAndStart("mouth","Speech")
i01.head.jaw.attach();


#webgui = Runtime.createAndStart("webgui", "WebGUI")

mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
#mouth.speakBlocking("Hello. I have powered up")

 
mouthControl.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
mouthControl.setmouth(10,180) 

i01.setHeadSpeed(0.5,0.5)
i01.head.moveTo(110,110)
sleep(4)

mouthControl.mouth.speak("Good morning")
i01.head.moveTo(70,30,80,90)
sleep(4)

mouthControl.mouth.speak("My name is Paul Inmoov")
i01.head.moveTo(130,90)
sleep(4)
mouthControl.mouth.speak("I was originally designed by Gal Langvan")
i01.head.moveTo(150,40)
sleep(4)
mouthControl.mouth.speak("and built by Alejandro Alonso")
i01.head.moveTo(160,76)
sleep(4)
mouthControl.mouth.speak("I only speak english")
i01.head.moveTo(140,35)
sleep(4)
mouthControl.mouth.speak("but I may learn to speak spanish soon")
i01.head.moveTo(160,110)
sleep(4)
mouthControl.mouth.speak("It will be a pleasure to be your friend")
i01.head.moveTo(150,50)
sleep(4)
mouthControl.mouth.speak("Thank you")
i01.head.moveTo(110,110)
sleep(4)

"""
i01.head.moveTo(70,150)
sleep(4)
i01.head.moveTo(100,76)
sleep(4)
i01.moveHead(70,86)
sleep(4)
i01.moveHead(110,110)
sleep(4)
i01.moveHead(75,50)
sleep(4)
i01.moveHead(90,100)
sleep(4)
"""
i01.setHeadSpeed(1,1)
i01.head.detach()

