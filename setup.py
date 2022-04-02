from setuptools import setup,find_packages
from pathlib import Path

root_dir = Path(__file__).parent.resolve()
with open(root_dir / 'README.md', mode='r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="mbinobs",
    description="Mix bin obfuscator",
    version='1.2',
    author='Manuel',
    author_email='manumathias2012@gmail.com',
    url='https://github.com/ManuelMaM/mbin-obs'
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    keywords = ['obfuscation','obfuscator','ipfuscation']
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License', 
    ],
    entry_points = {
        "console_scripts": [
            "mbinobs = mbinobs.__main__:main",
        ]
    }
)