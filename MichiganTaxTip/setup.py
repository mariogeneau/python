from setuptools import setup

APP = ['MichiganTaxTip/MichiganTaxTip.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['PIL']
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)