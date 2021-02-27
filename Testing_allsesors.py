import time
import board
import adafruit_dht
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
import gc

ow_bus = OneWireBus(board.D3)
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

while True:
    try:
        dhtDevice11 = adafruit_dht.DHT11(board.D4)
        temperature_c = dhtDevice11.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice11.humidity
        print(
            "DATA DHT11 Temp : {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
    except RuntimeError as error:
        print(error.args[0])
        continue
    except Exception as error:
        dhtDevice11.exit()
        raise error
    time.sleep(1)
    dhtDevice11.exit()

    try:
        dhtDevice22 = adafruit_dht.DHT22(board.D2)
        temperature_c = dhtDevice22.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice22.humidity
        print(
            "DATA DHT22 Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
    except RuntimeError as error:
        print(error.args[0])
        continue
    except Exception as error:
        dhtDevice22.exit()
        raise error
    time.sleep(1)
    dhtDevice22.exit()

    print("DATA DS18 Temp: {0:0.3f}C".format(ds18.temperature))

    time.sleep(5.0)
    gc.collect()

    print("Mem_Free: {} Bytes".format(gc.mem_free()))
