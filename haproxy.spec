Name: sxp-haproxy
Version:  %{version}
Release:  %{release}%{?dist}
Summary:  HA Proxy bake image

License:  GPL
URL:   None
Source:  sxp-haproxy.tar
#BuildRoot: /var/lib/jenkins/workspace/Build\ RPM/rpmbuild/%{name}-%{version}

%description
HA Proxy bake image

%prep
%setup -n sxp-haproxy


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/haproxy
cp -R * $RPM_BUILD_ROOT/etc/haproxy

%files
/etc/haproxy

%clean
rm -rf $RPM_BUILD_ROOT
