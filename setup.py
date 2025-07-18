import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
    

__version__ = "0.0.0"
REPO_NAME="mlops_project_wines"
SRC_REPO="mlproject"
AUTHOR_USER_NAME="siva"
AUTHOR_EMAIL="msivakumarredd878@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    long_description=long_description,
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)