from setuptools import setup

setup(
    name="invoicing-pdf",
    packages=["invoicing"],
    version="1.0.0",
    license="MIT",
    description="This package can be used to convert Excel invoices to PDF",
    author="Raji",
    author_email="",
    url="",
    keywords=["invoices", "excel", "pdf"],
    install_requires=["fpdf", "pandas", "openpyxl"],
    classifiers=["Development Status :: 3 - Alpha",
                 "intended Audience :: Developers",
                 "Topic :: Software Development :: Build Tools",
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python :: 3.8",
                 "Programming Language :: Python :: 3.9",
                 "Programming Language :: Python :: 3.10",
                 "Programming Language :: Python :: 3.11",
                 ],
)


