from setuptools import setup

setup(name = "specdog",
      version = "0.0.1",
      description = "Simple tool to aumomate test routines execution",
      author = "Weslleymberg Lisboa",
      author_email = "weslleym.lisboa@gmail.com",
      url = "",
      packages=["specdog",],
      include_package_data=True,
      zip_safe=False,
      install_requires=["pyinotify",],
      entry_points="""
            [console_scripts]
            specdog = specdog:main
            """,
     )
