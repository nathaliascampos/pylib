from setuptools import setup

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

# with open('requirements.txt') as f:
#     required = f.read().splitlines()

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='pylib',
    url='https://github.com/nathaliascampos/py-lib',
    author='Nathalia Campos',
    author_email='campossnathalia@gmail.com',
    # Needed to actually package something
    packages=['pylib'],
    # Needed for dependencies
    # install_requires=['numpy'],
    # install_requires=required,
    # *strongly* suggested for sharing
    version='0.0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
