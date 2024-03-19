# script for Paul's presnetation
# http://myrobotlab.org/content/my-inmoov-parts-list-and-way-working

headPort = "COM10"

#i01 = Runtime.createAndStart("i01", "InMoov")
#i01.attachArduino("headPort","uno", headPort)

#i01.attachHead("headPort")
#head=i01.startHead(headPort)
mouth = Runtime.createAndStart("mouth","Speech")
mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
#mouth.speakBlocking("Hello. I have powered up")

 
mouthControl = Runtime.createAndStart("mouthControl","MouthControl")
mouthControl.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
mouthControl.connect(headPort)
mouthControl.jaw.detach()
mouthControl.jaw.setPin(26)
mouthControl.jaw.attach()
mouthControl.setmouth(10,35)

#i01.setHeadSpeed(0.2,0.2)
mouthControl.mouth.speak("Good morning")
#i01.head.moveTo(65,66)
mouthControl.mouth.speak("My name is Paul")
#i01.head.moveTo(75,86)
mouthControl.mouth.speak("I am here to introduce you the robotics courses")
#i01.moveHead(65,96)
mouthControl.mouth.speak("at escuuela de pensamiento maatematico")
#i01.moveHead(75,76)
mouthControl.mouth.speak("I only speak english")
#i01.moveHead(65,86)
mouthControl.mouth.speak("but I will learn to speak spanish very soon")
#i01.moveHead(85,86)
mouthControl.mouth.speak("Now I will let Alexander speak")
#i01.moveHead(75,96)
mouthControl.mouth.speak("Thank you")
#i01.moveHead(75,96)
#i01.rest()
#i01.setHeadSpeed(1,1)

