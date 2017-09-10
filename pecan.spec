#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pecan
Version  : 1.2.1
Release  : 36
URL      : http://pypi.debian.net/pecan/pecan-1.2.1.tar.gz
Source0  : http://pypi.debian.net/pecan/pecan-1.2.1.tar.gz
Summary  : A WSGI object-dispatching web framework, designed to be lean and fast, with few dependencies.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pecan-bin
Requires: pecan-legacypython
Requires: pecan-python
Requires: Mako
Requires: WebOb
Requires: WebTest
Requires: logutils
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Pecan
=====
A WSGI object-dispatching web framework, designed to be lean and fast with few
dependencies.

%package bin
Summary: bin components for the pecan package.
Group: Binaries

%description bin
bin components for the pecan package.


%package legacypython
Summary: legacypython components for the pecan package.
Group: Default

%description legacypython
legacypython components for the pecan package.


%package python
Summary: python components for the pecan package.
Group: Default
Requires: pecan-legacypython

%description python
python components for the pecan package.


%prep
%setup -q -n pecan-1.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505055412
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505055412
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gunicorn_pecan
/usr/bin/pecan

%files legacypython
%defattr(-,root,root,-)
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/__init__.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/__init__.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/app.py_tmpl
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/controllers/__init__.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/controllers/__init__.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/controllers/root.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/controllers/root.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/model/__init__.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/model/__init__.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/templates/error.html
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/templates/index.html
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/templates/layout.html
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests/__init__.py_tmpl
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests/config.py_tmpl
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests/test_functional.py_tmpl
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests/test_units.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests/test_units.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/__init__.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/__init__.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/app.py_tmpl
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/controllers/__init__.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/controllers/__init__.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/controllers/root.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/controllers/root.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/errors.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/errors.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/model/__init__.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/model/__init__.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests/__init__.py_tmpl
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests/config.py_tmpl
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests/test_functional.py_tmpl
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests/test_units.py
%exclude /usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests/test_units.pyc
%exclude /usr/lib/python2.7/site-packages/pecan/tests/scaffold_fixtures/file_sub/bar_+package+/spam.txt
%exclude /usr/lib/python2.7/site-packages/pecan/tests/scaffold_fixtures/file_sub/foo_+package+
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
