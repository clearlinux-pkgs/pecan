#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pecan
Version  : 1.3.2
Release  : 45
URL      : http://pypi.debian.net/pecan/pecan-1.3.2.tar.gz
Source0  : http://pypi.debian.net/pecan/pecan-1.3.2.tar.gz
Summary  : A WSGI object-dispatching web framework, designed to be lean and fast, with few dependencies.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pecan-bin
Requires: pecan-python3
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


%package python
Summary: python components for the pecan package.
Group: Default
Requires: pecan-python3

%description python
python components for the pecan package.


%package python3
Summary: python3 components for the pecan package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pecan package.


%prep
%setup -q -n pecan-1.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523556845
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gunicorn_pecan
/usr/bin/pecan

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
