import board
import adafruit_dht
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
import gc
import time


initial_memory = gc.mem_free()
dhtDevice0 = adafruit_dht.DHT11(board.D0)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)


dhtDevice1 = adafruit_dht.DHT11(board.D1)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)

dhtDevice2 = adafruit_dht.DHT11(board.D2)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)

dhtDevice3 = adafruit_dht.DHT11(board.D3)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)

dhtDevice4 = adafruit_dht.DHT11(board.D4)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)

dhtDevice5 = adafruit_dht.DHT11(board.D5)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)

dhtDevice6 = adafruit_dht.DHT11(board.D6)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)

dhtDevice7 = adafruit_dht.DHT11(board.D7)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)

dhtDevice8 = adafruit_dht.DHT11(board.D8)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)


dhtDevice9 = adafruit_dht.DHT11(board.D9)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)

dhtDevice10 = adafruit_dht.DHT11(board.D10)
current_memory = gc.mem_free()
print("Mem_Free: {} Bytes".format(current_memory))
time.sleep(1)

