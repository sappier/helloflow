from setuptools import setup

setup(
    name='helloflow',
    version='0.1.0',
    description='The Metaflow helloworld flow example as a python package',
    url='https://github.com/sappier/helloflow',
    license='Apache License 2.0',
    author='Roman Kindruk',
    author_email='roman.kindruk@sap.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
    ],
    install_requires=[
        'metaflow',
    ],
    packages=['helloflow']
)
