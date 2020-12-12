Name:     inih
Version:  52
Release:  1
Summary:  Simple INI file parser library

License:  BSD
URL:      https://github.com/benhoyt/inih
Source0:  https://github.com/benhoyt/inih/archive/r%{version}/%{name}-r%{version}.tar.gz

BuildRequires: meson


%description
The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.


%package devel
Summary:  Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
This package contains development files for %{name}.

The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.


%prep
%autosetup -n %{name}-r%{version}


%build
%meson -Ddefault_library=shared -Ddistro_install=true
%meson_build


%install
%meson_install


%files
%license LICENSE.txt
%doc README.md
#{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.0


%files devel
%{_includedir}/ini.h
%{_libdir}/pkgconfig/inih.pc
%{_libdir}/lib%{name}.so
