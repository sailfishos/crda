Name:       crda
Summary:    Central regulatory domain agent for 802.11 wireless networking
Version:    3.18
Release:    1
Group:      System/Networking
License:    ISC
URL:        http://wireless.kernel.org/en/developers/Regulatory/
Source0:    http://wireless.kernel.org/download/crda/crda-%{version}.tar.bz2
Requires:   udev
Requires:   iw
Requires:   wireless-regdb
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  python
BuildRequires:  python-M2Crypto
BuildRequires:  wireless-regdb

%description
CRDA acts as the udev helper for communication between the kernel
and userspace for regulatory compliance. It relies on nl80211
for communication. CRDA is intended to be run only through udev
communication from the kernel.


%package devel
Summary:        Header files for use with libreg. 
Group:          Development/System

%description devel
Header files to make use of libreg for accessing regulatory info.


%prep
%setup -q -n %{name}-%{version}

%build
cd %{name}
make %{?jobs:-j%jobs}

%install
cd %{name}
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%doc %{name}/LICENSE
%doc %{name}/README
/lib/udev/rules.d/85-regulatory.rules
/sbin/crda
/sbin/regdbdump
%{_libdir}/libreg.so
%{_mandir}/man8/crda.8.gz
%{_mandir}/man8/regdbdump.8.gz

%files devel
%defattr(-,root,root,-)
%{_includedir}/reglib/nl80211.h
%{_includedir}/reglib/regdb.h
%{_includedir}/reglib/reglib.h

