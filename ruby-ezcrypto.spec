Summary:	Ruby EZ Crypto Library
Summary(pl.UTF-8):	Biblioteka EZ Crypto dla języka Ruby
Name:		ruby-ezcrypto
Version:	0.7
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/13089/ezcrypto-0.7.tgz	
# Source0-md5:	1da109470b0cbfcfbd571e8aae99f973
URL:		http://ezcrypto.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	setup.rb = 3.4.1
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby EZ crypto library.

%description -l pl.UTF-8
Biblioteka EZ Crypto dla języka Ruby.

%prep
%setup -q -n ezcrypto-%{version}
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --ri -o ri lib
rm ri/created.rid
rdoc -o rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
install -d $RPM_BUILD_ROOT%{ruby_ridir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
