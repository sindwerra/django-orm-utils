import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="django-orm-utils",
    version='0.0.1',
    author='sindwerra',
    author_email='sindwerra@hotmail.com',
    description='django orm related utils',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/sindwerra/django_orm_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)