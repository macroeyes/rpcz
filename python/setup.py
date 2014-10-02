import os
import sys
import shutil
from setuptools.command import build_ext
from compiler import generate_proto
from setuptools import setup, Command, Extension

# setuptools DWIM monkey-patch madness
# http://mail.python.org/pipermail/distutils-sig/2007-September/thread.html#8204
if 'setuptools.extension' in sys.modules:
    m = sys.modules['setuptools.extension']
    m.Extension.__dict__ = m._Extension.__dict__

def _build_rpcz_proto():
    generate_proto(
        '../build/src/rpcz/proto/rpcz.proto',
        'rpcz'
    )

def _build_test_protos():
    generate_proto(
		'../test/proto/search.proto',
		'tests'
	)
    generate_proto(
		'../test/proto/search.proto',
		'tests',
		with_plugin='python_rpcz',
		suffix='_rpcz.py',
		plugin_binary='../build/src/rpcz/plugin/python/protoc-gen-python_rpcz'
	)


class Build(build_ext.build_ext):
    def run(self):
        _build_rpcz_proto()
        _build_test_protos()
        shutil.copy('py', 'rpcz')
        build_ext.build_ext.run(self)


class GenPyext(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        if os.system('cython --cplus cython/pywraprpcz.pyx') != 0:
            raise IOError("Running cython failed.")


setup(
    name="rpcz",
    version="0.9.1",
    author="Nadav Samet",
    author_email="nadavs@google.com",
    description="An RPC implementation for Protocol Buffer based on ZeroMQ",
    license="Apache 2.0",
    keywords="protocol-buffers rpc zeromq 0mq",
    packages=['rpcz', 'tests'],
	setup_requires=['setuptools_cython'],
    url='http://github.com/macroeyes/rpcz',
    long_description='',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
    ],
    cmdclass={
        'Build': Build,
        'GenPyext': GenPyext,
    },
    ext_modules=[
        Extension(
			'rpcz.pywraprpcz',
			['cython/pywraprpcz.cpp'],
			libraries=['rpcz'],
			include_dirs=[
				'./../include',
			    './../build/src',
				'/usr/local/include'
			],
			library_dirs=[
			    '/usr/local/lib'
			],
			language='c++'
		)
    ],
)
