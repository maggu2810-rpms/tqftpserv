%global debug_package %{nil}
%global commit 783425b550de2a359db6aa3b41577c3fbaae5903

Name:           tqftpserv
Version:        20200207
Release:        1%{?dist}
Summary:        Trivial File Transfer Protocol server over AF_QIPCRTR

License:        BSD-3-Clause
URL:            https://github.com/andersson/tqftpserv
Source0:        https://github.com/andersson/tqftpserv/archive/%{commit}/qftpserv-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  qrtr

%description
%summary.

%prep
%autosetup -n %{name}-%{commit}

%build
%make_build

%install
%make_install prefix=/usr
#install -D tqftpserv %{buildroot}/usr/bin/tqftpserv
#install -D %{buildroot}/usr/lib/systemd/system/tqftpserv.service
#install -D %{buildroot}/usr/share/tqftpserv/LICENSE

%files
%license LICENSE
%{_bindir}/tqftpserv
/usr/lib/systemd/system/tqftpserv.service

%changelog
* Wed May 10 2023 Justin Zobel <justin@1707.io>
- Initial Commit
