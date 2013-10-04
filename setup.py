from distutils.core import setup

setup(
    name='EStruct',
    version='0.1.0',
    author='Simon Black',
    author_email='simon.black.bug@gmail.com',
    packages=['estruct','estruct.tests'],
    scripts=['bin/example.py'],
    url='http://pypi.python.org/pypi/EStruct/',
    license='LICENSE.txt',
    description="Python package to extend the capabilities of the standard library's Struct package.",
    long_description=open('README.txt').read(),
    install_requires=[],
)