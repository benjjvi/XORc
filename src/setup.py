import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

print(find_packages())

# This call to setup() does all the work
setup(
    name="XORc",
    version="1.0.8",
    description="XORc is a simple python package to provide simple XOR encryption using XOR algorithms.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bildsben/xorc",
    author="bildsben",
    author_email="ben.voisey2@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "xorc=xorc.__main__:main",
        ]
    },
)