# wateralarm
water watchdog for the ground floor,
a raspberry pi in combination with a water sensor is used to notify a user via pushover in case of an emergency.
* waterinterrupt.py, waits for an interrupt and then notifies via pushover - is run as a systemctl service
* wateralarm.py, is called every minute and logs the current wateralarm flag into a file that is visualized by ...
* waterserver.py, a flask server that streams data to its clients whenever wateralarm.py logs something

## hardware setup
see https://www.instructables.com/id/Raspberry-Pi-water-alarm-system/
