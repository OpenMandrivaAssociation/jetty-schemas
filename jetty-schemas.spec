%{?_javapackages_macros:%_javapackages_macros}

%global     addver M0
%global     toolchain_id org.eclipse.jetty.toolchain
Name:       jetty-schemas
Version:    3.2
Release:    3%{?dist}
Summary:    XML Schemas for Jetty

License:    CDDL or GPLv2 with exceptions
URL:        http://www.eclipse.org/jetty/
Source0:    http://git.eclipse.org/c/jetty/%{toolchain_id}.git/snapshot/%{toolchain_id}-%{name}-%{version}.%{addver}.tar.bz2
Source1:    https://glassfish.dev.java.net/public/CDDL+GPL_1_1.html

BuildArch:  noarch
BuildRequires:  maven-local

BuildRequires:  jetty-toolchain

%description
%{summary}.

%prep
%setup -q -n %{toolchain_id}-%{name}-%{version}.%{addver}
cp %SOURCE1 .

%build
pushd %{name}
%mvn_build

%install
pushd %{name}
%mvn_install

%files -f %{name}/.mfiles
%dir %{_javadir}/%{name}
%doc CDDL+GPL_1_1.html

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 02 2013 Michael Simacek <msimacek@redhat.com> - 3.1-2
- Fix License tag

* Thu Nov 28 2013 Michael Simacek <msimacek@redhat.com> - 3.1-1
- Initial version


