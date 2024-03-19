# script for Paul's presentation
# http://myrobotlab.org/content/my-inmoov-parts-list-and-way-working
print ("Starting Paul's code...")


LeftPort = "COM10"
rightPort = "COM29"

#RIGHT ARM SERVO VALUES
#Set here the correct values when installing new servos, This are absolute values.
R_bicep_Min=25			#Extended
R_bicep_Max=80			#Compressed
R_bicep_Rest=25		#Extended

R_rotate_Min=80		#Towards de body
R_rotate_Max=175		#Open, oposit to the body
R_rotate_Rest=113		#Just to the front

R_shoulder_Min=60		#Backwards
R_shoulder_Max=150		#Forward
R_shoulder_Rest=90		#Arm vertical

R_omoplate_Min=90		#Closed to the body
R_omoplate_Max=125		#Open
R_omoplate_Rest=90		#Closed to the body

R_thumb_Min=180		#Open, extended
R_thumb_Max=100		#Closed
R_thumb_Rest=180		#Open, extended

R_index_Min=155		#Open, extended
R_index_Max=80			#Closed
R_index_Rest=155		#Open, extended

R_majeure_Min=165		#Open, extended
R_majeure_Max=70		#Closed
R_majeure_Rest=165		#Open, extended

R_ringFinger_Min=165	#Open, extended
R_ringFinger_Max=65		#Closed
R_ringFinger_Rest=165	#Open, extended

R_pinky_Min=165		#Open, extended
R_pinky_Max=95			#Closed
R_pinky_Rest=165		#Open, extended

#LEFT ARM SERVO VALUES
#Set here the correct values when installing new servos, This are absolute values.
#LEFT ARM

L_thumb_Min=10			#Open, extended
L_thumb_Max=90			#Closed
L_thumb_Rest=10		#Open, extended

L_index_Min=6			#Open, extended
L_index_Max=80			#Closed
L_index_Rest=6			#Open, extended

L_majeure_Min=10		#Open, extended
L_majeure_Max=105		#Closed
L_majeure_Rest=10		#Open, extended

L_ringFinger_Min=6		#Open, extended
L_ringFinger_Max=75		#Closed
L_ringFinger_Rest=6		#Open, extended

L_pinky_Min=15			#Open, extended
L_pinky_Max=90			#Closed
L_pinky_Rest=15		#Open, extended

