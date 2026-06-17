#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class WheelController(Node):

    def __init__(self):
        super().__init__('wheel_controller')

        self.subscription = self.create_subscription(
            Int32,
            'numbers',
            self.callback,
            10
        )

        self.get_logger().info('Wheel Controller Started')

    def callback(self, msg):

        distance = msg.data

        if distance <= 3:
            self.get_logger().info(
                f'Distance = {distance} --> STOP WHEELS'
            )
        else:
            self.get_logger().info(
                f'Distance = {distance} --> MOVE WHEELS'
            )


def main(args=None):
    rclpy.init(args=args)

    node = WheelController()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
