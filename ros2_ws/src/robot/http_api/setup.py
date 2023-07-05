from setuptools import setup

package_name = 'http_api'
core_modules = 'http_api/core'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, core_modules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stephan',
    maintainer_email='ret7020@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'http_api = http_api.api:main'
        ],
    },
)
