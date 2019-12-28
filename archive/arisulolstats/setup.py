from setuptools import setup

setup(name='arisulolstats',
      version='1.1',
      description="Show League of Legends' stats",
      url='https://github.com/IceArrow256/arisulolstats',
      author='IceArrow256',
      author_email='icearrow256@gmail.com',
      license='MIT',
      packages=['arisulolstats'],
      zip_safe=False,
      install_requires=['PyQt5', 'ia256utilities', 'riotwatcher'],
      entry_points = {'arisulolstats': ['arisulolstats=arisulolstats:main']}
      )
