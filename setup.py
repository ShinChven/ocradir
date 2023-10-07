from setuptools import setup, find_packages

setup(
    name='ocradir',
    version='0.1',
    description='OCR tool to convert images in a directory to markdown files.',
    author='ShinChven',
    author_email='shinchven@gmail.com',
    url='https://github.com/ShinChven/ocradir.git',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'pytesseract'
    ],
    entry_points={
        'console_scripts': [
            'ocradir=ocradir.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
