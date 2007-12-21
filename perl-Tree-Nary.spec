%define real_name Tree-Nary

Summary:	Tree::Nary - Perl implementation of N-ary search trees
Name:		perl-%{real_name}
Version:	1.3
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/F/FS/FSORIANO/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Tree::Nary class implements N-ary trees (trees of data with any 
number of branches), providing the organizational structure for a tree (collection) 
of any number of nodes, but knowing nothing about the specific type of node used. 
It can be used to display hierarchical database entries in an internal application (the
NIS netgroup file is an example of such a database). It offers the capability to select 
nodes on the tree, and attachment points for nodes on the tree. Each attachment point 
can support multiple child nodes.

The data field contains the actual data of the node. The next and previous fields point
to the node's siblings (a sibling is another node with the same parent). The parent
field points to the parent of the node, or is undef if the node is the root of the
tree. The children field points to the first child of the node. The other children are
accessed by using the next pointer of each child.
This module is a translation (albeit not a direct one) from the C implementation of 
N-ary trees, available in the GLIB distribution (see SEE ALSO).

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/Tree/*.pm
%{_mandir}/*/*

