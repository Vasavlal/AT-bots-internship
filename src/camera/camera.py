#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO

class ObjectDetector(Node):

    def __init__(self):
        super().__init__('object_detector')

        self.bridge = CvBridge()

        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

        self.model = YOLO('yolov8n.pt')

        self.get_logger().info('Object Detector Started')

    def image_callback(self, msg):

        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        results = self.model(frame)

        for result in results:

            for box in result.boxes:

                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]

                self.get_logger().info(
                    f'Object Detected: {label}'
                )

def main(args=None):

    rclpy.init(args=args)

    node = ObjectDetector()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
