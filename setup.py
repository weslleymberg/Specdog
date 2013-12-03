from setuptools import setup, find_packages

setup(name = "specdog",
      version = "1.1.0",
      description = "Simple tool to automate test routines execution",
      author = "Weslleymberg Lisboa",
      author_email = "weslleym.lisboa@gmail.com",
      url = "http://github.com/weslleymberg/Specdog",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=["pyinotify",],
      entry_points="""
      [console_scripts]
      specdog = specdog:main
      """,
     )
