from setuptools import setup, find_packages


setup(
    name='fbxosctrl',
    version='0.1.6',
    # packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={'fbxosctrl': ['py.typed']},
    install_requires=[
        'requests',
        'dicttoxml',
        'xmltodict',
        'zeroconf',
    ],
    url='https://github.com/afer92/fbxosctrl',
    license='LGPL-3.0 ',
    author='Alain Ferraro',
    description='API For freebox os',
    packages=['fbxostools'],
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
    ],
    python_requires='>=3.4',
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'pylint',
        'tox',
        'pytest-cov'
    ]

)
