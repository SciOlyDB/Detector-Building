from ti_hub import *
detectorbuilding=analog_in("BB 5")
analogvalue=detectorbuilding.measurement()
text_at(6,"Analog in value = "+str(analogvalue),"left")

[
for n in range(200):
 a=detectorbuilding.measurement()
 text_at(6,"ANALOG in = "+str(a),"left")
 sleep(.1)

]


