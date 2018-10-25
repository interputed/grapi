import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grapi",
    version="0.1.4",
    author="Andrew Craighead",
    author_email="craigheadap@missouri.edu",
    description="Python 3 bindings for Graylog's REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/interputed/grapi",
    packages=setuptools.find_packages(),
    keywords=["graylog", "graylog-api", "graylog api", "python3 graylog", "python3 graylog api", "python3 graylog-api"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
)
