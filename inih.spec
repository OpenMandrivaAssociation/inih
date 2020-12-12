%define major 0
%define libpackage %mklibname inih %{major}
%define devpackage %mklibname -d inih

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

%package -n %{libpackage}
Summary:	This is a library for inih package provides simple INI file parser
Group:		System/Libraries

%description -n %{libpackage}
This is a library for inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for


%package -n %{devpackage}
Summary:  Development package for %{name}
Requires:	%{libpackage} = %{EVRD}


%description -n %{devpackage}
This package contains development files for %{name}.

The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.


%prep
%autosetup -n %{name}-r%{version}


%build
%meson -Ddistro_install=true
%meson_build


%install
%meson_install


%files -n %{libpackage}
%license LICENSE.txt
%doc README.md
#{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.%{major}

%files -n %{devpackage}
%{_includedir}/ini.h
%{_libdir}/pkgconfig/inih.pc
%{_libdir}/lib%{name}.so
