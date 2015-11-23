from setuptools import setup, find_packages
import flattexts


setup(
    name="django-flattexts",
    version=flattexts.__version__,
    url='https://github.com/vikingco/django-flattexts/',
    license='BSD',
    description='Django flattexts',
    long_description=open('README.rst', 'r').read(),
    author='City Live nv',
    packages=find_packages('.'),
    install_requires=['django-parler==1.4', 'django-summernote==0.5.15'],
    # package_dir={
    #    '': [
    #        'templates/*',
    #        'templates/*/*',
    #    ],
    # },
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
