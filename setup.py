from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='handtracking',
      version='1.0',
      description='Building a Real-time Hand-Detector using Neural Networks (SSD) on Tensorflow',
      url='https://github.com/victordibia/handtracking',
      author='Victor Dibia',
      license=license,
      install_requires=required
)
