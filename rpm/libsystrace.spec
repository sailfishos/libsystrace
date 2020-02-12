Name: libsystrace
Version: 0.0.0
Release: 1
Summary: A library for logging systrace data
License: BSD
URL: https://git.sailfishos.org/mer-core/libsystrace
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
mkdir -p build
pushd build
%cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DVERSION=%{version}
make %{?_smp_mflags}
popd build

%install
rm -rf %{buildroot}
make -C build install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/libsystrace.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libsystrace.so
%{_libdir}/pkgconfig/systrace.pc
%{_includedir}/systrace.h

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
