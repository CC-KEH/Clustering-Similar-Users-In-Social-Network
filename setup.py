import setuptools

__version__ = "0.0.1"

with open('README.md','r') as file:
    long_description = file.read()
    
AUTHOR_NAME = "CC-KEH"
AUTHOR_EMAIL = "example@example.com"
REPO_NAME = 'Social-Media-Community-Using-Optimized-Clustering-Algorithm'
SRC_REPO = "SNC"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    description='Social Media Community using KNN Algorithm',
    long_description=long_description,
    url=f"https/github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src')
)
