%define	major 0
%define libname %mklibname oping %{major}
%define devname %mklibname oping -d

Summary:	Library to generate ICMP echo requests
Name:		liboping
Version:	1.6.2
Release:	6
License:	GPLv2+
Group:		System/Libraries
URL:		https://verplant.org/liboping/
Source0:	http://verplant.org/liboping/files/%{name}-%{version}.tar.gz
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(ncurses)

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

%package -n	%{devname}
Summary:	Development library and header files for the liboping library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	oping-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
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

%package perl
Group:          Networking/IRC
Summary:        %{name} perl plugin

%description perl
This package allow %{name} to use perl scripts

%prep
%setup -q
sed -i 's/-Werror//g' src/Makefile.*
sed -i 's|/usr/local||g' bindings/perl/Makefile.PL

%build
%configure2_5x \
	--disable-static

%make -C src
%make -C bindings perl/Makefile
cd bindings/perl
perl Makefile.PL INSTALLDIRS=vendor TOP_BUILDDIR=..
%make

%install
%makeinstall_std

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%files -n oping
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/oping
%{_bindir}/noping
%{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{devname}
%{_libdir}/*so
%{_includedir}/*.h
%{_mandir}/man3/*

%files perl
%{perl_vendorarch}/*

