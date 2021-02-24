import setuptools

setuptools.setup(
    name="mafk",
    version="0.0.1",
    author="Rull Deef",
    author_email="deeroll666@gmail.com",
    license="MIT",
    description="simple C-project handler",
    long_description=open("README.md", "rt").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RullDeef/mafk",
    packages=setuptools.find_packages(),
    scripts=["bin/mafk"]
)
