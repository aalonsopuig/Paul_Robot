# script for Paul's presentation
# http://myrobotlab.org/content/my-inmoov-parts-list-and-way-working
print ("Starting Paul's code...")


LeftPort = "COM10"
rightPort = "COM29"

i01 = Runtime.createAndStart("i01", "InMoov")

# Head configuration
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

#RIGHT ARM CONFIGURATION
ra = Runtime.create("i01.rightArm","InMoovArm")

#Definition of Min & Max angles for each servo
ra.bicep.setMinMax(90,150)
ra.rotate.setMinMax(60,135)
ra.shoulder.setMinMax(60,150)
ra.omoplate.setMinMax(90,125)

#Definition of rest position relative to Min/Max Angles (value 0 is the Min and 180 is the Max)
ra.bicep.setRest(0)
ra.rotate.setRest(128)
ra.shoulder.setRest(60)
ra.omoplate.setRest(0)

i01.startRightArm(rightPort)
i01.setArmSpeed("right", 0.20, 0.20, 0.20, 0.20)

sleep(10)

i01.moveArm("right",0,128,60,0)
sleep(4)
i01.moveArm("right",90,0,0,90)
sleep(4)
i01.moveArm("right",180,128,140,90)
sleep(6)
i01.moveArm("right",180,180,180,140)
sleep(4)
i01.moveArm("right",0,128,60,0)
sleep(10)





i01.setHeadSpeed(1,1)
i01.head.detach()
i01.rightArm.detach()

