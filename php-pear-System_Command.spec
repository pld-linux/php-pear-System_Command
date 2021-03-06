%define		status		stable
%define		pearname	System_Command
Summary:	%{pearname} - commandline execution interface
Summary(pl.UTF-8):	%{pearname} - interfejs do wykonywania poleceń systemowych
Name:		php-pear-%{pearname}
Version:	1.0.8
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	c90211d85422a60c626a15fcc56702fd
URL:		http://pear.php.net/package/System_Command/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Running functions from the commandline can be dangerous if the proper
precautions are not taken to escape the shell arguments and reaping
the exit status properly. This class give a formal interface to both,
so that you can run a system command as comfortably as you would run a
PHP function, which full pear error handling as results on failure.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Używanie funkcji z poleceń systemowych może być niebezpieczne, jeśli
nie wykonało się odpowiedniego przygotowania parametrów i sprawdzenia
kodu wyjścia. Ta klasa daje formalny interfejs do obu rzeczy, co
pozwala na wywoływanie poleceń systemowych w sposób tak wygodny, jak
wywołanie funkcji PHP, która używa obsługi błędów PEAR-a w przypadku
niepowodzenia.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/System_Command/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/System
%{php_pear_dir}/System/*.php
