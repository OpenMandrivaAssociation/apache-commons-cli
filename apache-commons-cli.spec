Name:           apache-commons-cli
Version:        1.11.0
Release:        1
Summary:        Command Line Interface Library for Java
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-cli/
BuildArch:      noarch

Source0:        https://www.apache.org/dist/commons/cli/source/commons-cli-%{version}-src.tar.gz

Patch:          0001-Port-tests-to-commons-lang3.patch

BuildRequires:  javapackages-bootstrap

%description
The CLI library provides a simple and easy to use API for working with the
command line arguments and options.

%prep
%autosetup -p1 -C -n commons-cli-1.11.0-src

# Compatibility links
%mvn_alias : org.apache.commons:commons-cli
%mvn_file : commons-cli %{name}

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc README.md RELEASE-NOTES.txt
