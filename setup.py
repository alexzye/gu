import setuptools

setuptools.setup(
	name="gu",
	version="0.0.1",
	author="Alex Ye",
	author_email="alex@example.com",
	description="git user switcher",
	scripts=['./scripts/gu'],
	packages=setuptools.find_packages(),
	python_requires='>=3.6',
)
