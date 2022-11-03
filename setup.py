from setuptools import setup, find_packages


setup(
    name="patterns",
    version="0.1.0",
    description="Reusable HTML widgets for building web apps in pure Python",
    author="Pipal Academy",
    install_requires=[
        "Jinja2>=3.1.0",
    ],
    url="https://github.com/pipalacademy/patterns",
    packages=["patterns"]
)
