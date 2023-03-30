from setuptools import setup, find_packages


setup(
    name='orchestra-ai',
    version='0.0.1',
    license='MIT',
    author="Jason Jin",
    author_email='jason@useorchestra.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/orchestraai/orchestra-sdk',
    keywords='orchestra python',
    install_requires=[
          'open-ai'
    ],
)
