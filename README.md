# wateralarm
water watchdog for the ground floor,
a raspberry pi in combination with a water sensor is used to notify a user via pushover in case of an emergency.
* waterinterrupt.py, waits for an interrupt and then notifies via pushover - is run as a systemctl service
* wateralarm.py, is called every minute and logs the current wateralarm flag into a file that is visualized by ...
* waterserver.py, a flask server that streams data to its clients whenever wateralarm.py logs something

## hardware setup
see https://www.instructables.com/id/Raspberry-Pi-water-alarm-system/

* PSU: https://www.amazon.de/gp/product/B00K7EKI8S/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1
  This PSU is cheap and generates 12V and 5V out of the box. Wire pins (i.e. https://www.amazon.com/SIM-NAT-Breadboard-Arduino-Raspberry/dp/B06XRV92ZB?ref_=fsclp_pl_dp_1) can be used to connect the raspberry pi and the watersenser (no soldering required)
* Watersensor: https://www.amazon.de/gp/product/B00AMCONRM/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1
