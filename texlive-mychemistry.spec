# revision 28611
# category Package
# catalog-ctan /macros/latex/contrib/mychemistry
# catalog-date 2012-12-21 20:05:59 +0100
# catalog-license lppl1.3
# catalog-version 1.99b
Name:		texlive-mychemistry
Version:	1.99b
Release:	1
Summary:	Create reaction schemes with LaTeX and ChemFig
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mychemistry
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mychemistry.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mychemistry.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands for typesetting complex chemical
reaction schemes with LaTeX and ChemFig. The package requires
the packages ChemFig, mhchem, chemcompounds and (sometimes)
chemexec.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mychemistry/mychemistry.sty
%doc %{_texmfdistdir}/doc/latex/mychemistry/README
%doc %{_texmfdistdir}/doc/latex/mychemistry/examples.pdf
%doc %{_texmfdistdir}/doc/latex/mychemistry/examples.tex
%doc %{_texmfdistdir}/doc/latex/mychemistry/mychemistry_en.pdf
%doc %{_texmfdistdir}/doc/latex/mychemistry/mychemistry_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
