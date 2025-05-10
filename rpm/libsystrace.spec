Name: libsystrace
Version: 0.0.0
Release: 1
Summary: A library for logging systrace data
License: BSD-3-Clause
URL: https://github.com/sailfishos/libsystrace
Source0: %{name}-%{version}.tar.bz2
BuildRequires: cmake
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
%summary

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DVERSION=%{version}
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE.md
%{_libdir}/libsystrace.so.*

%files devel
%{_libdir}/libsystrace.so
%{_libdir}/pkgconfig/systrace.pc
%{_includedir}/systrace.h
