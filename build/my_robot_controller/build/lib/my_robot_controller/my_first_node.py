#!/usr/bin/env python3

import rclpy
from rclpy.node import Node



class myNode(Node):

    def __init__(self):
        super().__init__("First_Node")
        self.get_logger().info("Heiiilo!") 



def main(args=None):
    rclpy.init(args=args)

    node = myNode()
    rclpy.spin(node) # node will ben running until keyboard interuption 
    rclpy.shutdown()


if __name__ == '__main__':
    main()