def Demo1():
#DEMO Movimientos generales brazo dcho

	mouthControl.mouth.speak("Let me show you how I move my arm")
	i01.head.moveTo(130,90)
	sleep(4)

	#Bicep UP
	i01.moveArm("right",180,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(5)
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(2)

	#Shoulder forward, back and rest
	i01.moveArm("right",175,R_rotate_Rest_Rel,180,R_omoplate_Rest_Rel)
	sleep(7)
	i01.handClose("right")
	sleep(7)
	i01.moveArm("right",175,R_rotate_Rest_Rel,0,R_omoplate_Rest_Rel)
	sleep(7)
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(5)
	
	#Omoplate UP and down
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,180)
	sleep(5)
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(5)
	
	#Rotate
	i01.moveArm("right",175,140,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(7)
	i01.moveArm("right",175,0,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(7)
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(5)
	
	#Hand close, open
	i01.handClose("right")
	sleep(7)
	i01.handOpen("right")
	sleep(5)
	i01.handRest("right")
	sleep(5)
	
	#Everything to its normal rest position
	i01.moveArm("right",R_bicep_Rest_Rel,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	
	sleep(10)
	return

def Demo2():
#DEMO Toma objeto y lo deja en mesa

	#Bicep UP
	i01.moveArm("right",180,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(5)
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(5)

	mouthControl.mouth.speak("put an object in my hand please")
	i01.head.moveTo(160,76)
	sleep(4)

	#take
	i01.moveHand("right", 140, 140, 140, 140, 140);
	sleep(7)

	#Shoulder forward
	i01.moveArm("right",175,R_rotate_Rest_Rel,180,R_omoplate_Rest_Rel)
	sleep(7)
		
	#Rotate
	i01.moveArm("right",175,0,180,R_omoplate_Rest_Rel)
	sleep(7)

	mouthControl.mouth.speak("now y drop it")
	i01.head.moveTo(140,35)
	sleep(4)

	#drop
	i01.handOpen("right")
	sleep(5)
	
	#Everything to its normal rest position
	i01.moveArm("right",R_bicep_Rest_Rel,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	i01.handRest("right")
	
	sleep(10)
	return

def Demo3():
#DEMO Just speak and move head
	
	mouthControl.mouth.speak("Good morning")
	i01.head.moveTo(70,30,80,90)
	sleep(4)
	
	mouthControl.mouth.speak("My name is Paul Inmoov")
	i01.head.moveTo(130,90)
	sleep(4)
	mouthControl.mouth.speak("I was originally designed by Gal Langvaan")
	i01.head.moveTo(150,40)
	sleep(4)
	mouthControl.mouth.speak("and built by Alecandro Alonso")
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
	return

def Demo4():
#DEMO General demonstration of head and right arm

	mouthControl.mouth.speak("Good morning")
	i01.head.moveTo(70,30,80,90)
	sleep(4)
	
	mouthControl.mouth.speak("My name is Paul Inmoov")
	i01.head.moveTo(130,90)
	sleep(4)

	mouthControl.mouth.speak("At this moment I just have one arm, but I will show you how I use it")
	i01.head.moveTo(150,40)
	sleep(4)

	mouthControl.mouth.speak("Now I will activate my bicep slowly")
	i01.head.moveTo(130,90)
#	sleep(4)

	#Bicep UP
	i01.moveArm("right",180,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(5)
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(2)

	mouthControl.mouth.speak("and now I extend and then recover my arm")
	i01.head.moveTo(160,76)
#	sleep(4)

	#Shoulder forward, back and rest
	i01.moveArm("right",R_bicep_Rest_Rel,R_rotate_Rest_Rel,180,R_omoplate_Rest_Rel)
	sleep(7)
	i01.handClose("right")
	sleep(7)
	i01.moveArm("right",180,R_rotate_Rest_Rel,0,R_omoplate_Rest_Rel)
	sleep(7)
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(5)
	
	#Omoplate UP and down
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,180)
	sleep(5)
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(5)
	
	#Rotate
	i01.moveArm("right",175,140,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(7)
	i01.moveArm("right",175,0,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(7)
	i01.moveArm("right",175,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	sleep(5)
	
	#Hand close, open
	i01.handClose("right")
	sleep(7)
	i01.handOpen("right")
	sleep(5)
	i01.handRest("right")
	sleep(5)
	
	#Everything to its normal rest position
	i01.moveArm("right",R_bicep_Rest_Rel,R_rotate_Rest_Rel,R_shoulder_Rest_Rel,R_omoplate_Rest_Rel)
	
	sleep(10)
	return

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

#LEFT ARM
#rh.thumb.setMinMax(10,90)
#rh.index.setMinMax(6,80)
#rh.majeure.setMinMax(10,105)
#rh.ringFinger.setMinMax(6,75)
#rh.pinky.setMinMax(15,90)


#RIGHT ARM CONFIGURATION
ra = Runtime.create("i01.rightArm","InMoovArm")
rh = Runtime.create("i01.rightHand","InMoovHand")

#Conversion from absolute servo limits to relative limits (0..180)
ra.bicep.map     (0,180,R_bicep_Min,R_bicep_Max)
ra.rotate.map    (0,180,R_rotate_Min,R_rotate_Max)
ra.shoulder.map  (0,180,R_shoulder_Min,R_shoulder_Max)
ra.omoplate.map  (0,180,R_omoplate_Min,R_omoplate_Max)

rh.thumb.map     (0,180,R_thumb_Min,R_thumb_Max)
rh.index.map     (0,180,R_index_Min,R_index_Max)
rh.majeure.map   (0,180,R_majeure_Min,R_majeure_Max)
rh.ringFinger.map(0,180,R_ringFinger_Min,R_ringFinger_Max)
rh.pinky.map     (0,180,R_pinky_Min,R_pinky_Max)


#Definition of rest position relative to Min/Max Angles (value 0 is the Min and 180 is the Max)
R_bicep_Rest_Rel=     180 * (R_bicep_Rest - R_bicep_Min)           / (R_bicep_Max - R_bicep_Min)
R_rotate_Rest_Rel=    180 * (R_rotate_Rest - R_rotate_Min)         / (R_rotate_Max - R_rotate_Min)
R_shoulder_Rest_Rel=  180 * (R_shoulder_Rest - R_shoulder_Min)     / (R_shoulder_Max - R_shoulder_Min)
R_omoplate_Rest_Rel=  180 * (R_omoplate_Rest - R_omoplate_Min)     / (R_omoplate_Max - R_omoplate_Min)

R_thumb_Rest_Rel=     180 * (R_thumb_Rest - R_thumb_Min)           / (R_thumb_Max - R_thumb_Min)
R_index_Rest_Rel=     180 * (R_index_Rest - R_index_Min)           / (R_index_Max - R_index_Min)
R_majeure_Rest_Rel=   180 * (R_majeure_Rest - R_majeure_Min)       / (R_majeure_Max - R_majeure_Min)
R_ringFinger_Rest_Rel=180 * (R_ringFinger_Rest - R_ringFinger_Min) / (R_ringFinger_Max - R_ringFinger_Min)
R_pinky_Rest_Rel=     180 * (R_pinky_Rest - R_pinky_Min)           / (R_pinky_Max - R_pinky_Min)

ra.bicep.setRest(R_bicep_Rest_Rel)
ra.rotate.setRest(R_rotate_Rest_Rel)
ra.shoulder.setRest(R_shoulder_Rest_Rel)
ra.omoplate.setRest(R_omoplate_Rest_Rel)

rh.thumb.setRest(R_thumb_Rest_Rel)
rh.index.setRest(R_index_Rest_Rel)
rh.majeure.setRest(R_majeure_Rest_Rel)
rh.ringFinger.setRest(R_ringFinger_Rest_Rel)
rh.pinky.setRest(R_pinky_Rest_Rel)

#Start Services
i01.startRightArm(rightPort)
i01.startRightHand(rightPort)

#Set speed 
i01.setArmSpeed("right", 0.20, 0.20, 0.20, 0.20)
i01.setHandSpeed("right", 0.80, 0.80, 0.80, 0.80, 0.80)


Demo3()

Demo2()

Demo1()


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

