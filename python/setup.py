import os
import compiler
import shutil
from distutils.core import Command
from distutils.command import build as build_module
from distutils.extension import Extension
from distutils.core import setup

rpcz_python_dir = os.path.abspath(os.path.dirname(__file__))

def _build_rpcz_proto():
    compiler.generate_proto(
        '../build/src/rpcz/proto/rpcz.proto',
        'rpcz'
    )

def _build_test_protos():
    compiler.generate_proto(
		'../test/proto/search.proto',
		'tests'
	)
    compiler.generate_proto(
		'../test/proto/search.proto',
		'tests',
		with_plugin='python_rpcz',
		suffix='_rpcz.py',
		plugin_binary='../build/src/rpcz/plugin/python/protoc-gen-python_rpcz'
	)


class Build(build_module.build):
    def run(self):
        _build_rpcz_proto()
        _build_test_protos()
        shutil.copy('compiler.py', 'rpcz')
        build_module.build.run(self)


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
    packages=[
		'rpcz',
		'tests'
	],
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
				'../include',
			    '../build/src',
				'/usr/local/include'
			],
			library_dirs=[
			    '../build/src/rpcz',
			    '/usr/local/lib'
			],
			language='c++'
		)
    ],
)
