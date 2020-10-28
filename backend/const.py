from queue import Queue
from collections import OrderedDict

## Shared between MQTT listener and Data collector
data_queue = Queue()

## Stores positions of devices encountered so far
positions = OrderedDict()

## Coordinates of the anchor nodes
ANCHORS = {
	'30:AE:A4:18:2F:28' : [0,0],
	'80:7D:3A:C5:0D:94' : [560,580],
	'24:6F:28:25:07:A4'	: [980,0]
}

## RSSI Model

# Old model
# A = -2.031862 
# B = -8.7073472

# Total
# A = -8.033376
# B = -7.912847
## Device 0,0
# A = -19.096085
# B = -6.212227
## Device 560,580
# A = 1.65022
# B = -9.596229
## Device 980,0
# A = -19.424024
# B = -5.5061473

A = -2.031862 
B = -9.2

TIME_WINDOW = 1

