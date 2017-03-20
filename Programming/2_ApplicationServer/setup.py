from setuptools import setup

setup(
    name='ApplicationServer',
    version='1.0.0',
    author='Mattie432',
    author_email='matt@mattie432.com',
    description='',
    url='https://github.com/Mattie432/Blockchain-Voting-System',
    packages=[
        'applicationserver',
        'network',
        'user_ballot_registration',
        'website',
        'ethereum'
    ],
    install_requires=[
        'Django>=1.10.0',
        'psycopg2',
        'crochet',
        'pycrypto',
        'ecdsa',
        'pysha3',
        'web3'
    ]
)
