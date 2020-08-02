from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["click==7.1.2", "joblib==0.16.0", "nltk==3.5", "regex==2020.7.14", "tqdm==4.48.0"]

setup(
    name="rdsl",
    version="0.0.1",
    author="Sasu Usen",
    author_email="osas.usen@gmail.com",
    description="A package for reusable data science codes",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/SpearSource/RDSL",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    scripts=['scripts/nltk_download.py'],
)
