from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
from pymavlink import mavutil

vehicle = connect('/dev/ttyUSB0', wait_ready=True, baud=921600)


def servo(channel, sv):
    # input the message
    msg = vehicle.message_factory.command_long_encode(0, 0,  # target system, target component
                                                      mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
                                                      0,  # konfirmasi
                                                      channel,  # pin relay pada AUX OUT 3
                                                      sv,  # pwm value
                                                      0, 0, 0, 0, 0)  # param 1 ~ 5 ga dipake
    # send command to vehicle
    vehicle.send_mavlink(msg)
    vehicle.flush()
servo(3, 1900)