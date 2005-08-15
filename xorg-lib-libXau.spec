
#
Summary:	Xau - Authorization Protocol for X
Summary(pl):	Xau - protok� autoryzacji dla X
Name:		xorg-lib-libXau
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXau-%{version}.tar.bz2
# Source0-md5:	1c5c9779d78f45267cae2e6cc1856517
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/libXau-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xau - Authorization Protocol for X.

%description -l pl
Xau - protok� autoryzacji dla X.


%package devel
Summary:	Header files libXau development
Summary(pl):	Pliki nag��wkowe do biblioteki libXau
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXau = %{version}-%{release}
Requires:	xorg-proto-xproto-devel

%description devel
Xau - Authorization Protocol for X.

This package contains the header files needed to develop programs that
use these libXau.

%description devel -l pl
Xau - protok� autoryzacji dla X.

Pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania program�w
u�ywaj�cych biblioteki libXau.


%package static
Summary:	Static libXau libraries
Summary(pl):	Biblioteki statyczne libXau
Group:		Development/Libraries
Requires:	xorg-lib-libXau-devel = %{version}-%{release}

%description static
Xau - Authorization Protocol for X.

This package contains the static libXau library.

%description static -l pl
Xau - protok� autoryzacji dla X.

Pakiet zawiera statyczne biblioteki libXau.


%prep
%setup -q -n libXau-%{version}


%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,wheel) %{_libdir}/libXau.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.la
%attr(755,root,wheel) %{_libdir}/libXau.so
%{_pkgconfigdir}/xau.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXau.a