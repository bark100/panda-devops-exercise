from setuptools import setup

setup(
    name='Gify Panda',
    version='1.0',
    long_description=__doc__,
    packages=['gify-panda'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)

