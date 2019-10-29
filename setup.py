from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='grade',
    version='0.8.0',
    packages=['grade'],
    url='https://github.com/thoward27/grade',
    license='AGPL',
    author='Tom Howard',
    author_email='info@tomhoward.codes',
    description='A package for easy autograding.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
)
