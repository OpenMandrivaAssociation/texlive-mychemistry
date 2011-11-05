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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides commands for typesetting complex chemical
reaction schemes with LaTeX and ChemFig. The package requires
the packages ChemFig, mhchem, chemcompounds and (sometimes)
chemexec.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
