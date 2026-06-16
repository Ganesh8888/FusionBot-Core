import os
import subprocess
from ament_index_python.packages import get_package_share_directory

def test_urdf_parsing():
    urdf_path = os.path.join(
        get_package_share_directory("fusion_bot"), "description", "robot.urdf.xacro"
    )
    result = subprocess.run(
        ["xacro", urdf_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    assert result.returncode == 0, f"Xacro parsing failed: {result.stderr.decode()}"
