from setuptools import setup

setup(
    name='unitconverter',
    version='0.1.0',
    entry_points={
        'console_scripts': ['unitconvert=unitconverter.CLI:run_cli'],
    },
    description='Command line tool for unit conversion',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    author='Dan Nixon',
    packages=['unitconverter', 'unitconverter.unit_tables'],
    include_package_data=True,
    zip_safe=False)
