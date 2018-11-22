import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hello-nico",
    version="0.0.2",
    author="Nico",
    author_email="github@gerardnico.com",
    description="A small hello world package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gerardnico/python/hello_world_pkg/README.md",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)