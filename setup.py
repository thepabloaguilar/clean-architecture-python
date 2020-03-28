from setuptools import find_packages


with open(join(dirname(__file__), "README.md")) as _file:
    long_description = _file.read()


setup(
    name="clean-architecture-example",
    version="0.0.1",
    author="Pablo Aguilar",
    description="Clean Architecture Example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "aniso8601==8.0.0",
        "click==7.1.1",
        "dataclasses-json==0.4.2",
        "flask==1.1.1",
        "flask-restful==0.3.8",
        "itsdangerous==1.1.0",
        "jinja2==2.11.1",
        "markupsafe==1.1.1",
        "marshmallow==3.5.1",
        "marshmallow-enum==1.5.1",
        "mypy-extensions==0.4.3",
        "punq==0.4.1",
        "pytz==2019.3",
        "six==1.14.0",
        "sqlalchemy==1.3.15",
        "stringcase==1.2.0",
        "typing-extensions==3.7.4.1",
        "typing-inspect==0.5.0",
        "werkzeug==1.0.0",
    ],
    python_requires=">=3.7",
)
