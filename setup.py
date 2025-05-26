from setuptools import setup, find_packages

setup(
    name='purr',
    version='0.1.0',
    description='A simple mouse event tracker(warning: this is a gag tool — use it in purrduction at your own risk)',
    author='Nabbo Noushad Darad',
    author_email='nabbonoushad@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pynput',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
