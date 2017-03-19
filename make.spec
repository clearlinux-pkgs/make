#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : make
Version  : 4.2.1
Release  : 21
URL      : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz
Source0  : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 GPL-3.0+ LGPL-2.0
Requires: make-bin
Requires: make-doc
Requires: make-locales
BuildRequires : guile
Patch1: skip-tests-features-archive.patch

%description
This directory contains the 4.2.1 release of GNU Make.
See the file NEWS for the user-visible changes from previous releases.
In addition, there have been bugs fixed.

%package bin
Summary: bin components for the make package.
Group: Binaries

%description bin
bin components for the make package.


%package dev
Summary: dev components for the make package.
Group: Development
Requires: make-bin
Provides: make-devel

%description dev
dev components for the make package.


%package doc
Summary: doc components for the make package.
Group: Documentation

%description doc
doc components for the make package.


%package locales
Summary: locales components for the make package.
Group: Default

%description locales
locales components for the make package.


%prep
%setup -q -n make-4.2.1
%patch1 -p1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang make

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/make

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files locales -f make.lang 
%defattr(-,root,root,-)

