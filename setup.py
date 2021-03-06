import setuptools

setuptools.setup(name='crazy hamster',
                 version='0.1',
                 description='The craziest hamster in the world',
                 url='https://github.com/ehsangolshani/crazy-hamster',
                 author='Ehsan Golshani',
                 author_email='ehsanroman74@gmail.com',
                 license='GNU',
                 install_requires=[
                     'aiohttp',
                     'asyncio',
                 ],
                 packages=['crazy_hamster'],
                 zip_safe=False)
