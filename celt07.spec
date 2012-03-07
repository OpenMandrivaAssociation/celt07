%define major 0
%define libname %mklibname celt0_ %major
%define develname %mklibname -d celt0_0.7

Summary:	Older version of the CELT ultra-low delay audio codec
Name:		celt07
Version:	0.7.1
Release:	1
Source0:	http://downloads.us.xiph.org/releases/celt/%{name}-%{version}.tar.gz
License:	BSD
Group:		Sound
Url:		http://www.celt-codec.org/
BuildRequires:	libogg-devel

%description
This is an older version of the CELT ultra-low delay audio codec,
using a bitstream format different from the current version.

Since the older version is still in common use and newer versions
can't play back or convert streams created with the older version,
this version should be available for some time.

%package -n	%{libname}
Summary:	Ultra-low delay audio codec - shared library
Group:		System/Libraries

%description -n	%{libname}
This is an older version of the CELT ultra-low delay audio codec,
using a bitstream format different from the current version.

Since the older version is still in common use and newer versions
can't play back or convert streams created with the older version,
this version should be available for some time.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

# Remove stuff that would conflict with the newer, default celt
rm -rf %buildroot%_includedir \
	%buildroot%_libdir/*.a \
	%buildroot%_libdir/*.so \
	%buildroot%_libdir/pkgconfig \
	%buildroot%_bindir

%check
make check

%files -n %{libname}
%doc README COPYING
%{_libdir}/libcelt0.so.%{major}*
