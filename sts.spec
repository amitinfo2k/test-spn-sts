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
mkdir -p $RPM_BUILD_ROOT/opt
cp -R * $RPM_BUILD_ROOT/opt

%files
/opt

%clean
rm -rf $RPM_BUILD_ROOT
