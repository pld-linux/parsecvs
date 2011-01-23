Summary:	RCS ,v file parser and GIT import tool
Name:		parsecvs
Version:	0.1
Release:	0.1
License:	GPL
Group:		Development
URL:		http://gitweb.freedesktop.org/?p=users/keithp/parsecvs.git
Source0:	%{name}.tar
# Source0-md5:	1aadf5cc5ee6ac86e36da07ea258757a
Patch0:		%{name}-0.1-alt6.patch
BuildRequires:	flex
BuildRequires:	git-core-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This directory contains code which can directly read RCS ,v files and
generate a git-style rev-list structure from them. Revision lists can
be merged together to produce a composite revision history for an
arbitrary collection of files.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	GIT_LIBDIR=%{_libdir} \
	GIT_INCLUDEDIR=%{_includedir}/git-core

%install
rm -rf $RPM_BUILD_ROOT
install -pD %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
