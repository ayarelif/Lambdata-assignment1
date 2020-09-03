# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Lambdata-assignment1", # the name that you will install via pip
    version="0.0.1",
    author="Elif Ayar",
    author_email="eayar2020@gmail.com",
    description="Collection of Data Science assignment first",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/ayarelif/Lambdata-assignment1",
    #keywords="",
    packages=find_packages(), # ["my_lambdata"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)