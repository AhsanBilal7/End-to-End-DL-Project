import setuptools


with open("README.md", 'r' , encoding = 'utf-8') as file:
    long_drescription = file.read()

__version__ = "0.0.0"

AUTOHR_USER_NAME  = 'AhsanBilal7'
AUTOHR_EMAIL  = 'abilal.bee20seecs@seecs.edu.pk'
REPO_NAME  = 'AhsanBilal7'
SRC_REPO  = 'AhsanBilal7'

setuptools.setup(
    name = f"{SRC_REPO}",
    version = __version__,
    author = f"{AUTOHR_USER_NAME}",
    author_email = f"{AUTOHR_EMAIL}",
    description = "A template for End-to-End Deep learning projects",
    long_description = long_drescription,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTOHR_USER_NAME}/{SRC_REPO}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTOHR_USER_NAME}/{SRC_REPO}/issues"
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src")
)