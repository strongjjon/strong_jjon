from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'zero_ros'
share_dir = 'share/' + package_name

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
           (share_dir +'/launch', glob(os.path.join('launch', '*.launch.py'))),
           (share_dir +'/param', glob(os.path.join('param', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zero',
    maintainer_email='zero@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_turtlesim = zero_ros.move_turtlesim:main',
            'move_turtlebot = zero_ros.move_turtlebot:main',
            'simple_pub = zero_ros.simple_pub:main',
            'simple_sub = zero_ros.simple_sub:main',
            'simple_sub2 = zero_ros.simple_sub2:main',
            'simple_time_pub = zero_ros.simple_time_pub:main',
            'simple_time_sub = zero_ros.simple_time_sub:main',
            "move_turtlebot_s = zero_ros.move_turtlebot_s:main",
            "simple_image_sub = zero_ros.simple_image_sub:main",
            "simple_service_server = zero_ros.simple_service_server:main",
            "simple_service_client = zeor_ros.simple_service_client:main",
            "simple_action_server = zero_ros.simple_action_server:main",
            "simple_action_client = zero_ros.simple_action_client:main",
        ],
    },
)
