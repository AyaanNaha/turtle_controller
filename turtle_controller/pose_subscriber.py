#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node): # create a class for subscriber node

    def __init__(self):
        super().__init__("pose_subscriber") # name the node
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10) #creating a subscriber that will listen to the /turtle1/pose topic
        self.get_logger().info("Pose Subscriber Node Started") # print to cmd line

    def pose_callback(self, msg: Pose): # callback from the subscriber - runs whenever the subscriber hears something. Need to include the message type as an input
        self.get_logger().info(f"({msg.x},{msg.y})") #just prints the message

def main(args=None):
    rclpy.init(args=args)

    node = PoseSubscriberNode() # make node and spin
    rclpy.spin(node)

    rclpy.shutdown()