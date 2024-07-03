from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="disnet",
    version="0.1.0",
    author="Austin Starnes",
    author_email="austin@worthify.ai",
    description="Depth estimation network definitions, pip installable for easy use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Worthify-AI/DIS",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your dependencies here
    ],
)
