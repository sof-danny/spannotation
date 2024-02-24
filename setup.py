from setuptools import setup, find_packages

setup(
    name='spannotation',
    version='0.1.15',
    author='Samuel O. Folorunsho',
    author_email='folorunshosamuel001@gmail.com',
    description="This Python package offers a simple yet powerful tool for image segmentation, particularly useful for navigation and path detection tasks in various environments. Utilizing minimal user input, it allows for the efficient segmentation of images into 'drivable' and 'non-drivable' regions, making it an ideal solution for a range of applications from agriculture to autonomous navigation.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sof-danny/spannotation',
    packages=find_packages(),
    install_requires=[
        'opencv-python', 'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

