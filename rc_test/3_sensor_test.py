from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
  pressure = sense.get_pressure()
  temp = sense.get_temperature()
  humidity = sense.get_humidity()

  p = round(pressure, 2)
  t = round(temp, 2)
  h = round(humidity, 2)

  msg = "Press : " + str(p) + "  Temp : " + str(t) + "  Humid : " + str(h)
  print(msg)
  sleep(0.1)