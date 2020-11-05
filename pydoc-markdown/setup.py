# This file was auto-generated by Shut. DO NOT EDIT
# For more information about Shut, check out https://pypi.org/project/shut/

from __future__ import print_function
import io
import os
import setuptools
import sys

readme_file = 'README.md'
source_readme_file = '../README.md'
if not os.path.isfile(readme_file) and os.path.isfile(source_readme_file):
  import shutil; shutil.copyfile(source_readme_file, readme_file)
  import atexit; atexit.register(lambda: os.remove(readme_file))
if os.path.isfile(readme_file):
  with io.open(readme_file, encoding='utf8') as fp:
    long_description = fp.read()
else:
  print("warning: file \"{}\" does not exist.".format(readme_file), file=sys.stderr)
  long_description = None

requirements = [
  'click >=7.0.0,<8.0.0',
  'docspec >=0.2.0,<0.3.0',
  'docspec-python >=0.0.7,<0.1.0',
  'nr.collections >=0.0.1,<0.1.0',
  'nr.interface >=0.0.3,<0.1.0',
  'nr.databind.core >=0.0.18,<0.1.0',
  'nr.databind.json >=0.0.9,<0.1.0',
  'nr.fs >=1.6.0,<2.0.0',
  'requests >=2.23.0,<3.0.0',
  'PyYAML >=5.3.0,<6.0.0',
  'six >=1.11.0,<2.0.0',
  'toml >=0.10.1,<1.0.0',
  'watchdog >=0.10.2,<1.0.0',
]

setuptools.setup(
  name = 'pydoc-markdown',
  version = '3.7.0',
  author = 'Niklas Rosenstein',
  author_email = 'rosensteinniklas@gmail.com',
  description = 'Create Python API documentation in Markdown format.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/NiklasRosenstein/pydoc-markdown',
  license = 'MIT',
  packages = setuptools.find_packages('src', ['test', 'test.*', 'tests', 'tests.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = True,
  install_requires = requirements,
  extras_require = {},
  tests_require = [],
  python_requires = '>=3.5.0,<4.0.0',
  data_files = [],
  entry_points = {
    'console_scripts': [
      'pydoc-markdown = pydoc_markdown.main:cli',
    ],
    'pydoc_markdown.interfaces.Loader': [
      'python = pydoc_markdown.contrib.loaders.python:PythonLoader',
    ],
    'pydoc_markdown.interfaces.Processor': [
      'crossref = pydoc_markdown.contrib.processors.crossref:CrossrefProcessor',
      'filter = pydoc_markdown.contrib.processors.filter:FilterProcessor',
      'google = pydoc_markdown.contrib.processors.google:GoogleProcessor',
      'pydocmd = pydoc_markdown.contrib.processors.pydocmd:PydocmdProcessor',
      'smart = pydoc_markdown.contrib.processors.smart:SmartProcessor',
      'sphinx = pydoc_markdown.contrib.processors.sphinx:SphinxProcessor',
    ],
    'pydoc_markdown.interfaces.Renderer': [
      'hugo = pydoc_markdown.contrib.renderers.hugo:HugoRenderer',
      'markdown = pydoc_markdown.contrib.renderers.markdown:MarkdownRenderer',
      'mkdocs = pydoc_markdown.contrib.renderers.mkdocs:MkdocsRenderer',
      'docusaurus = pydoc_markdown.contrib.renderers.docusaurus:DocusaurusRenderer',
    ],
    'pydoc_markdown.interfaces.SourceLinker': [
      'git = pydoc_markdown.contrib.source_linkers.git:GitSourceLinker',
      'github = pydoc_markdown.contrib.source_linkers.git:GithubSourceLinker',
      'gitea = pydoc_markdown.contrib.source_linkers.git:GiteaSourceLinker',
    ]
  },
  cmdclass = {},
  keywords = ['documentation', 'docs', 'generator', 'markdown', 'pydoc'],
  classifiers = ['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Intended Audience :: End Users/Desktop', 'Topic :: Software Development :: Code Generators', 'Topic :: Utilities', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 2', 'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5'],
  zip_safe = True,
)
