%define		status		beta
%define		pearname	HTTP_Request2
%define		subver	RC1
%define		rel		1
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Provides an easy way to perform HTTP requests
Summary(pl.UTF-8):	%{pearname} - dostarcza łatwą w użyciu metodę do wykonywania zapytań HTTP
Name:		php-pear-%{pearname}
Version:	2.0.0
Release:	0.%{subver}.%{rel}
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}%{subver}.tgz
# Source0-md5:	f1633221537fa3d69adbc4c1ef1f3000
URL:		http://pear.php.net/package/HTTP_Request2/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-Net_URL2 >= 0.3.0
Suggests:	php-curl
Suggests:	php-fileinfo
Suggests:	php-openssl
Suggests:	php-zlib
Obsoletes:	php-pear-HTTP_Request2-tests
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

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Port klasy HTTP_Request do PHP5. Udostępnia czystsze API oraz
dołączalne adaptery.

Obecnie dostępne są:
 - adapter oparty na gniazdach, na podstawie starego kodu HTTP_Request,
 - adapter Curl,
 - adapter Mock, do testowania pakietów korzystających z HTTP_Request2.

Klasa ta wspiera żądania POST z dołączonymi danymi oraz plikami,
autentykację, ciastka (cookies), serwery proxy, kompresję gzip oraz
deflate encoding, oraz monitorowanie żądań za pomocą obserwatorów.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

rm .%{php_pear_dir}/data/HTTP_Request2/generate-list.php

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

%{php_pear_dir}/data/%{pearname}
