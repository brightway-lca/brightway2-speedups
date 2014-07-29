from setuptools import setup, Extension
# from Cython.Distutils import build_ext
import numpy as np

SRC_DIR = "bw2speedups"

extension_1 = Extension(SRC_DIR + "._indexer",
                        # [SRC_DIR + "/_indexer.pyx"],
                        [SRC_DIR + "/_indexer.c"],
                        libraries=[],
                        include_dirs=[np.get_include()])


if __name__ == "__main__":
    setup(
        author="Chris Mutel",
        author_email="cmutel@gmail.com",
        # cmdclass = {'build_ext': build_ext},
        description="""Cython functions to speed up Brightway2 LCA calculations""",
        ext_modules = [extension_1],
        # install_requires=['numpy', 'cython'],
        install_requires=['numpy'],
        name = 'bw2speedups',
        packages=[SRC_DIR],
        version="1.0",
        zip_safe=False,
    )
