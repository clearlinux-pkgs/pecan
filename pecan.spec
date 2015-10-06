#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pecan
Version  : 1.0.2
Release  : 17
URL      : https://pypi.python.org/packages/source/p/pecan/pecan-1.0.2.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pecan/pecan-1.0.2.tar.gz
Summary  : A WSGI object-dispatching web framework, designed to be lean and fast, with few dependencies.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pecan-bin
Requires: pecan-python
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


%package python
Summary: python components for the pecan package.
Group: Default

%description python
python components for the pecan package.


%prep
%setup -q -n pecan-1.0.2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gunicorn_pecan
/usr/bin/pecan

%files python
%defattr(-,root,root,-)
%exclude /usr/lib/python2.7/site-packages/pecan/tests/scaffold_fixtures/file_sub/bar_+package+/spam.txt
%exclude /usr/lib/python2.7/site-packages/pecan/tests/scaffold_fixtures/file_sub/foo_+package+
%exclude /usr/lib/python3.4/site-packages/pecan/tests/scaffold_fixtures/file_sub/bar_+package+/spam.txt
%exclude /usr/lib/python3.4/site-packages/pecan/tests/scaffold_fixtures/file_sub/foo_+package+
/usr/lib/python*/*
