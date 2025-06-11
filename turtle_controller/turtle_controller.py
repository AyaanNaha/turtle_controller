#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")

        self.cmd_vel_publisher_ = self.create_publisher(Twist,"/turtle1/cmd_vel", 10)
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)

        self.get_logger().info("turtle_controller node started")
    
    def pose_callback(self, pose: Pose):
        msg = Twist()

        if (pose.x > 10.0 or pose.x < 1.0 or pose.y > 10.0 or pose.y < 1.0):
            msg.angular.z = 2.0
            msg.linear.x = 1.5
            self.get_logger().info("Rotating")
        else:
            msg.angular.z = 0.0
            msg.linear.x = 3.0
            self.get_logger().info("Cruising")
        
        self.cmd_vel_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = TurtleControllerNode()
    rclpy.spin(node)

    rclpy.shutdown()