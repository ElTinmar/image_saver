from distutils.core import setup

setup(
    name='image_saver',
    author='Martin Privat',
    version='0.1.0',
    packages=['image_saver','image_saver.tests'],
    license='MIT',
    description='write images to raw files, image files or videos',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy", 
        "opencv-python",
    ]
)