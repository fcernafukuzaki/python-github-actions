import sys


def test_python_version():
    version = f'{sys.version_info.major}.{sys.version_info.minor}'
    print(f'Versión de Python: {version}')

    assert version >= "3.9", 'Se está usando una versión inferior a Python 3.9.'
