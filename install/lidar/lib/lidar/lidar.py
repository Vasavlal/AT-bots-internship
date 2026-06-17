#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class LidarPublisher(Node):

    def __init__(self):
        super().__init__('lidar_publisher')

        self.publisher_ = self.create_publisher(
            Int32,
            'numbers',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_distance
        )

        self.distance = 0

        self.get_logger().info('LiDAR Publisher Started')

    def publish_distance(self):

        msg = Int32()
        msg.data = self.distance

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Publishing Distance: {self.distance}'
        )

        self.distance += 1

        if self.distance > 10:
            self.distance = 0


def main(args=None):
    rclpy.init(args=args)

    node = LidarPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()

