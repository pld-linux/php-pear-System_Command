%include	/usr/lib/rpm/macros.php
%define		_class		System
%define		_subclass	Command
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - commandline execution interface
Summary(pl):	%{_pearname} - interfejs do wykonywania polece� systemowych
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1cdc6c0797c719cf5c0cc4d21f1be058
URL:		http://pear.php.net/package/System_Command/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Running functions from the commandline can be dangerous if the proper
precautions are not taken to escape the shell arguments and reaping
the exit status properly. This class give a formal interface to both,
so that you can run a system command as comfortably as you would run a
php function, which full pear error handling as results on failure.

This class has in PEAR status: %{_status}.

%description -l pl
U�ywanie funkcji z polece� systemowych mo�e by� niebezpieczne, je�li
nie wykona�o si� odpowiedniego przygotowania parametr�w i sprawdzenia
kodu wyj�cia. Ta klasa daje formalny interfejs do obu rzeczy, co
pozwala na wywo�ywanie polece� systemowych w spos�b tak wygodny, jak
wywo�anie funkcji php, kt�ra u�ywa obs�ugi b��d�w PEAR-a w przypadku
niepowodzenia.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php