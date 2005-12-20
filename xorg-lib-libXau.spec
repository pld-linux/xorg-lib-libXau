Summary:	Xau - Authorization Protocol for X
Summary(pl):	Xau - protokó³ autoryzacji dla X
Name:		xorg-lib-libXau
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/lib/libXau-%{version}.tar.bz2
# Source0-md5:	aac9eef61542eb0c4db67274d8244714
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	libXau
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xau - Authorization Protocol for X.

%description -l pl
Xau - protokó³ autoryzacji dla X.

%package devel
Summary:	Header files for libXau library
Summary(pl):	Pliki nag³ówkowe biblioteki libXau
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xproto-devel
Obsoletes:	libXau-devel

%description devel
Xau - Authorization Protocol for X.

This package contains the header files needed to develop programs that
use libXau.

%description devel -l pl
Xau - protokó³ autoryzacji dla X.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXau.

%package static
Summary:	Static libXau library
Summary(pl):	Biblioteka statyczna libXau
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXau-static

%description static
Xau - Authorization Protocol for X.

This package contains the static libXau library.

%description static -l pl
Xau - protokó³ autoryzacji dla X.

Pakiet zawiera statyczn± bibliotekê libXau.

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXau.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXau.so
%{_libdir}/libXau.la
%{_includedir}/X11/Xauth.h
%{_pkgconfigdir}/xau.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXau.a
