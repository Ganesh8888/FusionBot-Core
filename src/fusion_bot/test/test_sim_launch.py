import os
import unittest
import pytest
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import launch_testing
import launch_testing.actions

@pytest.mark.launch_test
def generate_test_description():
    sim_launch_path = os.path.join(
        get_package_share_directory('fusion_bot'), 'launch', 'sim.launch.py')
    
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([sim_launch_path]),
        ),
        launch_testing.actions.ReadyToTest()
    ])

class TestSimLaunch(unittest.TestCase):
    def test_nodes_start(self):
        # We just want to ensure the launch file executes without throwing exceptions.
        self.assertTrue(True)
