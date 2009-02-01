%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Request2
%define		_status		alpha
%define		_pearname	HTTP_Request2
Summary:	%{_pearname} - Provides an easy way to perform HTTP requests
Summary(pl.UTF-8):	%{_pearname} - dostarcza łatwą w użyciu metodę do wykonywania zapytań HTTP
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	597c8414127c152b6202a09702bf29fc
URL:		http://pear.php.net/package/HTTP_Request2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Net_URL2 >= 0.2.0
Requires:	php-pear-PEAR >= 1.4.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP5 rewrite of HTTP_Request package. Provides cleaner API and
pluggable adapters. 

Currently available are:
 - Socket adapter, based on old HTTP_Request code,
 - Curl adapter, wraps around PHP's cURL extension,
 - Mock adapter, to use for testing packages dependent on
   HTTP_Request2.

Supports POST requests with data and file uploads, authentication,
cookies, proxies, gzip and deflate encodings, monitoring the request
progress with Observers.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Port klasy HTTP_Request do PHP5. Udostępnia czystsze API oraz
dołączalne adaptery.

Obecnie dostępne są:
 - adapter oparty na gniazdach, na podstawie starego kodu
   HTTP_Request,
 - adapter Curl, 
 - adapter Mock, do testowania pakietów korzystających z
   HTTP_Request2.

Klasa ta wspiera żądania POST z dołączonymi danymi oraz plikami,
autentykację, ciastka (cookies), serwery proxy, kompresję gzip oraz
deflate encoding, oraz monitorowanie żądań za pomocą obserwatorów.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%{php_pear_dir}/HTTP/Request2
%{php_pear_dir}/HTTP/Request2.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/HTTP_Request2
