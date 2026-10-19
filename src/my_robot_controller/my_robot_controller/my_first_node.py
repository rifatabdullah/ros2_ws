#!/usr/bin/env python3

import rclpy
from rclpy.node import Node



class myNode(Node):

    def __init__(self):
        super().__init__("First_Node")
        self.counter = 0
        self.create_timer(1.0,self.timer_callback) # 1.0 is the time in seconds between each call of the timer_callback function

    def timer_callback(self):
        self.get_logger().info("Flying high"+" "+str(self.counter))
        self.counter += 1 



def main(args=None):
    rclpy.init(args=args)

    node = myNode()
    rclpy.spin(node) # node will be running until keyboard interuption 
    rclpy.shutdown()


if __name__ == '__main__':
    main()