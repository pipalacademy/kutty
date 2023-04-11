from setuptools import setup, find_packages


setup(
    name="kutty",
    version="0.1.0",
    description="Reusable HTML widgets for building web apps in pure Python",
    author="Pipal Academy",
    install_requires=["pygments", "markdown>=3.4.3"],
    url="https://github.com/pipalacademy/kutty",
    packages=find_packages()
)
