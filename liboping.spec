%define	major 0
%define libname %mklibname oping %{major}
%define develname %mklibname oping -d

Summary:	Library to generate ICMP echo requests
Name:		liboping
Version:	0.3.5
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Libraries
URL:		http://verplant.org/liboping/
Source0:	http://verplant.org/liboping/files/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
liboping is a C library to generate ICMP echo requests, better known as "ping
packets". It is intended for use in network monitoring applications or
applications that would otherwise need to fork ping(1) frequently. Included is
a sample application, called oping, which demonstrates the library's abilities.
It is like ping, ping6, and fping rolled into one. 

%package -n	%{libname}
Summary:	Library to generate ICMP echo requests
Group:          System/Libraries

%description -n	%{libname}
liboping is a C library to generate ICMP echo requests, better known as "ping
packets". It is intended for use in network monitoring applications or
applications that would otherwise need to fork ping(1) frequently. Included is
a sample application, called oping, which demonstrates the library's abilities.
It is like ping, ping6, and fping rolled into one. 

%package -n	%{develname}
Summary:	Static library and header files for the liboping library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	oping-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
liboping is a C library to generate ICMP echo requests, better known as "ping
packets". It is intended for use in network monitoring applications or
applications that would otherwise need to fork ping(1) frequently. Included is
a sample application, called oping, which demonstrates the library's abilities.
It is like ping, ping6, and fping rolled into one. 

This package contains header files for the liboping library.

%package -n	oping
Summary:	The oping utility demonstrates the liboping library's abilities
Group:		Networking/Other

%description -n	oping
The oping utility demonstrates the liboping library's abilities. It is like
ping, ping6, and fping rolled into one. 

%prep

%setup -q -n %{name}-%{version}

%build
rm -f configure
libtoolize --copy --force; aclocal; autoconf; automake --foreign --add-missing --copy

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n oping
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/oping
%attr(0644,root,root) %{_mandir}/man8/*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%attr(0755,root,root) %{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/*so
%attr(0644,root,root) %{_libdir}/*.a
%attr(0644,root,root) %{_libdir}/*.la
%attr(0644,root,root) %{_includedir}/*.h
%attr(0644,root,root) %{_mandir}/man3/*

