Name:           univocity-parsers
Version:        2.5.5
Release:        6%{?dist}
Summary:        Collection of parsers for Java
License:        ASL 2.0
URL:            https://github.com/uniVocity/univocity-parsers
BuildArch:      noarch

Source0:        https://github.com/uniVocity/univocity-parsers/archive/v%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

%description
uniVocity-parsers is a suite of extremely fast and reliable parsers
for Java.  It provides a consistent interface for handling different
file formats, and a solid framework for the development of new
parsers.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
# Tests require univocity-output-tester, which is not packaged yet.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.html

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.html

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Mat Booth <mat.booth@redhat.com> - 2.5.5-4
- Remove unnecessary javadoc invocation

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.5-1
- Initial packaging
