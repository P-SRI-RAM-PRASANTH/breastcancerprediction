from setuptools import setup, find_packages

setup(
    name='breastcancerprediction',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy==1.21.4',
        'streamlit==1.2.0',
        'protobuf>=3.20.0,<3.21.0',
        'streamlit-option-menu==0.3.2',
        'scikit-learn==1.0.2',
        'altair==4.2.0'
    ],
    entry_points={
        'console_scripts': [
            'run-app=app:main',  # assumes you have a `main()` function in app.py
        ],
    },
)
