from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("wrtn_urdf", package_name="wrtn_moveit_config")
        .robot_description(file_path="config/wrtn_urdf.urdf.xacro")
        .robot_description_semantic(file_path="config/wrtn_urdf.srdf")
        
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .to_moveit_configs()
    )
    return generate_demo_launch(moveit_config)
