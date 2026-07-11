#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped


class TwistStamper(Node):

    def __init__(self):

        super().__init__('twist_stamper')

        self.pub = self.create_publisher(
            TwistStamped,
            '/diff_drive_controller/cmd_vel',
            10)

        self.sub = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.callback,
            10)

    def callback(self, msg):

        self.get_logger().info(
            f"Received Twist: linear.x={msg.linear.x}, angular.z={msg.angular.z}"
        )

        stamped = TwistStamped()

        stamped.header.stamp = self.get_clock().now().to_msg()
        stamped.header.frame_id = "base_link"

        stamped.twist = msg

        self.pub.publish(stamped)

        self.get_logger().info("Published TwistStamped")


def main():

    rclpy.init()

    node = TwistStamper()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
