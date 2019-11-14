#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x96B047156338B6D4 (psmith@gnu.org)
#
Name     : make
Version  : 4.2.1
Release  : 37
URL      : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz
Source0  : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz
Source1 : http://mirrors.kernel.org/gnu/make/make-4.2.1.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.0
Requires: make-bin = %{version}-%{release}
Requires: make-info = %{version}-%{release}
Requires: make-license = %{version}-%{release}
Requires: make-locales = %{version}-%{release}
Requires: make-man = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : guile
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: skip-tests-features-archive.patch
Patch2: 0002-Fix_tests.patch
Patch3: glob-Do-not-assume-glibc-glob-internals.patch
Patch4: configure.ac-Support-GLIBC-glob-interface-version-2.patch

%description
This directory contains the 4.2.1 release of GNU Make.
See the file NEWS for the user-visible changes from previous releases.
In addition, there have been bugs fixed.

%package bin
Summary: bin components for the make package.
Group: Binaries
Requires: make-license = %{version}-%{release}

%description bin
bin components for the make package.


%package dev
Summary: dev components for the make package.
Group: Development
Requires: make-bin = %{version}-%{release}
Provides: make-devel = %{version}-%{release}
Requires: make = %{version}-%{release}

%description dev
dev components for the make package.


%package info
Summary: info components for the make package.
Group: Default

%description info
info components for the make package.


%package license
Summary: license components for the make package.
Group: Default

%description license
license components for the make package.


%package locales
Summary: locales components for the make package.
Group: Default

%description locales
locales components for the make package.


%package man
Summary: man components for the make package.
Group: Default

%description man
man components for the make package.


%prep
%setup -q -n make-4.2.1
cd %{_builddir}/make-4.2.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573773996
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1573773996
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/make
cp %{_builddir}/make-4.2.1/COPYING %{buildroot}/usr/share/package-licenses/make/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/make-4.2.1/glob/COPYING.LIB %{buildroot}/usr/share/package-licenses/make/ec2350cf4fe9c4f97c3ee5c9046d0396672c365a
cp %{_builddir}/make-4.2.1/tests/COPYING %{buildroot}/usr/share/package-licenses/make/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
%find_lang make
## install_append content
ln -s make %{buildroot}/usr/bin/gmake
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gmake
/usr/bin/make

%files dev
%defattr(-,root,root,-)
/usr/include/gnumake.h

%files info
%defattr(0644,root,root,0755)
/usr/share/info/make.info
/usr/share/info/make.info-1
/usr/share/info/make.info-2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/make/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/make/ec2350cf4fe9c4f97c3ee5c9046d0396672c365a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/make.1

%files locales -f make.lang
%defattr(-,root,root,-)

