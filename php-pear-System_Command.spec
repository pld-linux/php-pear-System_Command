%include	/usr/lib/rpm/macros.php
%define		_class		System
%define		_subclass	Command
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - commandline execution interface
Summary(pl):	%{_class}_%{_subclass} - interfejs do wykonywania poleceñ systemowych
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Running functions from the commandline can be dangerous if the proper
precautions are not taken to escape the shell arguments and reaping
the exit status properly. This class give a formal interface to both,
so that you can run a system command as comfortably as you would run a
php function, which full pear error handling as results on failure.

%description -l pl
U¿ywanie funkcji z poleceñ systemowych mo¿e byæ niebezpieczne, je¶li
nie wykona³o siê odpowiedniego przygotowania parametrów i sprawdzenia
kodu wyj¶cia. Ta klasa daje formalny interfejs do obu rzeczy, co
pozwala na wywo³ywanie poleceñ systemowych w sposób tak wygodny, jak
wywo³anie funkcji php, która u¿ywa obs³ugi b³êdów PEAR-a w przypadku
niepowodzenia.

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
