import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='tb-mqtt-client',
    version='1.0.0',
    description='ThingsBoard MQTT client Python SDK',
    author='ThingBoard',
    author_email='info@thingsboard.io',
    long_description=long_description,     
    url='git+https://https://github.com/howlab/thingsboard-python-client-sdk',
    keywords = ['MQTT'],  
    packages=setuptools.find_packages(exclude=("examples",)),
    setup_requires=['wheel'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],      
    install_requires=[
        'paho-mqtt>=1.3.0',
        'jsonschema',
    ]      
)
