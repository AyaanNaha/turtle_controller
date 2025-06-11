from setuptools import find_packages, setup

package_name = 'turtle_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ayaan',
    maintainer_email='ayaan.naha26@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = turtle_controller.my_first_node:main",
            "draw_circle = turtle_controller.draw_circle:main",
            "pose_subscriber = turtle_controller.pose_subscriber:main",
            "turtle_controller = turtle_controller.turtle_controller:main"
        ],
    },
)
