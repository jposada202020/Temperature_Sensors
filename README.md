# Temperature_Sensors

Trying to verify what would be the results.

This could be difficult to deal with memory wise, as the Metro M4 only let you define around ten pin. The library DHT allows you to destroy the object, so you can create
and destruct the object every time. On the long run this could cause memory fragmentation. Tested for two hours cannot notice anything abnormal.
For the DS18, the problem is that the library has not defined method to destroy the object once is created. cannot notice anything abnormal.

Code Test included:
Temperature Sensors:
* DHT11
* DHT22
* DS18x20

They are readed once, around every 8 seconds

## Test Jig Picture

![image](https://user-images.githubusercontent.com/34255413/109373984-22cded00-7880-11eb-9226-ef904c3ac0a2.png)
