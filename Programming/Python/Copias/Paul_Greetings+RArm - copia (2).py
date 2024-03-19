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
i01.head.moveTo(105,105)

#RIGHT ARM CONFIGURATION
ra = Runtime.create("i01.rightArm","InMoovArm")
rh = Runtime.create("i01.rightHand","InMoovHand")

#Definition of Min & Max angles for each servo
ra.bicep.setMinMax(90,150)
ra.rotate.setMinMax(60,135)
ra.shoulder.setMinMax(60,150)
ra.omoplate.setMinMax(90,125)
rh.thumb.setMinMax(10,90)
rh.index.setMinMax(6,80)
rh.majeure.setMinMax(10,105)
rh.ringFinger.setMinMax(6,75)
rh.pinky.setMinMax(15,90)

#Definition of rest position relative to Min/Max Angles (value 0 is the Min and 180 is the Max)
ra.bicep.setRest(0)
ra.rotate.setRest(128)
ra.shoulder.setRest(60)
ra.omoplate.setRest(0)
rh.thumb.setRest(0)
rh.index.setRest(0)
rh.majeure.setRest(0)
rh.ringFinger.setRest(0)
rh.pinky.setRest(0)

#Start Services
i01.startRightArm(rightPort)
i01.startRightHand(rightPort)

#Set speed 
i01.setArmSpeed("right", 0.20, 0.20, 0.20, 0.20)
i01.setHandSpeed("right", 0.80, 0.80, 0.80, 0.80, 0.80)

i01.moveArm("right",0,128,60,5)
sleep(4)
i01.moveArm("right",0,128,60,0)

#sleep(10)

i01.moveHand("right",180,0,0,0,0,0)
sleep(0.5)
i01.moveHand("right",180,180,0,0,0,0)
sleep(0.5)
i01.moveHand("right",180,180,180,0,0,0)
sleep(0.5)
i01.moveHand("right",180,180,180,180,0,0)
sleep(0.5)
i01.moveHand("right",180,180,180,180,180,0)
sleep(4)
i01.moveHand("right",0,0,0,0,0,0)
sleep(6)

i01.moveHand("right",180,0,0,0,0,0)
sleep(0.5)
i01.moveHand("right",180,180,0,0,0,0)
sleep(0.5)
i01.moveHand("right",180,180,180,0,0,0)
sleep(0.5)
i01.moveHand("right",180,180,180,180,0,0)
sleep(0.5)
i01.moveHand("right",180,180,180,180,180,0)
sleep(4)
i01.moveHand("right",0,0,0,0,0,0)
sleep(6)

i01.moveHand("right",180,0,0,0,0,0)
sleep(0.5)
i01.moveHand("right",180,180,0,0,0,0)
sleep(0.5)
i01.moveHand("right",180,180,180,0,0,0)
sleep(0.5)
i01.moveHand("right",180,180,180,180,0,0)
sleep(0.5)
i01.moveHand("right",180,180,180,180,180,0)
sleep(4)
i01.moveHand("right",0,0,0,0,0,0)
sleep(8)

#sleep(10)

#i01.moveArm("right",0,128,60,0)
#sleep(4)
#i01.moveArm("right",90,0,0,90)
#sleep(4)
#i01.moveArm("right",180,128,140,90)
#sleep(6)
#i01.moveArm("right",180,180,180,140)
#sleep(4)
#i01.moveArm("right",0,128,60,0)
#sleep(10)





i01.setHeadSpeed(1,1)
i01.head.detach()
i01.rightArm.detach()
i01.rightHand.detach()

