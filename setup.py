from setuptools import setup, find_packages

import os
print(os.getcwd())
with open("requirements.txt", "r") as f:
#with open("requires.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name='llm_bhasa',
    version='0.5',
    packages=find_packages(),
    install_requires=requirements,
    author="Pankaj Rawat",
    author_email="pankajr141@gmail.com",
    description='LLM trainer',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/pankajr141/llm_bhasa", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
