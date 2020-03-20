from setuptools import setup, find_packages

dependencies = [
    "aiter",            # Used for async generator tools
    "blspy",            # Signature library
    "cbor2",            # Used for network wire format
    "pyyaml",           # Used for config file format
    "miniupnpc",        # Allows users to open ports on their router
    "aiosqlite",        # asyncio wrapper for sqlite, to store blocks
    "aiohttp",          # HTTP server for full node rpc
    "colorlog"          # Adds color to logs
]

dev_dependencies = [
    "pytest",
    "flake8",
    "mypy",
    "isort",
    "autoflake",
    "black",
    "pytest-asyncio"
]

packages = ["lib.chiavdf.inkfish"] + find_packages(exclude=["lib", "lib.*"])

setup(
    name="chiablockchain",
    author="Mariano Sorgente",
    author_email="mariano@chia.net",
    description="Chia proof of space plotting, proving, and verifying (wraps C++)",
    license="Apache License",
    python_requires=">=3.7, <4",
    packages=packages,
    keywords="chia blockchain node",
    install_requires=dependencies,
    dev_requires=dev_dependencies,
    setup_requires=["setuptools_scm"],
    extras_require={
        'uvloop': ["uvloop"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    zip_safe=False,
)
