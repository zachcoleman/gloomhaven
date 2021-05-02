
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gloomhaven-zachcoleman",
    version="0.0.1",
    author="Zachary Coleman",
    author_email="zacharywcoleman@gmail.com",
    description="A small package for running Gloomhaven attack modifier deck simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zachcoleman/gloomhaven",
    project_urls={
        "Bug Tracker": "https://github.com/zachcoleman/gloomhaven/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["gloomhaven"],
    python_requires=">=3.9",
)

