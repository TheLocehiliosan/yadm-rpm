Summary: Yet Another Dotfiles Manager
Name: yadm
Version: 1.04
Release: 2%{?dist}
URL: https://github.com/TheLocehiliosan/yadm
License: GPLv3
BuildRequires: hostname git gnupg bats expect
Requires: bash hostname git
Source: https://github.com/TheLocehiliosan/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

%description
yadm is a tool for managing a collection of files across multiple computers,
using a shared Git repository. In addition, yadm provides a feature to select
alternate versions of files based on the operation system or host name. Lastly,
yadm supplies the ability to manage a subset of secure files, which are
encrypted before they are included in the repository.

%prep
%setup -q

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -m 755 yadm   ${RPM_BUILD_ROOT}%{_bindir}
install -m 644 yadm.1 ${RPM_BUILD_ROOT}%{_mandir}/man1

%check
bats test

%files
%attr(755,root,root) %{_bindir}/yadm
%attr(644,root,root) %{_mandir}/man1/*
%attr(644,root,root) %license LICENSE
%attr(644,root,root) %doc CHANGES

%changelog
* Mon May 16 2016 Tim Byrne <sultan@locehilios.com> 1.04-2
- Initial Fedora packaging
- Support alternate paths for yadm data
- Support asymmetric encryption
- Prevent the mixing of output and gpg prompts
