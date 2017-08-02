from setuptools import setup, find_packages
import os

setup(
    name="spark-jobserver-python",
    version=os.getenv("SJS_VERSION", "NO_ENV"),
    description=("The python modules required to "
                 "support PySpark jobs in Spark Job Server"),
    url="https://github.com/TimonSotiropoulos/spark-jobserver",
    license="Apache License 2.0",
    packages=find_packages(exclude=["test*", "example*"]),
    install_requires=["pyhocon", "py4j"]
)
