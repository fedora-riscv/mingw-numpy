%{?mingw_package_header}

%global pkgname numpy

Name:          mingw-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       1.15.0
Release:       1%{?dist}
BuildArch:     noarch

# Everything is BSD except for class SafeEval in numpy/lib/utils.py which is Python
License:       BSD and Python
URL:           http://www.numpy.org/
Source0:       https://github.com/%{pkgname}/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz


BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python2
BuildRequires: mingw32-python2-Cython
BuildRequires: mingw32-python2-setuptools

BuildRequires: mingw64-filesystem >= 102
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

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-python2-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-python2-%{pkgname}.debugfiles


%files -n mingw32-python2-%{pkgname} -f mingw32-python2-%{pkgname}.debugfiles
%license LICENSE.txt
%{mingw32_bindir}/f2py2
%{mingw32_bindir}/f2py
%{mingw32_bindir}/conv-template
%{mingw32_bindir}/from-template
%{mingw32_python2_sitearch}/*

%files -n mingw64-python2-%{pkgname} -f mingw64-python2-%{pkgname}.debugfiles
%license LICENSE.txt
%{mingw64_bindir}/f2py2
%{mingw64_bindir}/f2py
%{mingw64_bindir}/conv-template
%{mingw64_bindir}/from-template
%{mingw64_python2_sitearch}/*


%changelog
* Thu Aug 02 2018 Sandro Mani <manisandro@gmail.com> - 1.15.0-1
- Update to 1.15.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Sandro Mani <manisandro@gmail.com> - 1.14.5-1
- Update to 1.14.5

* Wed May 02 2018 Sandro Mani <manisandro@gmail.com> - 1.14.3-1
- Update to 1.14.3

* Tue Mar 13 2018 Sandro Mani <manisandro@gmail.com> - 1.14.2-1
- Update to 1.14.2

* Thu Feb 22 2018 Sandro Mani <manisandro@gmail.com> - 1.14.1-1
- Update to 1.14.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 1.13.3-1
- Update to 1.13.3

* Fri Sep 29 2017 Sandro Mani <manisandro@gmail.com> - 1.13.2-1
- Update to 1.13.2

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 1.13.1-2
- Rebuild for mingw-filesystem

* Sat Sep 02 2017 Sandro Mani <manisandro@gmail.com> - 1.13.1-1
- Initial package
