from setuptools import setup

requires=[
    "requests>=2.7.0",
    "pyquery>=1.2.9"
]

setup(name='tal.amp',
      version='0.1.0',
      description='AMP for TAL',
      author='Sunil Abraham',
      license='MIT',
      install_requires=requires,
      packages=[
          'tal',
          'tal.amp'
      ],
      entry_points={
          'console_scripts': [
              "tal-amp = tal.amp.main:main"
          ]
      })
