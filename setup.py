from setuptools import setup
setup(
    name = 'asset_manager',
    version = '0.1.0',
    packages = [
        'am_gui',
        'am_utils'
        ],
    install_requires=['Pillow'],
    entry_points = {
        'gui_scripts': [
            'am_gui = am_gui.main:main'
        ]
    })
