from setuptools import setup, find_packages

setup(
    name="starexx",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "starexx=starexx.cli:main",
        ],
    },
    author="Starexx",
    description="Automatic dependency installer for Python scripts.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/starexxx/starexx-pip",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
