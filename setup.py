import setuptools

setuptools.setup(
	name="gu",
	version="0.0.1",
	author="Example Author",
	author_email="author@example.com",
	description="A small example package",
	scripts=['./scripts/gu'],
	packages=setuptools.find_packages(),
	python_requires='>=3.6',
)
