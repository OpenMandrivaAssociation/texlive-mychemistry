# revision 22242
# category Package
# catalog-ctan /macros/latex/contrib/mychemistry
# catalog-date 2011-04-28 13:09:24 +0200
# catalog-license lppl1.3
# catalog-version 1.5.1
Name:		texlive-mychemistry
Version:	1.5.1
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
%doc %{_texmfdistdir}/doc/latex/mychemistry/mychemistry_de.pdf
%doc %{_texmfdistdir}/doc/latex/mychemistry/mychemistry_de.tex
%doc %{_texmfdistdir}/doc/latex/mychemistry/mychemistry_en.pdf
%doc %{_texmfdistdir}/doc/latex/mychemistry/mychemistry_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
