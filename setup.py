from setuptools import setup, find_packages

setup(
        name='10fifteen.recipe.distutils',
        author='Simon Inglis',
        author_email='info@10fifteen.com',
        description="Recipe for zc.buildout that downloads one or multiple distutils-archives and installs them",
        version='0.1',
        packages=find_packages(),
        entry_points={'zc.buildout': 
            ['default = 10fifteen.recipe.distutils:Recipe']},
        install_requires=['setuptools', 'zc.buildout'],
        namespace_packages=['10fifteen'],
        zip_safe=True,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Plugins',
            'Framework :: Buildout',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: System :: Installation/Setup',
            'License :: OSI Approved :: BSD License',
        ],
        )
