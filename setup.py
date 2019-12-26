import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "example-pkg-gautsi".
    version = "0.0.1",
    author = "Gautam Sisodia",
    packages = setuptools.find_packages(),
    classifiers = [
        "Progamming Language :: Python :: 3",
    ],
)
