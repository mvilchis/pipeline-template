from setuptools import setup, find_packages

from os import path

"""
dummy-pipeline: Pipeline Dummy
"""

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.org'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="dummy",
    version='0.0.1',
    description='Pipeline Dummy',
    long_description=long_description,
    url='https://github.com/nanounanue/pipeline-template',
    author='Adolfo De Unánue',
    author_email='nanounanue@gmail.com',
    license='GPL v3',

    packages=find_packages(),

    test_suite='tests',

    install_requires=[
        'numpy',
        'pyyaml',
        'pandas',
        'scikit-learn',
        'sqlalchemy',
        'datetime',
        'scipy',
        'luigi',
        'Click',
        'python-dotenv'
    ],

    extra_require={
        'test': ['mock']
    },

    entry_points = {
        'console_scripts' : [
            'dummy = dummy.scripts.cli:main',

        ]
    },

    zip_safe=False
)
