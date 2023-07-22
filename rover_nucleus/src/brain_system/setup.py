from setuptools import setup

package_name = 'brain_system'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ian',
    maintainer_email='iangarcia@ciencias.unam.mx',
    description='TODO: Publisher de mensajes (enviara todos los comandos recibidos por Arduino, serán recibidos por el SUbscriber y procesados por los módulos anexos)',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
         'talker = brain_system.publisher_member_function:main',
         'listener = brain_system.subscriber_member_function:main',
        ],
    },
)
