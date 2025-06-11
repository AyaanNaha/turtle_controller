#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node): # creating node with class, need to input Node as dependency
    def __init__(self):
        super().__init__("draw_circle") # names the node

        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) # creating a publisher to cmd_vel topic
        self.timer_ = self.create_timer(0.5, self.send_velocity_command) # creates a timer that calls the send_velocity_command each 0.5 secs
         
        self.get_logger().info("Draw circle node has been started") # prints to cmd line 
    
    def send_velocity_command(self):
        msg = Twist() # creating a Twist type message for the publisher
        msg.linear.x = 2.0
        msg.angular.z = 1.0

        self.cmd_vel_pub_.publish(msg) #publish the actual message

def main(args=None): # Main code
    rclpy.init(args=args) #initialize ros

    node = DrawCircleNode() #create node
    rclpy.spin(node) # keeps node running until ctrl + c

    rclpy.shutdown() # shutdown ros