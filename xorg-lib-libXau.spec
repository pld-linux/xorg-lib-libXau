Summary:	Xau - X authorization file management library
Summary(pl):	Xau - biblioteka zarządzająca plikami autoryzacji X
Name:		xorg-lib-libXau
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXau-%{version}.tar.bz2
# Source0-md5:	75a9f2b85cd1617b5ca98c9095323853
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.1.0
Obsoletes:	libXau
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xau is the X authorization file management library, conforming to X
Authorization Protocol.


%description -l pl
Xau to biblioteka zarządzająca plikami autoryzacji X zgodnie z
protokołem autoryzacji X.

%package devel
Summary:	Header files for libXau library
Summary(pl):	Pliki nagłówkowe biblioteki libXau
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xproto-devel
Obsoletes:	libXau-devel

%description devel
Header files for libXau library.

%description devel -l pl
Pliki nagłówkowe biblioteki libXau.

%package static
Summary:	Static libXau library
Summary(pl):	Biblioteka statyczna libXau
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXau-static

%description static
Static libXau library.

%description static -l pl
Biblioteka statyczna libXau.

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
