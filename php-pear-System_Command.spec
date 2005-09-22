%include	/usr/lib/rpm/macros.php
%define		_class		System
%define		_subclass	Command
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - commandline execution interface
Summary(pl):	%{_pearname} - interfejs do wykonywania poleceñ systemowych
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	46eb9ffc014bdd6b28c236953a9a8660
URL:		http://pear.php.net/package/System_Command/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Running functions from the commandline can be dangerous if the proper
precautions are not taken to escape the shell arguments and reaping
the exit status properly. This class give a formal interface to both,
so that you can run a system command as comfortably as you would run a
PHP function, which full pear error handling as results on failure.

In PEAR status of this package is: %{_status}.

%description -l pl
U¿ywanie funkcji z poleceñ systemowych mo¿e byæ niebezpieczne, je¶li
nie wykona³o siê odpowiedniego przygotowania parametrów i sprawdzenia
kodu wyj¶cia. Ta klasa daje formalny interfejs do obu rzeczy, co
pozwala na wywo³ywanie poleceñ systemowych w sposób tak wygodny, jak
wywo³anie funkcji PHP, która u¿ywa obs³ugi b³êdów PEAR-a w przypadku
niepowodzenia.

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
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
