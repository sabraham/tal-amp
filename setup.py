from setuptools import setup

setup(name='tal.amp',
      version='0.1.0',
      description='AMP for TAL',
      author='Sunil Abraham',
      license='MIT',
      packages=[
          'tal',
          'tal.amp'
      ],
      entry_points={
          'console_scripts': [
              "tal-amp = tal.amp.main:main"
          ]
      })
