Name:       crda
Summary:    Central regulatory domain agent for 802.11 wireless networking
Version:    4.14
Release:    1
License:    ISC
URL:        http://wireless.kernel.org/en/developers/Regulatory/
Source0:    %{name}-%{version}.tar.bz2
# Apply patches to crda/ and then in ./crda use:
#  git format-patch --base=<upstream-tag> <upstream-tag>..<sfos/tag> -o ../rpm/
# this set is:
#  git format-patch --base=v4.14 v4.14..jolla/crda-4.14 -o ../rpm/
Patch1:    0001-use-python3.patch
Patch2:    0002-Reorganise-vars-and-use-LIBDIR-for-regulatory.bin.patch
Requires:   udev
Requires:   iw
Requires:   wireless-regdb
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  python3-base
BuildRequires:  python-M2Crypto
BuildRequires:  wireless-regdb

%description
CRDA acts as the udev helper for communication between the kernel
and userspace for regulatory compliance. It relies on nl80211
for communication. CRDA is intended to be run only through udev
communication from the kernel.

%package devel
Summary:    Header files for use with libreg. 
Requires:   %{name} = %{version}-%{release}

%description devel
Header files to make use of libreg for accessing regulatory info.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}/crda

%build
# Drop ldconfig as it breaks the build in OBS. Also we need this only in package install time
# which is handled by %post
sed -i '/$(Q)ldconfig/d' Makefile
PUBKEY_DIR=%{_libdir}/crda/pubkeys/ RUNTIME_PUBKEY_DIR=%{_libdir}/crda/pubkeys/ LIBDIR=%{_libdir} V=1 make %{?_smp_mflags}

%install
rm -rf %{buildroot}
# The %%make_install macro does not pass args or take same-line environment vars so:
export LIBDIR=%{_libdir}
export V=1
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} README

%post
/sbin/ldconfig || :

%files
%defattr(-,root,root,-)
%license LICENSE
/lib/udev/rules.d/85-regulatory.rules
/sbin/crda
/sbin/regdbdump
%{_libdir}/libreg.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/reglib/nl80211.h
%{_includedir}/reglib/regdb.h
%{_includedir}/reglib/reglib.h

%files doc
%defattr(-,root,root,-)
%{_mandir}/man8/%{name}.*
%{_mandir}/man8/regdbdump.*
%{_docdir}/%{name}-%{version}
