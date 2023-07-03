import robomaster
from robomaster import robot


if __name__ == '__main__':
    robomaster.enable_logging_to_file()

    robomaster.config.LOCAL_IP_STR = "192.168.0.12"
    ep_robot = robot.Robot()

    ep_robot.initialize(conn_type='rndis')

    version = ep_robot.get_version()
    print("Robot version: {0}".format(version))
    ep_robot.close()