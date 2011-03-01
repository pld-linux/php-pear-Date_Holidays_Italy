%include	/usr/lib/rpm/macros.php
%define		_class		Date
%define		_subclass	Holidays_Italy
%define		_status		alpha
%define		_pearname	Date_Holidays_Italy
Summary:	%{_pearname} - Driver based class to calculate holidays in Italy
Summary(pl.UTF-8):	%{_pearname} - klasa do obliczania dat świąt włoskich
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b5f44c0ca248e014ca8d3e3f840e8b2d
URL:		http://pear.php.net/package/Date_Holidays_Italy/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Date_Holidays >= 0.21.1
Requires:	php-pear-PEAR-core >= 1.4.0b1
Obsoletes:	php-pear-Date_Holidays_Italy-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date_Holidays helps you calculate the dates and titles of holidays and
other special celebrations. This is the driver for calculating
holidays in Italy.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Date_Holidays pozwala na obliczenie dat oraz tytułów świąt oraz
specjalnych okazji. Klasa ta pozwala na wyliczenie świąt włoskich.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Date/Holidays/Driver/Italy.php
