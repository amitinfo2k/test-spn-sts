Name: sxp-sts
Version:  %{version}
Release:  %{release}%{?dist}
Summary:  sts rpm packg

License:  GPL
URL:   None
Source:  sxp-sts.tar

%description
sts rpm image

%prep
%setup -n sxp-sts

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/www/html
cp -R * $RPM_BUILD_ROOT/var/www/html

%files
/var/www/html

%clean
rm -rf $RPM_BUILD_ROOT
