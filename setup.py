from distutils.core import setup, Extension


setup(
    name                = 'pySUNXI',
    version             = '0.1.12',
    author              = 'Stefan Mavrodiev',
    author_email        = 'support@olimex.com',
    url                 = 'https://www.olimex.com/',
    license             = 'MIT',
    description         = 'Control GPIOs on SUNXI soc.',
    long_description    = open('README.txt').read() + open('CHANGES.txt').read(),
    classifiers         = [ 'Development Status :: 3 - Alpha',
                            'Environment :: Console',
                            'Intended Audience :: Developers',
                            'Intended Audience :: Education',
                            'License :: OSI Approved :: MIT License',
                            'Operating System :: POSIX :: Linux',
                            'Programming Language :: Python',
                            'Programming Language :: Python :: 3',
                            'Topic :: Home Automation',
                            'Topic :: Software Development :: Embedded Systems'
          ],
    ext_modules         = [Extension('SUNXI_GPIO', ['source/gpio_lib.c', 'source/pysunxi.c'])],
    package_dir={'': 'source'},
    packages=[''],
  
                            
)
