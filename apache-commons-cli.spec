Name:		apache-commons-cli
Version:	1.11.0
Release:	1
Summary:	Command line arguments and options
Group:		Development/Java
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-cli/
Source0:	https://www.apache.org/dist/commons/cli/source/commons-cli-%{version}-src.tar.gz
BuildArch:	noarch
# The site checkout profile is active when site-content is absent, and
# antrun is on the sysjar keep list. It only runs svn for the website.
%global sysjar_drops --drop org.apache.maven.plugins:maven-antrun-plugin
BuildRequires:	mvn(org.apache.commons:commons-parent:pom::)
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name commons-cli --link %{name} --alias org.apache.commons:commons-cli

%description
Apache Commons CLI presents, processes, and validates command line
arguments. 1.11.0 adds CommandLine.getOptionCount() and fixes help
formatting for option groups and trailing break characters.

%prep
%autosetup -n commons-cli-%{version}-src

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.md RELEASE-NOTES.txt
