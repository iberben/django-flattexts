from setuptools import setup, find_packages
import flattexts


setup(
    name="django-flattexts",
    version=flattexts.__version__,
    url='https://github.com/citylive/django-flattexts/',
    license='BSD',
    description='Django flattexts',
    long_description=open('README.rst', 'r').read(),
    author='City Live nv',
    packages=find_packages('.'),
    #package_dir={
    #    '': [
    #        'templates/*',
    #        'templates/*/*',
    #    ],
    #},
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)

