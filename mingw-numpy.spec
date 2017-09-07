%{?mingw_package_header}

%global pkgname numpy

Name:          mingw-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       1.13.1
Release:       1%{?dist}
BuildArch:     noarch

# Everything is BSD except for class SafeEval in numpy/lib/utils.py which is Python
License:        BSD and Python
URL:            http://www.numpy.org/
Source0:        https://github.com/%{pkgname}/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz


BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python2
BuildRequires: mingw32-python2-Cython
BuildRequires: mingw32-python2-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-python2
BuildRequires: mingw64-python2-Cython
BuildRequires: mingw64-python2-setuptools


%description
MinGW Windows Python %{pkgname} library.


%package -n mingw32-python2-%{pkgname}
Summary:       MinGW Windows Python2 %{pkgname} library

%description -n mingw32-python2-%{pkgname}
MinGW Windows Python2 %{pkgname} library.


%package -n mingw64-python2-%{pkgname}
Summary:       MinGW Windows Python2 %{pkgname} library

%description -n mingw64-python2-%{pkgname}
MinGW Windows Python2 %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%{mingw32_python2} setup.py build -b build_mingw32
%{mingw64_python2} setup.py build -b build_mingw64


%install
ln -s build_mingw32 build
# --skip-build currently broken
%{mingw32_python2} setup.py install -O1 --root=%{buildroot}
rm build

ln -s build_mingw64 build
# --skip-build currently broken
%{mingw64_python2} setup.py install -O1 --root=%{buildroot}
rm build


%files -n mingw32-python2-%{pkgname}
%license LICENSE.txt
%{mingw32_bindir}/f2py2
%{mingw32_python2_sitearch}/*

%files -n mingw64-python2-%{pkgname}
%license LICENSE.txt
%{mingw64_bindir}/f2py2
%{mingw64_python2_sitearch}/*


%changelog
* Sat Sep 02 2017 Sandro Mani <manisandro@gmail.com> - 1.13.1-1
- Initial package
