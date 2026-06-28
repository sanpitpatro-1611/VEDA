from setuptools import setup

setup(
    name="veda",
    version="1.0.0a1",
    description="VEDA Programming Language",
    author="Sanpit Patro",

    py_modules=[
        "main",
        "compiler"
    ],

    entry_points={
        "console_scripts": [
            "veda=main:main",
        ]
    },
)