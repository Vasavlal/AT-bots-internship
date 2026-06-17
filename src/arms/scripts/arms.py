#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class ArmController(Node):

    def __init__(self):
        super().__init__('arm_controller')

        self.subscription = self.create_subscription(
            Int32,
            'numbers',
            self.callback,
            10
        )

        self.get_logger().info('Arm Controller Started')

    def callback(self, msg):

        distance = msg.data

        if distance <= 3:
            self.get_logger().info(
                f'Distance={distance} -> ARMS STOP'
            )
        else:
            self.get_logger().info(
                f'Distance={distance} -> ARMS MOVING'
            )


def main(args=None):
    rclpy.init(args=args)
    node = ArmController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
