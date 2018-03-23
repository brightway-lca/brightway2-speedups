from setuptools import setup, Extension
# from Cython.Distutils import build_ext
import numpy as np

SRC_DIR = "bw2speedups"

kwargs = {
    "libraries": [],
    "include_dirs": [np.get_include()]
}

extension_1 = Extension(SRC_DIR + "._indexer",
                        # [SRC_DIR + "/_indexer.pyx"],
                        [SRC_DIR + "/_indexer.c"],
                        **kwargs)

extension_2 = Extension(SRC_DIR + "._find_first",
                        [SRC_DIR + "/_find_first.c"],
                        **kwargs)

extension_3 = Extension(SRC_DIR + "._consolidate",
                        [SRC_DIR + "/_consolidate.c"],
                        **kwargs)


if __name__ == "__main__":
    setup(
        # cmdclass = {'build_ext': build_ext},
        # install_requires=['numpy', 'cython'],
        author="Chris Mutel",
        author_email="cmutel@gmail.com",
        description="""Cython functions to speed up Brightway2 LCA calculations""",
        ext_modules = [extension_1, extension_2, extension_3],
        install_requires=['numpy'],
        name = 'bw2speedups',
        packages=[SRC_DIR],
        version="2.2.1",
        zip_safe=False,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
        ],
    )
