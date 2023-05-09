%define major 0
%define oldlibpackage %mklibname inih 0
%define libpackage %mklibname inih
%define devpackage %mklibname -d inih
%define libreader %mklibname INIReader
%define devreader %mklibname -d INIReader

Name:     inih
Version:  56
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
%rename %{oldlibpackage}

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

%package -n %{libreader}
Summary:	This is a library for INIReader package provides simple INI file parser
Group:		System/Libraries

%description -n %{libreader}
This is a library for INIReader package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for

%package -n %{devreader}
Summary:  Development package for %{name} INIReader
Requires:	%{libpackage} = %{EVRD}

%description -n %{devreader}
This package contains development files for %{name} INIReader.

The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.

%prep
%autosetup -n %{name}-r%{version}
%meson -Ddefault_library=shared -Ddistro_install=true

%build
%meson_build

%install
%meson_install

%files -n %{libpackage}
%license LICENSE.txt
%doc README.md
%{_libdir}/libinih.so.%{major}

%files -n %{devpackage}
%{_includedir}/ini.h
%{_libdir}/pkgconfig/inih.pc
%{_libdir}/libinih.so

%files -n %{libreader}
%{_libdir}/libINIReader.so.%{major}

%files -n %{devreader}
%{_includedir}/INIReader.h
%{_libdir}/pkgconfig/INIReader.pc
%{_libdir}/libINIReader.so
