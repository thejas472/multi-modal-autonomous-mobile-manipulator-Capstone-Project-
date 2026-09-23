#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import JointState
from std_msgs.msg import Float32MultiArray


class JointStatesToESP32(Node):

    def __init__(self):
        super().__init__('joint_states_to_esp32')

        # =====================================================
        # SUBSCRIBER
        # =====================================================

        self.sub = self.create_subscription(
            JointState,
            '/joint_states',
            self.callback,
            10
        )

        # =====================================================
        # PUBLISHER
        # =====================================================

        self.pub = self.create_publisher(
            Float32MultiArray,
            '/joint_commands',
            10
        )

        # =====================================================
        # JOINT NAMES
        # =====================================================

        self.arm_joints = [
            'base_joint',
            'shoulder_joint',
            'elbow_joint',
            'wrist_roll_joint',
            'wrist_pitch_link',
            'finger_gripper_joint'
        ]

        self.get_logger().info(
            'ESP32 Arm Bridge Started'
        )

    # =========================================================
    # RADIAN -> SERVO DEGREE
    # =========================================================

    def map_angle(
        self,
        rad,
        rad_min,
        rad_max,
        servo_min,
        servo_max,
        invert=False
    ):

        # Limit incoming joint angle
        rad = max(rad_min, min(rad_max, rad))

        # Normalize 0.0 -> 1.0
        normalized = (
            (rad - rad_min) /
            (rad_max - rad_min)
        )

        # Optional inversion
        if invert:
            normalized = 1.0 - normalized

        # Convert to servo degrees
        servo_angle = (
            servo_min +
            normalized *
            (servo_max - servo_min)
        )

        return max(
            0.0,
            min(180.0, servo_angle)
        )

    # =========================================================
    # CALLBACK
    # =========================================================

    def callback(self, msg):

        name_to_pos = dict(
            zip(msg.name, msg.position)
        )

        # -----------------------------------------------------
        # Make sure all joints exist
        # -----------------------------------------------------

        if not all(
            joint in name_to_pos
            for joint in self.arm_joints
        ):
            return

        # =====================================================
        # BASE
        #
        # URDF:
        # -pi -> +pi
        #
        # Servo:
        # 0 -> 180
        # =====================================================

        base_deg = self.map_angle(
            name_to_pos['base_joint'],
            -math.pi,
            math.pi,
            0,
            180
        )

        # =====================================================
        # SHOULDER
        #
        # URDF:
        # -pi/2 -> +pi/2
        #
        # Servo:
        # 20 -> 160
        # =====================================================

        shoulder_deg = self.map_angle(
            name_to_pos['shoulder_joint'],
            -math.pi / 2,
            math.pi / 2,
            20,
            160
        )

        # =====================================================
        # ELBOW
        #
        # URDF:
        # -1.2 -> 2.356
        #
        # Servo:
        # 0 -> 180
        #
        # Inverted because of physical servo orientation.
        # =====================================================

        elbow_deg = self.map_angle(
            name_to_pos['elbow_joint'],
            -1.2,
            2.356194,
            0,
            180,
            invert=True
        )

        # =====================================================
        # WRIST ROLL
        #
        # URDF:
        # -pi -> +pi
        #
        # Servo:
        # 0 -> 180
        #
        # Inverted for physical orientation.
        # =====================================================

        wrist_roll_deg = self.map_angle(
            name_to_pos['wrist_roll_joint'],
            -math.pi,
            math.pi,
            0,
            180,
            invert=True
        )

        # =====================================================
        # WRIST PITCH
        #
        # URDF:
        # -pi/2 -> +pi/2
        #
        # Servo:
        # 0 -> 180
        #
        # This gives the WRIST PITCH the maximum software range.
        # =====================================================

        wrist_pitch_deg = self.map_angle(
            name_to_pos['wrist_pitch_link'],
            -math.pi / 2,
            math.pi / 2,
            0,
            180
        )

        # =====================================================
        # GRIPPER
        #
        # URDF:
        # 0 -> 0.8 rad
        #
        # Instead of only commanding 30 -> 75.8 degrees,
        # expand it to:
        #
        # OPEN   = 10 degrees
        # CLOSED = 150 degrees
        #
        # Adjust these later if the mechanism hits a limit.
        # =====================================================

        gripper_deg = self.map_angle(
            name_to_pos['finger_gripper_joint'],
            0.0,
            0.8,
            10,
            150
        )

        # =====================================================
        # CREATE COMMAND
        # =====================================================

        out = Float32MultiArray()

        out.data = [
            float(base_deg),
            float(shoulder_deg),
            float(elbow_deg),
            float(wrist_roll_deg),
            float(wrist_pitch_deg),
            float(gripper_deg)
        ]

        self.pub.publish(out)

        # =====================================================
        # DEBUG
        # =====================================================

        self.get_logger().info(
            'Commands: '
            f'B={base_deg:.1f} '
            f'S={shoulder_deg:.1f} '
            f'E={elbow_deg:.1f} '
            f'WR={wrist_roll_deg:.1f} '
            f'WP={wrist_pitch_deg:.1f} '
            f'G={gripper_deg:.1f}'
        )


# =============================================================
# MAIN
# =============================================================

def main(args=None):

    rclpy.init(args=args)

    node = JointStatesToESP32()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:

        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()

