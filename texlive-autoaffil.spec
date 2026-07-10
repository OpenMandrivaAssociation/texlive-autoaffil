%global tl_name autoaffil
%global tl_revision 79311

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Automatic deduplicated affiliation numbering
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/autoaffil
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autoaffil.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autoaffil.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autoaffil.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the author and affiliation layout style common in
physics and related fields. All authors appear in a single block with
superscript numbers linking each name to a list of affiliations printed
below. This is the style native to revtex4-2 with the superscriptaddress
option, and is familiar from journals such as Physical Review Letters.
The package brings this style to the standard article class and
compatible classes, without requiring a specialised document class.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/autoaffil
%dir %{_datadir}/texmf-dist/source/latex/autoaffil
%dir %{_datadir}/texmf-dist/tex/latex/autoaffil
%doc %{_datadir}/texmf-dist/doc/latex/autoaffil/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/latex/autoaffil/README.md
%doc %{_datadir}/texmf-dist/doc/latex/autoaffil/autoaffil.pdf
%doc %{_datadir}/texmf-dist/source/latex/autoaffil/autoaffil.dtx
%doc %{_datadir}/texmf-dist/source/latex/autoaffil/autoaffil.ins
%{_datadir}/texmf-dist/tex/latex/autoaffil/autoaffil.sty
