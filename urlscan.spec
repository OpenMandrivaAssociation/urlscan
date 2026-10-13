Name:           urlscan
Version:        1.0.9
Release:        2
Summary:        Extract and browse the URLs contained in an email (urlview replacement)
License:        GPLv2+
Group:          Applications/Internet
URL:            https://github.com/firecat53/%{name}
Source0:        https://github.com/firecat53/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
#Source1:        muttrc

BuildArch:      noarch

BuildSystem:  python

BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(hatchling)
BuildRequires:  python%{pyver}dist(hatch-vcs)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(wheel)

Requires:       python%{pyver}dist(urwid)

%build -p
# GitHub archive has no tag metadata. hatch-vcs would otherwise report 0.0.0.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%description
%{name} searches for URLs in email messages, then displays a list of them in
the current terminal. It is primarily meant as a replacement for urlview.

%files
%doc LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{python_sitelib}/*
