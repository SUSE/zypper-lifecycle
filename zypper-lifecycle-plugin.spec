#
# spec file for package zypper-lifecycle
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           zypper-lifecycle-plugin
Version:        0.5
Release:        0
Requires:       zypper >= 1.13.10
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  zypper >= 1.13.10
%if 0%{?suse_version} >= 1210
BuildRequires: systemd-rpm-macros
%endif
%{?systemd_requires}

Source1:        zypper-lifecycle
Source2:        zypper-lifecycle.8
Source3:        lifecycle-report.service
Source4:        lifecycle-report.timer
Source5:        lifecycle-report
Summary:        Zypper subcommand for lifecycle information
License:        GPL-2.0
Group:          System/Packages
BuildArch:      noarch
Supplements:    zypper

%description
Zypper subcommand for products and packages lifecycle information.

%prep

%build

%install
mkdir -p %{buildroot}/usr/lib/zypper/commands %{buildroot}/%{_mandir}/man8
install -m 755 %{S:1} %{buildroot}/usr/lib/zypper/commands/
install -m 644 %{S:2} %{buildroot}/%{_mandir}/man8/
mkdir -p %{buildroot}/var/lib/lifecycle
mkdir -p %{buildroot}/usr/share/lifecycle
install -m 755 %{S:5} %{buildroot}/usr/share/lifecycle/
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 644 %{S:3} %{buildroot}%{_unitdir}
install -m 644 %{S:4} %{buildroot}%{_unitdir}

%pre
%service_add_pre lifecycle-report.service lifecycle-report.timer

%post
%service_add_post lifecycle-report.service lifecycle-report.timer

%preun
%service_del_preun lifecycle-report.service lifecycle-report.timer

%postun
%service_del_postun lifecycle-report.service lifecycle-report.timer

%files
%defattr(-,root,root,-)
/usr/lib/zypper/commands
/usr/share/lifecycle
/var/lib/lifecycle
%{_mandir}/man8/*
%{_unitdir}/*

%changelog
