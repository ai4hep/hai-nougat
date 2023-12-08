# This Makefile is for the LaTeXML extension to perl.
#
# It was generated automatically by MakeMaker version
# 7.70 (Revision: 77000) from the contents of
# Makefile.PL. Don't edit this file, edit Makefile.PL instead.
#
#       ANY CHANGES MADE HERE WILL BE LOST!
#
#   MakeMaker ARGV: ()
#

#   MakeMaker Parameters:

#     ABSTRACT => q[transforms TeX and LaTeX into XML/HTML/MathML]
#     AUTHOR => [q[Bruce Miller <bruce.miller@nist.gov>], q[Deyan Ginev <deyan.ginev@gmail.com>]]
#     BUILD_REQUIRES => {  }
#     CONFIGURE_REQUIRES => { version=>q[0.77] }
#     EXE_FILES => [q[bin/latexml], q[bin/latexmlpost], q[bin/latexmlfind], q[bin/latexmlmath], q[bin/latexmlc]]
#     LICENSE => q[open_source]
#     META_MERGE => { meta-spec=>{ version=>q[2] }, resources=>{ bugtracker=>{ web=>q[https://github.com/brucemiller/LaTeXML/issues] }, repository=>{ type=>q[git], url=>q[https://github.com/brucemiller/LaTeXML.git], web=>q[https://github.com/brucemiller/LaTeXML] } } }
#     MIN_PERL_VERSION => q[5.010001]
#     NAME => q[LaTeXML]
#     PREREQ_PM => { Archive::Zip=>q[0], DB_File=>q[0], File::Which=>q[0], Getopt::Long=>q[2.37], IO::Handle=>q[0], IO::String=>q[0], Image::Size=>q[0], JSON::XS=>q[0], LWP=>q[0], MIME::Base64=>q[0], Parse::RecDescent=>q[0], Pod::Parser=>q[0], Test::More=>q[0], Text::Unidecode=>q[0], Time::HiRes=>q[0], URI=>q[0], XML::LibXML=>q[1.61], XML::LibXSLT=>q[1.58], version=>q[0] }
#     TEST_REQUIRES => {  }
#     VERSION_FROM => q[lib/LaTeXML.pm]
#     macro => { DESTINSTALLTEXMFBASEDIR=>q[$(DESTDIR)$(INSTALLTEXMFBASEDIR)], DESTINSTALLTEXMFDIR=>q[$(DESTDIR)$(INSTALLTEXMFDIR)], INSTALLTEXMFBASEDIR=>q[$TEXMFLOCAL], INSTALLTEXMFDIR=>q[$TEXMFLOCAL/tex/latex/latexml], INST_TEXMFDIR=>q[$(INST_LIB)/LaTeXML/texmf], RECORD_REVISION=>q[$(PERLRUN) -pe "s@__REVISION__@$(REVISION)@" ], REVISION_BASE=>q[/data/luojw/nogut/LaTeXML-0.8.7], REVISION_FILE=>q[$(INST_LIBDIR)/LaTeXML/Version.pm] }

# --- MakeMaker post_initialize section:


# --- MakeMaker const_config section:

# These definitions are from config.sh (via /usr/lib64/perl5/Config.pm).
# They may have been overridden via Makefile.PL or on the command line.
AR = ar
CC = gcc
CCCDLFLAGS = -fPIC
CCDLFLAGS = -Wl,--enable-new-dtags -Wl,-z,relro -Wl,--as-needed -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 
CPPRUN = gcc  -E
DLEXT = so
DLSRC = dl_dlopen.xs
EXE_EXT = 
FULL_AR = /usr/bin/ar
LD = gcc
LDDLFLAGS = -lpthread -shared -Wl,-z,relro -Wl,--as-needed -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -L/usr/local/lib -fstack-protector-strong
LDFLAGS = -Wl,-z,relro -Wl,--as-needed -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -fstack-protector-strong -L/usr/local/lib
LIBC = /lib/../lib64/libc.so.6
LIB_EXT = .a
OBJ_EXT = .o
OSNAME = linux
OSVERS = 4.18.0-425.3.1.el8.x86_64
RANLIB = :
SITELIBEXP = /usr/local/share/perl5/5.32
SITEARCHEXP = /usr/local/lib64/perl5/5.32
SO = so
VENDORARCHEXP = /usr/lib64/perl5/vendor_perl
VENDORLIBEXP = /usr/share/perl5/vendor_perl


# --- MakeMaker constants section:
AR_STATIC_ARGS = cr
DIRFILESEP = /
DFSEP = $(DIRFILESEP)
NAME = LaTeXML
NAME_SYM = LaTeXML
VERSION = 0.8.7
VERSION_MACRO = VERSION
VERSION_SYM = 0_8_7
DEFINE_VERSION = -D$(VERSION_MACRO)=\"$(VERSION)\"
XS_VERSION = 0.8.7
XS_VERSION_MACRO = XS_VERSION
XS_DEFINE_VERSION = -D$(XS_VERSION_MACRO)=\"$(XS_VERSION)\"
INST_ARCHLIB = blib/arch
INST_SCRIPT = blib/script
INST_BIN = blib/bin
INST_LIB = blib/lib
INST_MAN1DIR = blib/man1
INST_MAN3DIR = blib/man3
MAN1EXT = 1
MAN3EXT = 3pm
MAN1SECTION = 1
MAN3SECTION = 3
INSTALLDIRS = site
DESTDIR = 
PREFIX = $(SITEPREFIX)
PERLPREFIX = /usr
SITEPREFIX = /usr/local
VENDORPREFIX = /usr
INSTALLPRIVLIB = /usr/share/perl5
DESTINSTALLPRIVLIB = $(DESTDIR)$(INSTALLPRIVLIB)
INSTALLSITELIB = /usr/local/share/perl5/5.32
DESTINSTALLSITELIB = $(DESTDIR)$(INSTALLSITELIB)
INSTALLVENDORLIB = /usr/share/perl5/vendor_perl
DESTINSTALLVENDORLIB = $(DESTDIR)$(INSTALLVENDORLIB)
INSTALLARCHLIB = /usr/lib64/perl5
DESTINSTALLARCHLIB = $(DESTDIR)$(INSTALLARCHLIB)
INSTALLSITEARCH = /usr/local/lib64/perl5/5.32
DESTINSTALLSITEARCH = $(DESTDIR)$(INSTALLSITEARCH)
INSTALLVENDORARCH = /usr/lib64/perl5/vendor_perl
DESTINSTALLVENDORARCH = $(DESTDIR)$(INSTALLVENDORARCH)
INSTALLBIN = /usr/bin
DESTINSTALLBIN = $(DESTDIR)$(INSTALLBIN)
INSTALLSITEBIN = /usr/local/bin
DESTINSTALLSITEBIN = $(DESTDIR)$(INSTALLSITEBIN)
INSTALLVENDORBIN = /usr/bin
DESTINSTALLVENDORBIN = $(DESTDIR)$(INSTALLVENDORBIN)
INSTALLSCRIPT = /usr/bin
DESTINSTALLSCRIPT = $(DESTDIR)$(INSTALLSCRIPT)
INSTALLSITESCRIPT = /usr/local/bin
DESTINSTALLSITESCRIPT = $(DESTDIR)$(INSTALLSITESCRIPT)
INSTALLVENDORSCRIPT = /usr/bin
DESTINSTALLVENDORSCRIPT = $(DESTDIR)$(INSTALLVENDORSCRIPT)
INSTALLMAN1DIR = /usr/share/man/man1
DESTINSTALLMAN1DIR = $(DESTDIR)$(INSTALLMAN1DIR)
INSTALLSITEMAN1DIR = /usr/local/share/man/man1
DESTINSTALLSITEMAN1DIR = $(DESTDIR)$(INSTALLSITEMAN1DIR)
INSTALLVENDORMAN1DIR = /usr/share/man/man1
DESTINSTALLVENDORMAN1DIR = $(DESTDIR)$(INSTALLVENDORMAN1DIR)
INSTALLMAN3DIR = /usr/share/man/man3
DESTINSTALLMAN3DIR = $(DESTDIR)$(INSTALLMAN3DIR)
INSTALLSITEMAN3DIR = /usr/local/share/man/man3
DESTINSTALLSITEMAN3DIR = $(DESTDIR)$(INSTALLSITEMAN3DIR)
INSTALLVENDORMAN3DIR = /usr/share/man/man3
DESTINSTALLVENDORMAN3DIR = $(DESTDIR)$(INSTALLVENDORMAN3DIR)
PERL_LIB = /usr/share/perl5
PERL_ARCHLIB = /usr/lib64/perl5
PERL_ARCHLIBDEP = /usr/lib64/perl5
LIBPERL_A = libperl.a
FIRST_MAKEFILE = Makefile
MAKEFILE_OLD = Makefile.old
MAKE_APERL_FILE = Makefile.aperl
PERLMAINCC = $(CC)
PERL_INC = /usr/lib64/perl5/CORE
PERL_INCDEP = /usr/lib64/perl5/CORE
PERL = "/usr/bin/perl"
FULLPERL = "/usr/bin/perl"
ABSPERL = $(PERL)
PERLRUN = $(PERL)
FULLPERLRUN = $(FULLPERL)
ABSPERLRUN = $(ABSPERL)
PERLRUNINST = $(PERLRUN) "-I$(INST_ARCHLIB)" "-I$(INST_LIB)"
FULLPERLRUNINST = $(FULLPERLRUN) "-I$(INST_ARCHLIB)" "-I$(INST_LIB)"
ABSPERLRUNINST = $(ABSPERLRUN) "-I$(INST_ARCHLIB)" "-I$(INST_LIB)"
PERL_CORE = 0
PERM_DIR = 755
PERM_RW = 644
PERM_RWX = 755

MAKEMAKER   = /usr/local/share/perl5/5.32/ExtUtils/MakeMaker.pm
MM_VERSION  = 7.70
MM_REVISION = 77000

# FULLEXT = Pathname for extension directory (eg Foo/Bar/Oracle).
# BASEEXT = Basename part of FULLEXT. May be just equal FULLEXT. (eg Oracle)
# PARENT_NAME = NAME without BASEEXT and no trailing :: (eg Foo::Bar)
# DLBASE  = Basename part of dynamic library. May be just equal BASEEXT.
MAKE = make
FULLEXT = LaTeXML
BASEEXT = LaTeXML
PARENT_NAME = 
DLBASE = $(BASEEXT)
VERSION_FROM = lib/LaTeXML.pm
OBJECT = 
LDFROM = $(OBJECT)
LINKTYPE = dynamic
BOOTDEP = 

# Handy lists of source code files:
XS_FILES = 
C_FILES  = 
O_FILES  = 
H_FILES  = 
MAN1PODS = bin/latexml \
	bin/latexmlc \
	bin/latexmlfind \
	bin/latexmlmath \
	bin/latexmlpost
MAN3PODS = lib/LaTeXML.pm \
	lib/LaTeXML/Common/Color.pm \
	lib/LaTeXML/Common/Color/Derived.pm \
	lib/LaTeXML/Common/Color/cmy.pm \
	lib/LaTeXML/Common/Color/cmyk.pm \
	lib/LaTeXML/Common/Color/gray.pm \
	lib/LaTeXML/Common/Color/hsb.pm \
	lib/LaTeXML/Common/Color/rgb.pm \
	lib/LaTeXML/Common/Config.pm \
	lib/LaTeXML/Common/Dimension.pm \
	lib/LaTeXML/Common/Error.pm \
	lib/LaTeXML/Common/Float.pm \
	lib/LaTeXML/Common/Font.pm \
	lib/LaTeXML/Common/Glue.pm \
	lib/LaTeXML/Common/Locator.pm \
	lib/LaTeXML/Common/Model.pm \
	lib/LaTeXML/Common/Model/DTD.pm \
	lib/LaTeXML/Common/Model/RelaxNG.pm \
	lib/LaTeXML/Common/Number.pm \
	lib/LaTeXML/Common/Object.pm \
	lib/LaTeXML/Common/XML.pm \
	lib/LaTeXML/Core.pm \
	lib/LaTeXML/Core/Alignment.pm \
	lib/LaTeXML/Core/Array.pm \
	lib/LaTeXML/Core/Box.pm \
	lib/LaTeXML/Core/Comment.pm \
	lib/LaTeXML/Core/Definition.pm \
	lib/LaTeXML/Core/Definition/CharDef.pm \
	lib/LaTeXML/Core/Definition/Conditional.pm \
	lib/LaTeXML/Core/Definition/Constructor.pm \
	lib/LaTeXML/Core/Definition/Expandable.pm \
	lib/LaTeXML/Core/Definition/Primitive.pm \
	lib/LaTeXML/Core/Definition/Register.pm \
	lib/LaTeXML/Core/Document.pm \
	lib/LaTeXML/Core/Gullet.pm \
	lib/LaTeXML/Core/KeyVal.pm \
	lib/LaTeXML/Core/KeyVals.pm \
	lib/LaTeXML/Core/List.pm \
	lib/LaTeXML/Core/Mouth.pm \
	lib/LaTeXML/Core/Mouth/Binding.pm \
	lib/LaTeXML/Core/Mouth/file.pm \
	lib/LaTeXML/Core/Mouth/http.pm \
	lib/LaTeXML/Core/Mouth/https.pm \
	lib/LaTeXML/Core/MuDimension.pm \
	lib/LaTeXML/Core/MuGlue.pm \
	lib/LaTeXML/Core/Pair.pm \
	lib/LaTeXML/Core/PairList.pm \
	lib/LaTeXML/Core/Parameter.pm \
	lib/LaTeXML/Core/Parameters.pm \
	lib/LaTeXML/Core/Rewrite.pm \
	lib/LaTeXML/Core/State.pm \
	lib/LaTeXML/Core/Stomach.pm \
	lib/LaTeXML/Core/Token.pm \
	lib/LaTeXML/Core/Tokens.pm \
	lib/LaTeXML/Core/Whatsit.pm \
	lib/LaTeXML/Global.pm \
	lib/LaTeXML/MathParser.pm \
	lib/LaTeXML/Package.pm \
	lib/LaTeXML/Post.pm \
	lib/LaTeXML/Post/MathML.pm \
	lib/LaTeXML/Post/UnicodeMath.pm \
	lib/LaTeXML/Pre/BibTeX.pm \
	lib/LaTeXML/Util/Pack.pm \
	lib/LaTeXML/Util/Pathname.pm \
	lib/LaTeXML/Util/Radix.pm \
	lib/LaTeXML/Util/Unicode.pm \
	lib/LaTeXML/Util/WWW.pm

# Where is the Config information that we are using/depend on
CONFIGDEP = $(PERL_ARCHLIBDEP)$(DFSEP)Config.pm $(PERL_INCDEP)$(DFSEP)config.h

# Where to build things
INST_LIBDIR      = $(INST_LIB)
INST_ARCHLIBDIR  = $(INST_ARCHLIB)

INST_AUTODIR     = $(INST_LIB)/auto/$(FULLEXT)
INST_ARCHAUTODIR = $(INST_ARCHLIB)/auto/$(FULLEXT)

INST_STATIC      = 
INST_DYNAMIC     = 
INST_BOOT        = 

# Extra linker info
EXPORT_LIST        = 
PERL_ARCHIVE       = 
PERL_ARCHIVEDEP    = 
PERL_ARCHIVE_AFTER = 


TO_INST_PM = lib/LaTeXML.pm \
	lib/LaTeXML/Common/Color.pm \
	lib/LaTeXML/Common/Color/Derived.pm \
	lib/LaTeXML/Common/Color/cmy.pm \
	lib/LaTeXML/Common/Color/cmyk.pm \
	lib/LaTeXML/Common/Color/gray.pm \
	lib/LaTeXML/Common/Color/hsb.pm \
	lib/LaTeXML/Common/Color/rgb.pm \
	lib/LaTeXML/Common/Config.pm \
	lib/LaTeXML/Common/Dimension.pm \
	lib/LaTeXML/Common/Error.pm \
	lib/LaTeXML/Common/Float.pm \
	lib/LaTeXML/Common/Font.pm \
	lib/LaTeXML/Common/Font/Metric.pm \
	lib/LaTeXML/Common/Font/StandardMetrics.pm \
	lib/LaTeXML/Common/Glue.pm \
	lib/LaTeXML/Common/Locator.pm \
	lib/LaTeXML/Common/Model.pm \
	lib/LaTeXML/Common/Model/DTD.pm \
	lib/LaTeXML/Common/Model/RelaxNG.pm \
	lib/LaTeXML/Common/Number.pm \
	lib/LaTeXML/Common/Object.pm \
	lib/LaTeXML/Common/XML.pm \
	lib/LaTeXML/Common/XML/Parser.pm \
	lib/LaTeXML/Common/XML/RelaxNG.pm \
	lib/LaTeXML/Common/XML/XPath.pm \
	lib/LaTeXML/Common/XML/XSLT.pm \
	lib/LaTeXML/Core.pm \
	lib/LaTeXML/Core/Alignment.pm \
	lib/LaTeXML/Core/Alignment/Template.pm \
	lib/LaTeXML/Core/Array.pm \
	lib/LaTeXML/Core/Box.pm \
	lib/LaTeXML/Core/Comment.pm \
	lib/LaTeXML/Core/Definition.pm \
	lib/LaTeXML/Core/Definition/CharDef.pm \
	lib/LaTeXML/Core/Definition/Conditional.pm \
	lib/LaTeXML/Core/Definition/Constructor.pm \
	lib/LaTeXML/Core/Definition/Constructor/Compiler.pm \
	lib/LaTeXML/Core/Definition/Expandable.pm \
	lib/LaTeXML/Core/Definition/Primitive.pm \
	lib/LaTeXML/Core/Definition/Register.pm \
	lib/LaTeXML/Core/Document.pm \
	lib/LaTeXML/Core/Gullet.pm \
	lib/LaTeXML/Core/KeyVal.pm \
	lib/LaTeXML/Core/KeyVals.pm \
	lib/LaTeXML/Core/List.pm \
	lib/LaTeXML/Core/Mouth.pm \
	lib/LaTeXML/Core/Mouth/Binding.pm \
	lib/LaTeXML/Core/Mouth/file.pm \
	lib/LaTeXML/Core/Mouth/http.pm \
	lib/LaTeXML/Core/Mouth/https.pm \
	lib/LaTeXML/Core/MuDimension.pm \
	lib/LaTeXML/Core/MuGlue.pm \
	lib/LaTeXML/Core/Pair.pm \
	lib/LaTeXML/Core/PairList.pm \
	lib/LaTeXML/Core/Parameter.pm \
	lib/LaTeXML/Core/Parameters.pm \
	lib/LaTeXML/Core/Rewrite.pm \
	lib/LaTeXML/Core/State.pm \
	lib/LaTeXML/Core/Stomach.pm \
	lib/LaTeXML/Core/Token.pm \
	lib/LaTeXML/Core/Tokens.pm \
	lib/LaTeXML/Core/Whatsit.pm \
	lib/LaTeXML/Global.pm \
	lib/LaTeXML/LaTeXML.catalog \
	lib/LaTeXML/MathParser.pm \
	lib/LaTeXML/Package.pm \
	lib/LaTeXML/Package/AmSTeX.pool.ltxml \
	lib/LaTeXML/Package/BibTeX.pool.ltxml \
	lib/LaTeXML/Package/IEEEtran.cls.ltxml \
	lib/LaTeXML/Package/JHEP.cls.ltxml \
	lib/LaTeXML/Package/JHEP2.cls.ltxml \
	lib/LaTeXML/Package/JHEP3.cls.ltxml \
	lib/LaTeXML/Package/LaTeX.pool.ltxml \
	lib/LaTeXML/Package/OmniBus.cls.ltxml \
	lib/LaTeXML/Package/PoS.cls.ltxml \
	lib/LaTeXML/Package/SIunits.sty.ltxml \
	lib/LaTeXML/Package/TeX.pool.ltxml \
	lib/LaTeXML/Package/a0poster.cls.ltxml \
	lib/LaTeXML/Package/a0size.sty.ltxml \
	lib/LaTeXML/Package/a4.sty.ltxml \
	lib/LaTeXML/Package/a4wide.sty.ltxml \
	lib/LaTeXML/Package/aa.cls.ltxml \
	lib/LaTeXML/Package/aa_support.sty.ltxml \
	lib/LaTeXML/Package/aas_macros.sty.ltxml \
	lib/LaTeXML/Package/aas_support.sty.ltxml \
	lib/LaTeXML/Package/aasms.sty.ltxml \
	lib/LaTeXML/Package/aaspp.sty.ltxml \
	lib/LaTeXML/Package/aastex.cls.ltxml \
	lib/LaTeXML/Package/aastex.sty.ltxml \
	lib/LaTeXML/Package/accents.sty.ltxml \
	lib/LaTeXML/Package/acmart.cls.ltxml \
	lib/LaTeXML/Package/acronym.sty.ltxml \
	lib/LaTeXML/Package/actuarialangle.sty.ltxml \
	lib/LaTeXML/Package/adjustbox.sty.ltxml \
	lib/LaTeXML/Package/ae.sty.ltxml \
	lib/LaTeXML/Package/aecompl.sty.ltxml \
	lib/LaTeXML/Package/afterpage.sty.ltxml \
	lib/LaTeXML/Package/aipcheck.tex.ltxml \
	lib/LaTeXML/Package/aipproc.cls.ltxml \
	lib/LaTeXML/Package/aipproc.sty.ltxml \
	lib/LaTeXML/Package/algc.sty.ltxml \
	lib/LaTeXML/Package/algcompatible.sty.ltxml \
	lib/LaTeXML/Package/algmatlab.sty.ltxml \
	lib/LaTeXML/Package/algorithm.sty.ltxml \
	lib/LaTeXML/Package/algorithm2e.sty.ltxml \
	lib/LaTeXML/Package/algorithmic.sty.ltxml \
	lib/LaTeXML/Package/algorithmicx.sty.ltxml \
	lib/LaTeXML/Package/algpascal.sty.ltxml \
	lib/LaTeXML/Package/algpseudocode.sty.ltxml \
	lib/LaTeXML/Package/alltt.sty.ltxml \
	lib/LaTeXML/Package/ams_core.cls.ltxml \
	lib/LaTeXML/Package/ams_support.sty.ltxml \
	lib/LaTeXML/Package/amsa.fontmap.ltxml \
	lib/LaTeXML/Package/amsaddr.sty.ltxml \
	lib/LaTeXML/Package/amsart.cls.ltxml \
	lib/LaTeXML/Package/amsb.fontmap.ltxml \
	lib/LaTeXML/Package/amsbook.cls.ltxml \
	lib/LaTeXML/Package/amsbsy.sty.ltxml \
	lib/LaTeXML/Package/amscd.sty.ltxml \
	lib/LaTeXML/Package/amsfonts.sty.ltxml \
	lib/LaTeXML/Package/amsgen.sty.ltxml \
	lib/LaTeXML/Package/amsmath.sty.ltxml \
	lib/LaTeXML/Package/amsopn.sty.ltxml \
	lib/LaTeXML/Package/amsppt.sty.ltxml \
	lib/LaTeXML/Package/amsproc.cls.ltxml \
	lib/LaTeXML/Package/amsrefs.sty.ltxml \
	lib/LaTeXML/Package/amssymb.sty.ltxml \
	lib/LaTeXML/Package/amstex.sty.ltxml \
	lib/LaTeXML/Package/amstex.tex.ltxml \
	lib/LaTeXML/Package/amstext.sty.ltxml \
	lib/LaTeXML/Package/amsthm.sty.ltxml \
	lib/LaTeXML/Package/amsxtra.sty.ltxml \
	lib/LaTeXML/Package/apjfonts.sty.ltxml \
	lib/LaTeXML/Package/appendix.sty.ltxml \
	lib/LaTeXML/Package/applemac.def.ltxml \
	lib/LaTeXML/Package/array.sty.ltxml \
	lib/LaTeXML/Package/article.cls.ltxml \
	lib/LaTeXML/Package/attachfile.sty.ltxml \
	lib/LaTeXML/Package/atveryend.sty.ltxml \
	lib/LaTeXML/Package/authblk.sty.ltxml \
	lib/LaTeXML/Package/auxhook.sty.ltxml \
	lib/LaTeXML/Package/avant.sty.ltxml \
	lib/LaTeXML/Package/babel.def.ltxml \
	lib/LaTeXML/Package/babel.sty.ltxml \
	lib/LaTeXML/Package/babel_support.sty.ltxml \
	lib/LaTeXML/Package/balance.sty.ltxml \
	lib/LaTeXML/Package/bbding.sty.ltxml \
	lib/LaTeXML/Package/bbm.sty.ltxml \
	lib/LaTeXML/Package/bbold.sty.ltxml \
	lib/LaTeXML/Package/beamer.cls.ltxml \
	lib/LaTeXML/Package/beton.sty.ltxml \
	lib/LaTeXML/Package/bezier.sty.ltxml \
	lib/LaTeXML/Package/bibunits.sty.ltxml \
	lib/LaTeXML/Package/bigintcalc.sty.ltxml \
	lib/LaTeXML/Package/bitset.sty.ltxml \
	lib/LaTeXML/Package/blindtext.sty.ltxml \
	lib/LaTeXML/Package/bm.sty.ltxml \
	lib/LaTeXML/Package/book.cls.ltxml \
	lib/LaTeXML/Package/bookman.sty.ltxml \
	lib/LaTeXML/Package/bookmark.sty.ltxml \
	lib/LaTeXML/Package/booktabs.sty.ltxml \
	lib/LaTeXML/Package/braket.sty.ltxml \
	lib/LaTeXML/Package/breakurl.sty.ltxml \
	lib/LaTeXML/Package/calc.sty.ltxml \
	lib/LaTeXML/Package/calrsfs.sty.ltxml \
	lib/LaTeXML/Package/cancel.sty.ltxml \
	lib/LaTeXML/Package/caption.sty.ltxml \
	lib/LaTeXML/Package/cases.sty.ltxml \
	lib/LaTeXML/Package/ccfonts.sty.ltxml \
	lib/LaTeXML/Package/chancery.sty.ltxml \
	lib/LaTeXML/Package/chapterbib.sty.ltxml \
	lib/LaTeXML/Package/charter.sty.ltxml \
	lib/LaTeXML/Package/chngcntr.sty.ltxml \
	lib/LaTeXML/Package/circuitikz.sty.ltxml \
	lib/LaTeXML/Package/cite.sty.ltxml \
	lib/LaTeXML/Package/citesort.sty.ltxml \
	lib/LaTeXML/Package/cleveref.sty.ltxml \
	lib/LaTeXML/Package/cmbright.sty.ltxml \
	lib/LaTeXML/Package/color.sty.ltxml \
	lib/LaTeXML/Package/colordvi.sty.ltxml \
	lib/LaTeXML/Package/colortbl.sty.ltxml \
	lib/LaTeXML/Package/comment.sty.ltxml \
	lib/LaTeXML/Package/concmath.sty.ltxml \
	lib/LaTeXML/Package/courier.sty.ltxml \
	lib/LaTeXML/Package/cp852.def.ltxml \
	lib/LaTeXML/Package/crop.sty.ltxml \
	lib/LaTeXML/Package/cropmark.sty.ltxml \
	lib/LaTeXML/Package/csquotes.def.ltxml \
	lib/LaTeXML/Package/csquotes.sty.ltxml \
	lib/LaTeXML/Package/dcolumn.sty.ltxml \
	lib/LaTeXML/Package/deluxetable.sty.ltxml \
	lib/LaTeXML/Package/diagbox.sty.ltxml \
	lib/LaTeXML/Package/ding.fontmap.ltxml \
	lib/LaTeXML/Package/doi.sty.ltxml \
	lib/LaTeXML/Package/doublespace.sty.ltxml \
	lib/LaTeXML/Package/dsfont.sty.ltxml \
	lib/LaTeXML/Package/eTeX.pool.ltxml \
	lib/LaTeXML/Package/ed.sty.ltxml \
	lib/LaTeXML/Package/ellipsis.sty.ltxml \
	lib/LaTeXML/Package/elsart.cls.ltxml \
	lib/LaTeXML/Package/elsart.sty.ltxml \
	lib/LaTeXML/Package/elsart_support.sty.ltxml \
	lib/LaTeXML/Package/elsart_support_core.sty.ltxml \
	lib/LaTeXML/Package/elsarticle.cls.ltxml \
	lib/LaTeXML/Package/empheq.sty.ltxml \
	lib/LaTeXML/Package/emulateapj.cls.ltxml \
	lib/LaTeXML/Package/emulateapj.sty.ltxml \
	lib/LaTeXML/Package/emulateapj5.sty.ltxml \
	lib/LaTeXML/Package/endnotes.sty.ltxml \
	lib/LaTeXML/Package/english.sty.ltxml \
	lib/LaTeXML/Package/enumerate.sty.ltxml \
	lib/LaTeXML/Package/enumitem.sty.ltxml \
	lib/LaTeXML/Package/epigraph.sty.ltxml \
	lib/LaTeXML/Package/epsf.sty.ltxml \
	lib/LaTeXML/Package/epsf.tex.ltxml \
	lib/LaTeXML/Package/epsfig.sty.ltxml \
	lib/LaTeXML/Package/epstopdf.sty.ltxml \
	lib/LaTeXML/Package/esint.sty.ltxml \
	lib/LaTeXML/Package/espcrc.sty.ltxml \
	lib/LaTeXML/Package/etex.sty.ltxml \
	lib/LaTeXML/Package/etoolbox.sty.ltxml \
	lib/LaTeXML/Package/eucal.sty.ltxml \
	lib/LaTeXML/Package/eufrak.sty.ltxml \
	lib/LaTeXML/Package/euler.sty.ltxml \
	lib/LaTeXML/Package/eulervm.sty.ltxml \
	lib/LaTeXML/Package/eurosym.sty.ltxml \
	lib/LaTeXML/Package/euscript.sty.ltxml \
	lib/LaTeXML/Package/expl3.ltx.ltxml \
	lib/LaTeXML/Package/expl3.pool.ltxml \
	lib/LaTeXML/Package/expl3.sty.ltxml \
	lib/LaTeXML/Package/exscale.sty.ltxml \
	lib/LaTeXML/Package/fancybox.sty.ltxml \
	lib/LaTeXML/Package/fancyhdr.sty.ltxml \
	lib/LaTeXML/Package/fancyheadings.sty.ltxml \
	lib/LaTeXML/Package/fancyvrb.sty.ltxml \
	lib/LaTeXML/Package/feynmf.sty.ltxml \
	lib/LaTeXML/Package/filehook.sty.ltxml \
	lib/LaTeXML/Package/fix-cm.sty.ltxml \
	lib/LaTeXML/Package/fixltx2e.sty.ltxml \
	lib/LaTeXML/Package/fixme.sty.ltxml \
	lib/LaTeXML/Package/flafter.sty.ltxml \
	lib/LaTeXML/Package/fleqn.sty.ltxml \
	lib/LaTeXML/Package/float.sty.ltxml \
	lib/LaTeXML/Package/floatfig.sty.ltxml \
	lib/LaTeXML/Package/floatflt.sty.ltxml \
	lib/LaTeXML/Package/floatpag.sty.ltxml \
	lib/LaTeXML/Package/flowchart.sty.ltxml \
	lib/LaTeXML/Package/flushend.sty.ltxml \
	lib/LaTeXML/Package/fontenc.sty.ltxml \
	lib/LaTeXML/Package/fontspec.sty.ltxml \
	lib/LaTeXML/Package/footmisc.sty.ltxml \
	lib/LaTeXML/Package/footnote.sty.ltxml \
	lib/LaTeXML/Package/fourier.sty.ltxml \
	lib/LaTeXML/Package/framed.sty.ltxml \
	lib/LaTeXML/Package/french.ldf.ltxml \
	lib/LaTeXML/Package/frenchb.ldf.ltxml \
	lib/LaTeXML/Package/fullpage.sty.ltxml \
	lib/LaTeXML/Package/gen-j-l.cls.ltxml \
	lib/LaTeXML/Package/gen-m-l.cls.ltxml \
	lib/LaTeXML/Package/gen-p-l.cls.ltxml \
	lib/LaTeXML/Package/gensymb.sty.ltxml \
	lib/LaTeXML/Package/geometry.sty.ltxml \
	lib/LaTeXML/Package/german.sty.ltxml \
	lib/LaTeXML/Package/gettitlestring.sty.ltxml \
	lib/LaTeXML/Package/glossaries.sty.ltxml \
	lib/LaTeXML/Package/graphics.sty.ltxml \
	lib/LaTeXML/Package/graphicx.sty.ltxml \
	lib/LaTeXML/Package/grffile.sty.ltxml \
	lib/LaTeXML/Package/helvet.sty.ltxml \
	lib/LaTeXML/Package/hepunits.sty.ltxml \
	lib/LaTeXML/Package/here.sty.ltxml \
	lib/LaTeXML/Package/hhline.sty.ltxml \
	lib/LaTeXML/Package/html.sty.ltxml \
	lib/LaTeXML/Package/hypcap.sty.ltxml \
	lib/LaTeXML/Package/hyperref.sty.ltxml \
	lib/LaTeXML/Package/hyperxmp.sty.ltxml \
	lib/LaTeXML/Package/icml.sty.ltxml \
	lib/LaTeXML/Package/icml_support.sty.ltxml \
	lib/LaTeXML/Package/ieeeconf.cls.ltxml \
	lib/LaTeXML/Package/ifblk.fontmap.ltxml \
	lib/LaTeXML/Package/ifclk.fontmap.ltxml \
	lib/LaTeXML/Package/ifetex.sty.ltxml \
	lib/LaTeXML/Package/ifgeo.fontmap.ltxml \
	lib/LaTeXML/Package/ifluatex.sty.ltxml \
	lib/LaTeXML/Package/ifpdf.sty.ltxml \
	lib/LaTeXML/Package/ifplatform.sty.ltxml \
	lib/LaTeXML/Package/ifsym.fontmap.ltxml \
	lib/LaTeXML/Package/ifsym.sty.ltxml \
	lib/LaTeXML/Package/iftex.sty.ltxml \
	lib/LaTeXML/Package/ifthen.sty.ltxml \
	lib/LaTeXML/Package/ifvtex.sty.ltxml \
	lib/LaTeXML/Package/ifwea.fontmap.ltxml \
	lib/LaTeXML/Package/ifxetex.sty.ltxml \
	lib/LaTeXML/Package/ijcai.sty.ltxml \
	lib/LaTeXML/Package/import.sty.ltxml \
	lib/LaTeXML/Package/indentfirst.sty.ltxml \
	lib/LaTeXML/Package/infwarerr.sty.ltxml \
	lib/LaTeXML/Package/inputenc.sty.ltxml \
	lib/LaTeXML/Package/inst_support.sty.ltxml \
	lib/LaTeXML/Package/intcalc.sty.ltxml \
	lib/LaTeXML/Package/iopams.sty.ltxml \
	lib/LaTeXML/Package/iopart.cls.ltxml \
	lib/LaTeXML/Package/iopart_support.sty.ltxml \
	lib/LaTeXML/Package/jheppub.sty.ltxml \
	lib/LaTeXML/Package/keyval.sty.ltxml \
	lib/LaTeXML/Package/kvdefinekeys.sty.ltxml \
	lib/LaTeXML/Package/kvoptions.sty.ltxml \
	lib/LaTeXML/Package/kvsetkeys.sty.ltxml \
	lib/LaTeXML/Package/l3keys2e.sty.ltxml \
	lib/LaTeXML/Package/lastpage.sty.ltxml \
	lib/LaTeXML/Package/latexml.sty.ltxml \
	lib/LaTeXML/Package/latexsym.sty.ltxml \
	lib/LaTeXML/Package/latin10.def.ltxml \
	lib/LaTeXML/Package/lgr.fontmap.ltxml \
	lib/LaTeXML/Package/lineno.sty.ltxml \
	lib/LaTeXML/Package/lipsum.sty.ltxml \
	lib/LaTeXML/Package/listings.sty.ltxml \
	lib/LaTeXML/Package/listingsutf8.sty.ltxml \
	lib/LaTeXML/Package/llncs.cls.ltxml \
	lib/LaTeXML/Package/lmodern.sty.ltxml \
	lib/LaTeXML/Package/longtable.sty.ltxml \
	lib/LaTeXML/Package/lscape.sty.ltxml \
	lib/LaTeXML/Package/ltxcmds.sty.ltxml \
	lib/LaTeXML/Package/luximono.sty.ltxml \
	lib/LaTeXML/Package/lxRDFa.sty.ltxml \
	lib/LaTeXML/Package/ly1.fontmap.ltxml \
	lib/LaTeXML/Package/makecell.sty.ltxml \
	lib/LaTeXML/Package/makeidx.sty.ltxml \
	lib/LaTeXML/Package/marvosym.sty.ltxml \
	lib/LaTeXML/Package/mathabx.sty.ltxml \
	lib/LaTeXML/Package/mathbbol.sty.ltxml \
	lib/LaTeXML/Package/mathdots.sty.ltxml \
	lib/LaTeXML/Package/mathpazo.sty.ltxml \
	lib/LaTeXML/Package/mathpple.sty.ltxml \
	lib/LaTeXML/Package/mathptm.sty.ltxml \
	lib/LaTeXML/Package/mathptmx.sty.ltxml \
	lib/LaTeXML/Package/mathrsfs.sty.ltxml \
	lib/LaTeXML/Package/mathtools.sty.ltxml \
	lib/LaTeXML/Package/microtype.sty.ltxml \
	lib/LaTeXML/Package/minimal.cls.ltxml \
	lib/LaTeXML/Package/mleftright.sty.ltxml \
	lib/LaTeXML/Package/mn.cls.ltxml \
	lib/LaTeXML/Package/mn2e.cls.ltxml \
	lib/LaTeXML/Package/mn2e_support.sty.ltxml \
	lib/LaTeXML/Package/mnras.cls.ltxml \
	lib/LaTeXML/Package/moderncv.cls.ltxml \
	lib/LaTeXML/Package/multicol.sty.ltxml \
	lib/LaTeXML/Package/multido.sty.ltxml \
	lib/LaTeXML/Package/multirow.sty.ltxml \
	lib/LaTeXML/Package/nameref.sty.ltxml \
	lib/LaTeXML/Package/natbib.sty.ltxml \
	lib/LaTeXML/Package/neurips.sty.ltxml \
	lib/LaTeXML/Package/newcent.sty.ltxml \
	lib/LaTeXML/Package/newfloat.sty.ltxml \
	lib/LaTeXML/Package/newlfont.sty.ltxml \
	lib/LaTeXML/Package/newtxmath.sty.ltxml \
	lib/LaTeXML/Package/newtxtext.sty.ltxml \
	lib/LaTeXML/Package/ngerman.sty.ltxml \
	lib/LaTeXML/Package/nicefrac.sty.ltxml \
	lib/LaTeXML/Package/nil.ldf.ltxml \
	lib/LaTeXML/Package/nomencl.sty.ltxml \
	lib/LaTeXML/Package/nopageno.sty.ltxml \
	lib/LaTeXML/Package/ntheorem.sty.ltxml \
	lib/LaTeXML/Package/numprint.sty.ltxml \
	lib/LaTeXML/Package/ot4.fontmap.ltxml \
	lib/LaTeXML/Package/overpic.sty.ltxml \
	lib/LaTeXML/Package/palatino.sty.ltxml \
	lib/LaTeXML/Package/paralist.sty.ltxml \
	lib/LaTeXML/Package/parskip.sty.ltxml \
	lib/LaTeXML/Package/pdfTeX.pool.ltxml \
	lib/LaTeXML/Package/pdflscape.sty.ltxml \
	lib/LaTeXML/Package/pdfpages.sty.ltxml \
	lib/LaTeXML/Package/pdfsync.sty.ltxml \
	lib/LaTeXML/Package/pdftexcmds.sty.ltxml \
	lib/LaTeXML/Package/pgf.sty.ltxml \
	lib/LaTeXML/Package/pgfkeys.code.tex.ltxml \
	lib/LaTeXML/Package/pgfmath.code.tex.ltxml \
	lib/LaTeXML/Package/pgfmathcalc.code.tex.ltxml \
	lib/LaTeXML/Package/pgfplots.sty.ltxml \
	lib/LaTeXML/Package/pgfplotstable.sty.ltxml \
	lib/LaTeXML/Package/pgfsys-latexml.def.ltxml \
	lib/LaTeXML/Package/pgfutil-common.tex.ltxml \
	lib/LaTeXML/Package/physics.sty.ltxml \
	lib/LaTeXML/Package/pifont.sty.ltxml \
	lib/LaTeXML/Package/placeins.sty.ltxml \
	lib/LaTeXML/Package/prettyref.sty.ltxml \
	lib/LaTeXML/Package/preview.sty.ltxml \
	lib/LaTeXML/Package/proof.sty.ltxml \
	lib/LaTeXML/Package/proofwiki.sty.ltxml \
	lib/LaTeXML/Package/psfig.sty.ltxml \
	lib/LaTeXML/Package/psfig.tex.ltxml \
	lib/LaTeXML/Package/psfrag.sty.ltxml \
	lib/LaTeXML/Package/pslatex.sty.ltxml \
	lib/LaTeXML/Package/pspicture.sty.ltxml \
	lib/LaTeXML/Package/pst-grad.sty.ltxml \
	lib/LaTeXML/Package/pst-node.sty.ltxml \
	lib/LaTeXML/Package/pstricks.sty.ltxml \
	lib/LaTeXML/Package/pstricks.tex.ltxml \
	lib/LaTeXML/Package/pxfonts.sty.ltxml \
	lib/LaTeXML/Package/pzd.fontmap.ltxml \
	lib/LaTeXML/Package/quantumarticle.cls.ltxml \
	lib/LaTeXML/Package/ragged2e.sty.ltxml \
	lib/LaTeXML/Package/refcount.sty.ltxml \
	lib/LaTeXML/Package/relsize.sty.ltxml \
	lib/LaTeXML/Package/remreset.sty.ltxml \
	lib/LaTeXML/Package/report.cls.ltxml \
	lib/LaTeXML/Package/revsymb.sty.ltxml \
	lib/LaTeXML/Package/revtex.cls.ltxml \
	lib/LaTeXML/Package/revtex.sty.ltxml \
	lib/LaTeXML/Package/revtex3_support.sty.ltxml \
	lib/LaTeXML/Package/revtex4-1.cls.ltxml \
	lib/LaTeXML/Package/revtex4.cls.ltxml \
	lib/LaTeXML/Package/revtex4.sty.ltxml \
	lib/LaTeXML/Package/revtex4_support.sty.ltxml \
	lib/LaTeXML/Package/rotate.sty.ltxml \
	lib/LaTeXML/Package/rotating.sty.ltxml \
	lib/LaTeXML/Package/rsfs.sty.ltxml \
	lib/LaTeXML/Package/scalefnt.sty.ltxml \
	lib/LaTeXML/Package/sectsty.sty.ltxml \
	lib/LaTeXML/Package/setspace.sty.ltxml \
	lib/LaTeXML/Package/showkeys.sty.ltxml \
	lib/LaTeXML/Package/sidecap.sty.ltxml \
	lib/LaTeXML/Package/siunitx.sty.ltxml \
	lib/LaTeXML/Package/slashbox.sty.ltxml \
	lib/LaTeXML/Package/slashed.sty.ltxml \
	lib/LaTeXML/Package/slides.cls.ltxml \
	lib/LaTeXML/Package/soul.sty.ltxml \
	lib/LaTeXML/Package/srcltx.sty.ltxml \
	lib/LaTeXML/Package/standalone.cls.ltxml \
	lib/LaTeXML/Package/standalone.sty.ltxml \
	lib/LaTeXML/Package/stfloats.sty.ltxml \
	lib/LaTeXML/Package/stmaryrd.sty.ltxml \
	lib/LaTeXML/Package/subcaption.sty.ltxml \
	lib/LaTeXML/Package/subeqn.sty.ltxml \
	lib/LaTeXML/Package/subeqnarray.sty.ltxml \
	lib/LaTeXML/Package/subfig.sty.ltxml \
	lib/LaTeXML/Package/subfigure.sty.ltxml \
	lib/LaTeXML/Package/subfiles.cls.ltxml \
	lib/LaTeXML/Package/subfiles.sty.ltxml \
	lib/LaTeXML/Package/subfloat.sty.ltxml \
	lib/LaTeXML/Package/supertabular.sty.ltxml \
	lib/LaTeXML/Package/sv_support.sty.ltxml \
	lib/LaTeXML/Package/svg.sty.ltxml \
	lib/LaTeXML/Package/svjour.cls.ltxml \
	lib/LaTeXML/Package/svjour3.cls.ltxml \
	lib/LaTeXML/Package/svmult.cls.ltxml \
	lib/LaTeXML/Package/t1.fontmap.ltxml \
	lib/LaTeXML/Package/t1enc.def.ltxml \
	lib/LaTeXML/Package/t1enc.sty.ltxml \
	lib/LaTeXML/Package/t2a.fontmap.ltxml \
	lib/LaTeXML/Package/t2b.fontmap.ltxml \
	lib/LaTeXML/Package/t2c.fontmap.ltxml \
	lib/LaTeXML/Package/tablefootnote.sty.ltxml \
	lib/LaTeXML/Package/tabularx.sty.ltxml \
	lib/LaTeXML/Package/tabulary.sty.ltxml \
	lib/LaTeXML/Package/tcilatex.tex.ltxml \
	lib/LaTeXML/Package/tcolorbox.sty.ltxml \
	lib/LaTeXML/Package/textcase.sty.ltxml \
	lib/LaTeXML/Package/textcomp.sty.ltxml \
	lib/LaTeXML/Package/texvc.sty.ltxml \
	lib/LaTeXML/Package/theorem.sty.ltxml \
	lib/LaTeXML/Package/thm-restate.sty.ltxml \
	lib/LaTeXML/Package/thmtools.sty.ltxml \
	lib/LaTeXML/Package/threeparttable.sty.ltxml \
	lib/LaTeXML/Package/tikz-3dplot.sty.ltxml \
	lib/LaTeXML/Package/tikz.sty.ltxml \
	lib/LaTeXML/Package/tikzbricks.sty.ltxml \
	lib/LaTeXML/Package/times.sty.ltxml \
	lib/LaTeXML/Package/titlesec.sty.ltxml \
	lib/LaTeXML/Package/titling.sty.ltxml \
	lib/LaTeXML/Package/tocbibind.sty.ltxml \
	lib/LaTeXML/Package/todonotes.sty.ltxml \
	lib/LaTeXML/Package/tracefnt.sty.ltxml \
	lib/LaTeXML/Package/transparent.sty.ltxml \
	lib/LaTeXML/Package/ts1.fontmap.ltxml \
	lib/LaTeXML/Package/turing.sty.ltxml \
	lib/LaTeXML/Package/twoopt.sty.ltxml \
	lib/LaTeXML/Package/txfonts.sty.ltxml \
	lib/LaTeXML/Package/txtbabel.def.ltxml \
	lib/LaTeXML/Package/type1cm.sty.ltxml \
	lib/LaTeXML/Package/ulem.sty.ltxml \
	lib/LaTeXML/Package/underscore.sty.ltxml \
	lib/LaTeXML/Package/undertilde.sty.ltxml \
	lib/LaTeXML/Package/units.sty.ltxml \
	lib/LaTeXML/Package/upgreek.sty.ltxml \
	lib/LaTeXML/Package/upquote.sty.ltxml \
	lib/LaTeXML/Package/upref.sty.ltxml \
	lib/LaTeXML/Package/url.sty.ltxml \
	lib/LaTeXML/Package/utf8.def.ltxml \
	lib/LaTeXML/Package/utf8x.def.ltxml \
	lib/LaTeXML/Package/utopia.sty.ltxml \
	lib/LaTeXML/Package/varioref.sty.ltxml \
	lib/LaTeXML/Package/varwidth.sty.ltxml \
	lib/LaTeXML/Package/verbatim.sty.ltxml \
	lib/LaTeXML/Package/vmargin.sty.ltxml \
	lib/LaTeXML/Package/wasysym.sty.ltxml \
	lib/LaTeXML/Package/wiki.sty.ltxml \
	lib/LaTeXML/Package/wrapfig.sty.ltxml \
	lib/LaTeXML/Package/xargs.sty.ltxml \
	lib/LaTeXML/Package/xcolor.sty.ltxml \
	lib/LaTeXML/Package/xfrac.sty.ltxml \
	lib/LaTeXML/Package/xkeyval.sty.ltxml \
	lib/LaTeXML/Package/xkvview.sty.ltxml \
	lib/LaTeXML/Package/xparse.sty.ltxml \
	lib/LaTeXML/Package/xspace.sty.ltxml \
	lib/LaTeXML/Package/xunicode.sty.ltxml \
	lib/LaTeXML/Package/xurl.sty.ltxml \
	lib/LaTeXML/Package/xy.sty.ltxml \
	lib/LaTeXML/Package/xy.tex.ltxml \
	lib/LaTeXML/Package/xylatexml.tex.ltxml \
	lib/LaTeXML/Package/xypic.sty.ltxml \
	lib/LaTeXML/Package/xypic.tex.ltxml \
	lib/LaTeXML/Package/yfonts.sty.ltxml \
	lib/LaTeXML/Post.pm \
	lib/LaTeXML/Post/Collector.pm \
	lib/LaTeXML/Post/CrossRef.pm \
	lib/LaTeXML/Post/Graphics.pm \
	lib/LaTeXML/Post/LaTeXImages.pm \
	lib/LaTeXML/Post/LexMath.pm \
	lib/LaTeXML/Post/MakeBibliography.pm \
	lib/LaTeXML/Post/MakeIndex.pm \
	lib/LaTeXML/Post/Manifest.pm \
	lib/LaTeXML/Post/Manifest/Epub.pm \
	lib/LaTeXML/Post/MathImages.pm \
	lib/LaTeXML/Post/MathML.pm \
	lib/LaTeXML/Post/MathML/Content.pm \
	lib/LaTeXML/Post/MathML/Linebreaker.pm \
	lib/LaTeXML/Post/MathML/OperatorDictionary.pm \
	lib/LaTeXML/Post/MathML/Presentation.pm \
	lib/LaTeXML/Post/OpenMath.pm \
	lib/LaTeXML/Post/PictureImages.pm \
	lib/LaTeXML/Post/SVG.pm \
	lib/LaTeXML/Post/Scan.pm \
	lib/LaTeXML/Post/Split.pm \
	lib/LaTeXML/Post/TeXMath.pm \
	lib/LaTeXML/Post/UnicodeMath.pm \
	lib/LaTeXML/Post/Writer.pm \
	lib/LaTeXML/Post/XMath.pm \
	lib/LaTeXML/Post/XSLT.pm \
	lib/LaTeXML/Pre/BibTeX.pm \
	lib/LaTeXML/Pre/BibTeX/Entry.pm \
	lib/LaTeXML/Util/Geometry.pm \
	lib/LaTeXML/Util/Image.pm \
	lib/LaTeXML/Util/ObjectDB.pm \
	lib/LaTeXML/Util/ObjectDB/Entry.pm \
	lib/LaTeXML/Util/Pack.pm \
	lib/LaTeXML/Util/Pathname.pm \
	lib/LaTeXML/Util/Radix.pm \
	lib/LaTeXML/Util/Test.pm \
	lib/LaTeXML/Util/Transform.pm \
	lib/LaTeXML/Util/Unicode.pm \
	lib/LaTeXML/Util/WWW.pm \
	lib/LaTeXML/resources/CSS/LaTeXML-blue.css \
	lib/LaTeXML/resources/CSS/LaTeXML-epub.css \
	lib/LaTeXML/resources/CSS/LaTeXML-marginpar.css \
	lib/LaTeXML/resources/CSS/LaTeXML-navbar-left.css \
	lib/LaTeXML/resources/CSS/LaTeXML-navbar-right.css \
	lib/LaTeXML/resources/CSS/LaTeXML.css \
	lib/LaTeXML/resources/CSS/ltx-amsart.css \
	lib/LaTeXML/resources/CSS/ltx-apj.css \
	lib/LaTeXML/resources/CSS/ltx-article.css \
	lib/LaTeXML/resources/CSS/ltx-book.css \
	lib/LaTeXML/resources/CSS/ltx-cv.css \
	lib/LaTeXML/resources/CSS/ltx-listings.css \
	lib/LaTeXML/resources/CSS/ltx-report.css \
	lib/LaTeXML/resources/CSS/ltx-svjour.css \
	lib/LaTeXML/resources/CSS/ltx-ulem.css \
	lib/LaTeXML/resources/Profiles/fragment-html.opt \
	lib/LaTeXML/resources/Profiles/fragment-xhtml.opt \
	lib/LaTeXML/resources/Profiles/fragment.opt \
	lib/LaTeXML/resources/Profiles/math.opt \
	lib/LaTeXML/resources/Profiles/modern.opt \
	lib/LaTeXML/resources/Profiles/standard.opt \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-bib.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-bib.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-block.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-block.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-common.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-common.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-inline.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-inline.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-math.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-math.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-meta.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-meta.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-misc.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-misc.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-para.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-para.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-picture.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-picture.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-structure.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-structure.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-tabular.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML-tabular.rng \
	lib/LaTeXML/resources/RelaxNG/LaTeXML.model \
	lib/LaTeXML/resources/RelaxNG/LaTeXML.rnc \
	lib/LaTeXML/resources/RelaxNG/LaTeXML.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-animation.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-animation.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-animevents-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-animevents-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-clip.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-clip.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-filter.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-filter.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-font.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-font.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-graphics-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-graphics-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-structure.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-structure.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-text.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-basic-text.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-clip.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-clip.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-conditional.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-conditional.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-container-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-container-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-core-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-core-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-cursor.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-cursor.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-datatypes.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-datatypes.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-docevents-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-docevents-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-extensibility.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-extensibility.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-extresources-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-extresources-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-filter.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-filter.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-font.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-font.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-gradient.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-gradient.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-graphevents-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-graphevents-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-graphics-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-graphics-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-hyperlink.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-hyperlink.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-image.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-image.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-marker.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-marker.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-mask.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-mask.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-opacity-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-opacity-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-paint-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-paint-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-pattern.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-pattern.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-profile.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-profile.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-script.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-script.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-shape.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-shape.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-structure.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-structure.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-style.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-style.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-text.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-text.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-view.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-view.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-viewport-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-viewport-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg-xlink-attrib.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg-xlink-attrib.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg11-inc.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg11-inc.rng \
	lib/LaTeXML/resources/RelaxNG/svg/svg11.rnc \
	lib/LaTeXML/resources/RelaxNG/svg/svg11.rng \
	lib/LaTeXML/resources/XSLT/LaTeXML-all-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-bib-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-block-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-common.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-epub3.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-html4.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-html5.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-inline-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-jats.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-math-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-meta-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-misc-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-para-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-picture-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-structure-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-tabular-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-tei.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-webpage-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-xhtml.xsl \
	lib/LaTeXML/resources/XSLT/LaTeXML-xhtml5.xsl \
	lib/LaTeXML/resources/javascript/LaTeXML-maybeMathjax.js \
	lib/LaTeXML/texmf/latexml.sty \
	lib/LaTeXML/texmf/lxRDFa.sty


# --- MakeMaker platform_constants section:
MM_Unix_VERSION = 7.70
PERL_MALLOC_DEF = -DPERL_EXTMALLOC_DEF -Dmalloc=Perl_malloc -Dfree=Perl_mfree -Drealloc=Perl_realloc -Dcalloc=Perl_calloc


# --- MakeMaker tool_autosplit section:
# Usage: $(AUTOSPLITFILE) FileToSplit AutoDirToSplitInto
AUTOSPLITFILE = $(ABSPERLRUN)  -e 'use AutoSplit;  autosplit($$$$ARGV[0], $$$$ARGV[1], 0, 1, 1)' --



# --- MakeMaker tool_xsubpp section:


# --- MakeMaker tools_other section:
SHELL = /bin/sh
CHMOD = chmod
CP = cp
MV = mv
NOOP = $(TRUE)
NOECHO = @
RM_F = rm -f
RM_RF = rm -rf
TEST_F = test -f
TOUCH = touch
UMASK_NULL = umask 0
DEV_NULL = > /dev/null 2>&1
MKPATH = $(ABSPERLRUN) -MExtUtils::Command -e 'mkpath' --
EQUALIZE_TIMESTAMP = $(ABSPERLRUN) -MExtUtils::Command -e 'eqtime' --
FALSE = false
TRUE = true
ECHO = echo
ECHO_N = echo -n
UNINST = 0
VERBINST = 0
MOD_INSTALL = $(ABSPERLRUN) -MExtUtils::Install -e 'install([ from_to => {@ARGV}, verbose => '\''$(VERBINST)'\'', uninstall_shadows => '\''$(UNINST)'\'', dir_mode => '\''$(PERM_DIR)'\'' ]);' --
DOC_INSTALL = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'perllocal_install' --
UNINSTALL = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'uninstall' --
WARN_IF_OLD_PACKLIST = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'warn_if_old_packlist' --
MACROSTART = 
MACROEND = 
USEMAKEFILE = -f
FIXIN = $(ABSPERLRUN) -MExtUtils::MY -e 'MY->fixin(shift)' --
CP_NONEMPTY = $(ABSPERLRUN) -MExtUtils::Command::MM -e 'cp_nonempty' --


# --- MakeMaker makemakerdflt section:
makemakerdflt : all
	$(NOECHO) $(NOOP)


# --- MakeMaker dist section:
TAR = tar
TARFLAGS = cvf
ZIP = zip
ZIPFLAGS = -r
COMPRESS = gzip --best
SUFFIX = .gz
SHAR = shar
PREOP = $(NOECHO) $(NOOP)
POSTOP = $(NOECHO) $(NOOP)
TO_UNIX = $(NOECHO) $(NOOP)
CI = ci -u
RCS_LABEL = rcs -Nv$(VERSION_SYM): -q
DIST_CP = best
DIST_DEFAULT = tardist
DISTNAME = LaTeXML
DISTVNAME = LaTeXML-0.8.7


# --- MakeMaker macro section:
DESTINSTALLTEXMFBASEDIR = $(DESTDIR)$(INSTALLTEXMFBASEDIR)
DESTINSTALLTEXMFDIR = $(DESTDIR)$(INSTALLTEXMFDIR)
INSTALLTEXMFBASEDIR = $TEXMFLOCAL
INSTALLTEXMFDIR = $TEXMFLOCAL/tex/latex/latexml
INST_TEXMFDIR = $(INST_LIB)/LaTeXML/texmf
RECORD_REVISION = $(PERLRUN) -pe "s@__REVISION__@$(REVISION)@" 
REVISION_BASE = /data/luojw/nogut/LaTeXML-0.8.7
REVISION_FILE = $(INST_LIBDIR)/LaTeXML/Version.pm


# --- MakeMaker depend section:


# --- MakeMaker cflags section:


# --- MakeMaker const_loadlibs section:


# --- MakeMaker const_cccmd section:


# --- MakeMaker post_constants section:


# --- MakeMaker pasthru section:

PASTHRU = LIBPERL_A="$(LIBPERL_A)"\
	LINKTYPE="$(LINKTYPE)"\
	PREFIX="$(PREFIX)"\
	PASTHRU_DEFINE='$(DEFINE) $(PASTHRU_DEFINE)'\
	PASTHRU_INC='$(INC) $(PASTHRU_INC)'


# --- MakeMaker special_targets section:
.SUFFIXES : .xs .c .C .cpp .i .s .cxx .cc $(OBJ_EXT)

.PHONY: all config static dynamic test linkext manifest blibdirs clean realclean disttest distdir pure_all subdirs clean_subdirs makemakerdflt manifypods realclean_subdirs subdirs_dynamic subdirs_pure_nolink subdirs_static subdirs-test_dynamic subdirs-test_static test_dynamic test_static



# --- MakeMaker c_o section:


# --- MakeMaker xs_c section:


# --- MakeMaker xs_o section:


# --- MakeMaker top_targets section:
all :: pure_all manifypods
	$(NOECHO) $(NOOP)

pure_all :: config pm_to_blib subdirs linkext
	$(NOECHO) $(NOOP)

subdirs :: $(MYEXTLIB)
	$(NOECHO) $(NOOP)

config :: $(FIRST_MAKEFILE) blibdirs
	$(NOECHO) $(NOOP)

help :
	perldoc ExtUtils::MakeMaker


# --- MakeMaker blibdirs section:
blibdirs : $(INST_LIBDIR)$(DFSEP).exists $(INST_ARCHLIB)$(DFSEP).exists $(INST_AUTODIR)$(DFSEP).exists $(INST_ARCHAUTODIR)$(DFSEP).exists $(INST_BIN)$(DFSEP).exists $(INST_SCRIPT)$(DFSEP).exists $(INST_MAN1DIR)$(DFSEP).exists $(INST_MAN3DIR)$(DFSEP).exists
	$(NOECHO) $(NOOP)

# Backwards compat with 6.18 through 6.25
blibdirs.ts : blibdirs
	$(NOECHO) $(NOOP)

$(INST_LIBDIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_LIBDIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_LIBDIR)
	$(NOECHO) $(TOUCH) $(INST_LIBDIR)$(DFSEP).exists

$(INST_ARCHLIB)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_ARCHLIB)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_ARCHLIB)
	$(NOECHO) $(TOUCH) $(INST_ARCHLIB)$(DFSEP).exists

$(INST_AUTODIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_AUTODIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_AUTODIR)
	$(NOECHO) $(TOUCH) $(INST_AUTODIR)$(DFSEP).exists

$(INST_ARCHAUTODIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_ARCHAUTODIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_ARCHAUTODIR)
	$(NOECHO) $(TOUCH) $(INST_ARCHAUTODIR)$(DFSEP).exists

$(INST_BIN)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_BIN)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_BIN)
	$(NOECHO) $(TOUCH) $(INST_BIN)$(DFSEP).exists

$(INST_SCRIPT)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_SCRIPT)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_SCRIPT)
	$(NOECHO) $(TOUCH) $(INST_SCRIPT)$(DFSEP).exists

$(INST_MAN1DIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_MAN1DIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_MAN1DIR)
	$(NOECHO) $(TOUCH) $(INST_MAN1DIR)$(DFSEP).exists

$(INST_MAN3DIR)$(DFSEP).exists :: Makefile.PL
	$(NOECHO) $(MKPATH) $(INST_MAN3DIR)
	$(NOECHO) $(CHMOD) $(PERM_DIR) $(INST_MAN3DIR)
	$(NOECHO) $(TOUCH) $(INST_MAN3DIR)$(DFSEP).exists



# --- MakeMaker linkext section:

linkext :: dynamic
	$(NOECHO) $(NOOP)


# --- MakeMaker dlsyms section:


# --- MakeMaker dynamic_bs section:

BOOTSTRAP =


# --- MakeMaker dynamic section:

dynamic :: $(FIRST_MAKEFILE) config $(INST_BOOT) $(INST_DYNAMIC)
	$(NOECHO) $(NOOP)


# --- MakeMaker dynamic_lib section:


# --- MakeMaker static section:

## $(INST_PM) has been moved to the all: target.
## It remains here for awhile to allow for old usage: "make static"
static :: $(FIRST_MAKEFILE) $(INST_STATIC)
	$(NOECHO) $(NOOP)


# --- MakeMaker static_lib section:


# --- MakeMaker manifypods section:

POD2MAN_EXE = $(PERLRUN) "-MExtUtils::Command::MM" -e pod2man "--"
POD2MAN = $(POD2MAN_EXE)


manifypods : pure_all config  \
	bin/latexml \
	bin/latexmlc \
	bin/latexmlfind \
	bin/latexmlmath \
	bin/latexmlpost \
	lib/LaTeXML.pm \
	lib/LaTeXML/Common/Color.pm \
	lib/LaTeXML/Common/Color/Derived.pm \
	lib/LaTeXML/Common/Color/cmy.pm \
	lib/LaTeXML/Common/Color/cmyk.pm \
	lib/LaTeXML/Common/Color/gray.pm \
	lib/LaTeXML/Common/Color/hsb.pm \
	lib/LaTeXML/Common/Color/rgb.pm \
	lib/LaTeXML/Common/Config.pm \
	lib/LaTeXML/Common/Dimension.pm \
	lib/LaTeXML/Common/Error.pm \
	lib/LaTeXML/Common/Float.pm \
	lib/LaTeXML/Common/Font.pm \
	lib/LaTeXML/Common/Glue.pm \
	lib/LaTeXML/Common/Locator.pm \
	lib/LaTeXML/Common/Model.pm \
	lib/LaTeXML/Common/Model/DTD.pm \
	lib/LaTeXML/Common/Model/RelaxNG.pm \
	lib/LaTeXML/Common/Number.pm \
	lib/LaTeXML/Common/Object.pm \
	lib/LaTeXML/Common/XML.pm \
	lib/LaTeXML/Core.pm \
	lib/LaTeXML/Core/Alignment.pm \
	lib/LaTeXML/Core/Array.pm \
	lib/LaTeXML/Core/Box.pm \
	lib/LaTeXML/Core/Comment.pm \
	lib/LaTeXML/Core/Definition.pm \
	lib/LaTeXML/Core/Definition/CharDef.pm \
	lib/LaTeXML/Core/Definition/Conditional.pm \
	lib/LaTeXML/Core/Definition/Constructor.pm \
	lib/LaTeXML/Core/Definition/Expandable.pm \
	lib/LaTeXML/Core/Definition/Primitive.pm \
	lib/LaTeXML/Core/Definition/Register.pm \
	lib/LaTeXML/Core/Document.pm \
	lib/LaTeXML/Core/Gullet.pm \
	lib/LaTeXML/Core/KeyVal.pm \
	lib/LaTeXML/Core/KeyVals.pm \
	lib/LaTeXML/Core/List.pm \
	lib/LaTeXML/Core/Mouth.pm \
	lib/LaTeXML/Core/Mouth/Binding.pm \
	lib/LaTeXML/Core/Mouth/file.pm \
	lib/LaTeXML/Core/Mouth/http.pm \
	lib/LaTeXML/Core/Mouth/https.pm \
	lib/LaTeXML/Core/MuDimension.pm \
	lib/LaTeXML/Core/MuGlue.pm \
	lib/LaTeXML/Core/Pair.pm \
	lib/LaTeXML/Core/PairList.pm \
	lib/LaTeXML/Core/Parameter.pm \
	lib/LaTeXML/Core/Parameters.pm \
	lib/LaTeXML/Core/Rewrite.pm \
	lib/LaTeXML/Core/State.pm \
	lib/LaTeXML/Core/Stomach.pm \
	lib/LaTeXML/Core/Token.pm \
	lib/LaTeXML/Core/Tokens.pm \
	lib/LaTeXML/Core/Whatsit.pm \
	lib/LaTeXML/Global.pm \
	lib/LaTeXML/MathParser.pm \
	lib/LaTeXML/Package.pm \
	lib/LaTeXML/Post.pm \
	lib/LaTeXML/Post/MathML.pm \
	lib/LaTeXML/Post/UnicodeMath.pm \
	lib/LaTeXML/Pre/BibTeX.pm \
	lib/LaTeXML/Util/Pack.pm \
	lib/LaTeXML/Util/Pathname.pm \
	lib/LaTeXML/Util/Radix.pm \
	lib/LaTeXML/Util/Unicode.pm \
	lib/LaTeXML/Util/WWW.pm
	$(NOECHO) $(POD2MAN) --section=$(MAN1SECTION) --perm_rw=$(PERM_RW) -u \
	  bin/latexml $(INST_MAN1DIR)/latexml.$(MAN1EXT) \
	  bin/latexmlc $(INST_MAN1DIR)/latexmlc.$(MAN1EXT) \
	  bin/latexmlfind $(INST_MAN1DIR)/latexmlfind.$(MAN1EXT) \
	  bin/latexmlmath $(INST_MAN1DIR)/latexmlmath.$(MAN1EXT) \
	  bin/latexmlpost $(INST_MAN1DIR)/latexmlpost.$(MAN1EXT) 
	$(NOECHO) $(POD2MAN) --section=$(MAN3SECTION) --perm_rw=$(PERM_RW) -u \
	  lib/LaTeXML.pm $(INST_MAN3DIR)/LaTeXML.$(MAN3EXT) \
	  lib/LaTeXML/Common/Color.pm $(INST_MAN3DIR)/LaTeXML::Common::Color.$(MAN3EXT) \
	  lib/LaTeXML/Common/Color/Derived.pm $(INST_MAN3DIR)/LaTeXML::Common::Color::Derived.$(MAN3EXT) \
	  lib/LaTeXML/Common/Color/cmy.pm $(INST_MAN3DIR)/LaTeXML::Common::Color::cmy.$(MAN3EXT) \
	  lib/LaTeXML/Common/Color/cmyk.pm $(INST_MAN3DIR)/LaTeXML::Common::Color::cmyk.$(MAN3EXT) \
	  lib/LaTeXML/Common/Color/gray.pm $(INST_MAN3DIR)/LaTeXML::Common::Color::gray.$(MAN3EXT) \
	  lib/LaTeXML/Common/Color/hsb.pm $(INST_MAN3DIR)/LaTeXML::Common::Color::hsb.$(MAN3EXT) \
	  lib/LaTeXML/Common/Color/rgb.pm $(INST_MAN3DIR)/LaTeXML::Common::Color::rgb.$(MAN3EXT) \
	  lib/LaTeXML/Common/Config.pm $(INST_MAN3DIR)/LaTeXML::Common::Config.$(MAN3EXT) \
	  lib/LaTeXML/Common/Dimension.pm $(INST_MAN3DIR)/LaTeXML::Common::Dimension.$(MAN3EXT) \
	  lib/LaTeXML/Common/Error.pm $(INST_MAN3DIR)/LaTeXML::Common::Error.$(MAN3EXT) \
	  lib/LaTeXML/Common/Float.pm $(INST_MAN3DIR)/LaTeXML::Common::Float.$(MAN3EXT) \
	  lib/LaTeXML/Common/Font.pm $(INST_MAN3DIR)/LaTeXML::Common::Font.$(MAN3EXT) \
	  lib/LaTeXML/Common/Glue.pm $(INST_MAN3DIR)/LaTeXML::Common::Glue.$(MAN3EXT) \
	  lib/LaTeXML/Common/Locator.pm $(INST_MAN3DIR)/LaTeXML::Common::Locator.$(MAN3EXT) \
	  lib/LaTeXML/Common/Model.pm $(INST_MAN3DIR)/LaTeXML::Common::Model.$(MAN3EXT) \
	  lib/LaTeXML/Common/Model/DTD.pm $(INST_MAN3DIR)/LaTeXML::Common::Model::DTD.$(MAN3EXT) \
	  lib/LaTeXML/Common/Model/RelaxNG.pm $(INST_MAN3DIR)/LaTeXML::Common::Model::RelaxNG.$(MAN3EXT) \
	  lib/LaTeXML/Common/Number.pm $(INST_MAN3DIR)/LaTeXML::Common::Number.$(MAN3EXT) \
	  lib/LaTeXML/Common/Object.pm $(INST_MAN3DIR)/LaTeXML::Common::Object.$(MAN3EXT) \
	  lib/LaTeXML/Common/XML.pm $(INST_MAN3DIR)/LaTeXML::Common::XML.$(MAN3EXT) \
	  lib/LaTeXML/Core.pm $(INST_MAN3DIR)/LaTeXML::Core.$(MAN3EXT) \
	  lib/LaTeXML/Core/Alignment.pm $(INST_MAN3DIR)/LaTeXML::Core::Alignment.$(MAN3EXT) \
	  lib/LaTeXML/Core/Array.pm $(INST_MAN3DIR)/LaTeXML::Core::Array.$(MAN3EXT) \
	  lib/LaTeXML/Core/Box.pm $(INST_MAN3DIR)/LaTeXML::Core::Box.$(MAN3EXT) \
	  lib/LaTeXML/Core/Comment.pm $(INST_MAN3DIR)/LaTeXML::Core::Comment.$(MAN3EXT) \
	  lib/LaTeXML/Core/Definition.pm $(INST_MAN3DIR)/LaTeXML::Core::Definition.$(MAN3EXT) \
	  lib/LaTeXML/Core/Definition/CharDef.pm $(INST_MAN3DIR)/LaTeXML::Core::Definition::CharDef.$(MAN3EXT) \
	  lib/LaTeXML/Core/Definition/Conditional.pm $(INST_MAN3DIR)/LaTeXML::Core::Definition::Conditional.$(MAN3EXT) \
	  lib/LaTeXML/Core/Definition/Constructor.pm $(INST_MAN3DIR)/LaTeXML::Core::Definition::Constructor.$(MAN3EXT) \
	  lib/LaTeXML/Core/Definition/Expandable.pm $(INST_MAN3DIR)/LaTeXML::Core::Definition::Expandable.$(MAN3EXT) 
	$(NOECHO) $(POD2MAN) --section=$(MAN3SECTION) --perm_rw=$(PERM_RW) -u \
	  lib/LaTeXML/Core/Definition/Primitive.pm $(INST_MAN3DIR)/LaTeXML::Core::Definition::Primitive.$(MAN3EXT) \
	  lib/LaTeXML/Core/Definition/Register.pm $(INST_MAN3DIR)/LaTeXML::Core::Definition::Register.$(MAN3EXT) \
	  lib/LaTeXML/Core/Document.pm $(INST_MAN3DIR)/LaTeXML::Core::Document.$(MAN3EXT) \
	  lib/LaTeXML/Core/Gullet.pm $(INST_MAN3DIR)/LaTeXML::Core::Gullet.$(MAN3EXT) \
	  lib/LaTeXML/Core/KeyVal.pm $(INST_MAN3DIR)/LaTeXML::Core::KeyVal.$(MAN3EXT) \
	  lib/LaTeXML/Core/KeyVals.pm $(INST_MAN3DIR)/LaTeXML::Core::KeyVals.$(MAN3EXT) \
	  lib/LaTeXML/Core/List.pm $(INST_MAN3DIR)/LaTeXML::Core::List.$(MAN3EXT) \
	  lib/LaTeXML/Core/Mouth.pm $(INST_MAN3DIR)/LaTeXML::Core::Mouth.$(MAN3EXT) \
	  lib/LaTeXML/Core/Mouth/Binding.pm $(INST_MAN3DIR)/LaTeXML::Core::Mouth::Binding.$(MAN3EXT) \
	  lib/LaTeXML/Core/Mouth/file.pm $(INST_MAN3DIR)/LaTeXML::Core::Mouth::file.$(MAN3EXT) \
	  lib/LaTeXML/Core/Mouth/http.pm $(INST_MAN3DIR)/LaTeXML::Core::Mouth::http.$(MAN3EXT) \
	  lib/LaTeXML/Core/Mouth/https.pm $(INST_MAN3DIR)/LaTeXML::Core::Mouth::https.$(MAN3EXT) \
	  lib/LaTeXML/Core/MuDimension.pm $(INST_MAN3DIR)/LaTeXML::Core::MuDimension.$(MAN3EXT) \
	  lib/LaTeXML/Core/MuGlue.pm $(INST_MAN3DIR)/LaTeXML::Core::MuGlue.$(MAN3EXT) \
	  lib/LaTeXML/Core/Pair.pm $(INST_MAN3DIR)/LaTeXML::Core::Pair.$(MAN3EXT) \
	  lib/LaTeXML/Core/PairList.pm $(INST_MAN3DIR)/LaTeXML::Core::PairList.$(MAN3EXT) \
	  lib/LaTeXML/Core/Parameter.pm $(INST_MAN3DIR)/LaTeXML::Core::Parameter.$(MAN3EXT) \
	  lib/LaTeXML/Core/Parameters.pm $(INST_MAN3DIR)/LaTeXML::Core::Parameters.$(MAN3EXT) \
	  lib/LaTeXML/Core/Rewrite.pm $(INST_MAN3DIR)/LaTeXML::Core::Rewrite.$(MAN3EXT) \
	  lib/LaTeXML/Core/State.pm $(INST_MAN3DIR)/LaTeXML::Core::State.$(MAN3EXT) \
	  lib/LaTeXML/Core/Stomach.pm $(INST_MAN3DIR)/LaTeXML::Core::Stomach.$(MAN3EXT) \
	  lib/LaTeXML/Core/Token.pm $(INST_MAN3DIR)/LaTeXML::Core::Token.$(MAN3EXT) \
	  lib/LaTeXML/Core/Tokens.pm $(INST_MAN3DIR)/LaTeXML::Core::Tokens.$(MAN3EXT) \
	  lib/LaTeXML/Core/Whatsit.pm $(INST_MAN3DIR)/LaTeXML::Core::Whatsit.$(MAN3EXT) \
	  lib/LaTeXML/Global.pm $(INST_MAN3DIR)/LaTeXML::Global.$(MAN3EXT) \
	  lib/LaTeXML/MathParser.pm $(INST_MAN3DIR)/LaTeXML::MathParser.$(MAN3EXT) \
	  lib/LaTeXML/Package.pm $(INST_MAN3DIR)/LaTeXML::Package.$(MAN3EXT) \
	  lib/LaTeXML/Post.pm $(INST_MAN3DIR)/LaTeXML::Post.$(MAN3EXT) \
	  lib/LaTeXML/Post/MathML.pm $(INST_MAN3DIR)/LaTeXML::Post::MathML.$(MAN3EXT) \
	  lib/LaTeXML/Post/UnicodeMath.pm $(INST_MAN3DIR)/LaTeXML::Post::UnicodeMath.$(MAN3EXT) \
	  lib/LaTeXML/Pre/BibTeX.pm $(INST_MAN3DIR)/LaTeXML::Pre::BibTeX.$(MAN3EXT) \
	  lib/LaTeXML/Util/Pack.pm $(INST_MAN3DIR)/LaTeXML::Util::Pack.$(MAN3EXT) \
	  lib/LaTeXML/Util/Pathname.pm $(INST_MAN3DIR)/LaTeXML::Util::Pathname.$(MAN3EXT) 
	$(NOECHO) $(POD2MAN) --section=$(MAN3SECTION) --perm_rw=$(PERM_RW) -u \
	  lib/LaTeXML/Util/Radix.pm $(INST_MAN3DIR)/LaTeXML::Util::Radix.$(MAN3EXT) \
	  lib/LaTeXML/Util/Unicode.pm $(INST_MAN3DIR)/LaTeXML::Util::Unicode.$(MAN3EXT) \
	  lib/LaTeXML/Util/WWW.pm $(INST_MAN3DIR)/LaTeXML::Util::WWW.$(MAN3EXT) 




# --- MakeMaker processPL section:


# --- MakeMaker installbin section:

EXE_FILES = bin/latexml bin/latexmlc bin/latexmlfind bin/latexmlmath bin/latexmlpost

pure_all :: $(INST_SCRIPT)/latexml $(INST_SCRIPT)/latexmlc $(INST_SCRIPT)/latexmlfind $(INST_SCRIPT)/latexmlmath $(INST_SCRIPT)/latexmlpost
	$(NOECHO) $(NOOP)

realclean ::
	$(RM_F) \
	  $(INST_SCRIPT)/latexml $(INST_SCRIPT)/latexmlc \
	  $(INST_SCRIPT)/latexmlfind $(INST_SCRIPT)/latexmlmath \
	  $(INST_SCRIPT)/latexmlpost 

$(INST_SCRIPT)/latexml : bin/latexml $(FIRST_MAKEFILE) $(INST_SCRIPT)$(DFSEP).exists $(INST_BIN)$(DFSEP).exists
	$(NOECHO) $(RM_F) $(INST_SCRIPT)/latexml
	$(CP) bin/latexml $(INST_SCRIPT)/latexml
	$(FIXIN) $(INST_SCRIPT)/latexml
	-$(NOECHO) $(CHMOD) $(PERM_RWX) $(INST_SCRIPT)/latexml

$(INST_SCRIPT)/latexmlc : bin/latexmlc $(FIRST_MAKEFILE) $(INST_SCRIPT)$(DFSEP).exists $(INST_BIN)$(DFSEP).exists
	$(NOECHO) $(RM_F) $(INST_SCRIPT)/latexmlc
	$(CP) bin/latexmlc $(INST_SCRIPT)/latexmlc
	$(FIXIN) $(INST_SCRIPT)/latexmlc
	-$(NOECHO) $(CHMOD) $(PERM_RWX) $(INST_SCRIPT)/latexmlc

$(INST_SCRIPT)/latexmlfind : bin/latexmlfind $(FIRST_MAKEFILE) $(INST_SCRIPT)$(DFSEP).exists $(INST_BIN)$(DFSEP).exists
	$(NOECHO) $(RM_F) $(INST_SCRIPT)/latexmlfind
	$(CP) bin/latexmlfind $(INST_SCRIPT)/latexmlfind
	$(FIXIN) $(INST_SCRIPT)/latexmlfind
	-$(NOECHO) $(CHMOD) $(PERM_RWX) $(INST_SCRIPT)/latexmlfind

$(INST_SCRIPT)/latexmlmath : bin/latexmlmath $(FIRST_MAKEFILE) $(INST_SCRIPT)$(DFSEP).exists $(INST_BIN)$(DFSEP).exists
	$(NOECHO) $(RM_F) $(INST_SCRIPT)/latexmlmath
	$(CP) bin/latexmlmath $(INST_SCRIPT)/latexmlmath
	$(FIXIN) $(INST_SCRIPT)/latexmlmath
	-$(NOECHO) $(CHMOD) $(PERM_RWX) $(INST_SCRIPT)/latexmlmath

$(INST_SCRIPT)/latexmlpost : bin/latexmlpost $(FIRST_MAKEFILE) $(INST_SCRIPT)$(DFSEP).exists $(INST_BIN)$(DFSEP).exists
	$(NOECHO) $(RM_F) $(INST_SCRIPT)/latexmlpost
	$(CP) bin/latexmlpost $(INST_SCRIPT)/latexmlpost
	$(FIXIN) $(INST_SCRIPT)/latexmlpost
	-$(NOECHO) $(CHMOD) $(PERM_RWX) $(INST_SCRIPT)/latexmlpost



# --- MakeMaker subdirs section:

# none

# --- MakeMaker clean_subdirs section:
clean_subdirs :
	$(NOECHO) $(NOOP)


# --- MakeMaker clean section:

# Delete temporary files but do not touch installed files. We don't delete
# the Makefile here so a later make realclean still has a makefile to use.

clean :: clean_subdirs
	- $(RM_F) \
	  $(BASEEXT).bso $(BASEEXT).def \
	  $(BASEEXT).exp $(BASEEXT).x \
	  $(BOOTSTRAP) $(INST_ARCHAUTODIR)/extralibs.all \
	  $(INST_ARCHAUTODIR)/extralibs.ld $(MAKE_APERL_FILE) \
	  *$(LIB_EXT) *$(OBJ_EXT) \
	  *perl.core MYMETA.json \
	  MYMETA.yml blibdirs.ts \
	  core core.*perl.*.? \
	  core.[0-9] core.[0-9][0-9] \
	  core.[0-9][0-9][0-9] core.[0-9][0-9][0-9][0-9] \
	  core.[0-9][0-9][0-9][0-9][0-9] lib$(BASEEXT).def \
	  mon.out perl \
	  perl$(EXE_EXT) perl.exe \
	  perlmain.c pm_to_blib \
	  pm_to_blib.ts so_locations \
	  tmon.out 
	- $(RM_RF) \
	  blib 
	  $(NOECHO) $(RM_F) $(MAKEFILE_OLD)
	- $(MV) $(FIRST_MAKEFILE) $(MAKEFILE_OLD) $(DEV_NULL)


# --- MakeMaker realclean_subdirs section:
# so clean is forced to complete before realclean_subdirs runs
realclean_subdirs : clean
	$(NOECHO) $(NOOP)


# --- MakeMaker realclean section:
# Delete temporary files (via clean) and also delete dist files
realclean purge :: realclean_subdirs
	- $(RM_F) \
	  $(FIRST_MAKEFILE) $(MAKEFILE_OLD) 
	- $(RM_RF) \
	  $(DISTVNAME) 


# --- MakeMaker metafile section:
metafile : create_distdir
	$(NOECHO) $(ECHO) Generating META.yml
	$(NOECHO) $(ECHO) '---' > META_new.yml
	$(NOECHO) $(ECHO) 'abstract: '\''transforms TeX and LaTeX into XML/HTML/MathML'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'author:' >> META_new.yml
	$(NOECHO) $(ECHO) '  - '\''Bruce Miller <bruce.miller@nist.gov>'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  - '\''Deyan Ginev <deyan.ginev@gmail.com>'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'build_requires:' >> META_new.yml
	$(NOECHO) $(ECHO) '  ExtUtils::MakeMaker: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'configure_requires:' >> META_new.yml
	$(NOECHO) $(ECHO) '  version: '\''0.77'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'dynamic_config: 1' >> META_new.yml
	$(NOECHO) $(ECHO) 'generated_by: '\''ExtUtils::MakeMaker version 7.70, CPAN::Meta::Converter version 2.150010'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'license: open_source' >> META_new.yml
	$(NOECHO) $(ECHO) 'meta-spec:' >> META_new.yml
	$(NOECHO) $(ECHO) '  url: http://module-build.sourceforge.net/META-spec-v1.4.html' >> META_new.yml
	$(NOECHO) $(ECHO) '  version: '\''1.4'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'name: LaTeXML' >> META_new.yml
	$(NOECHO) $(ECHO) 'no_index:' >> META_new.yml
	$(NOECHO) $(ECHO) '  directory:' >> META_new.yml
	$(NOECHO) $(ECHO) '    - t' >> META_new.yml
	$(NOECHO) $(ECHO) '    - inc' >> META_new.yml
	$(NOECHO) $(ECHO) 'requires:' >> META_new.yml
	$(NOECHO) $(ECHO) '  Archive::Zip: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  DB_File: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  File::Which: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Getopt::Long: '\''2.37'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  IO::Handle: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  IO::String: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Image::Size: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  JSON::XS: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  LWP: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  MIME::Base64: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Parse::RecDescent: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Pod::Parser: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Test::More: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Text::Unidecode: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  Time::HiRes: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  URI: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  XML::LibXML: '\''1.61'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  XML::LibXSLT: '\''1.58'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  perl: '\''5.010001'\''' >> META_new.yml
	$(NOECHO) $(ECHO) '  version: '\''0'\''' >> META_new.yml
	$(NOECHO) $(ECHO) 'resources:' >> META_new.yml
	$(NOECHO) $(ECHO) '  bugtracker: https://github.com/brucemiller/LaTeXML/issues' >> META_new.yml
	$(NOECHO) $(ECHO) '  repository: https://github.com/brucemiller/LaTeXML.git' >> META_new.yml
	$(NOECHO) $(ECHO) 'version: 0.8.7' >> META_new.yml
	$(NOECHO) $(ECHO) 'x_serialization_backend: '\''CPAN::Meta::YAML version 0.018'\''' >> META_new.yml
	-$(NOECHO) $(MV) META_new.yml $(DISTVNAME)/META.yml
	$(NOECHO) $(ECHO) Generating META.json
	$(NOECHO) $(ECHO) '{' > META_new.json
	$(NOECHO) $(ECHO) '   "abstract" : "transforms TeX and LaTeX into XML/HTML/MathML",' >> META_new.json
	$(NOECHO) $(ECHO) '   "author" : [' >> META_new.json
	$(NOECHO) $(ECHO) '      "Bruce Miller <bruce.miller@nist.gov>",' >> META_new.json
	$(NOECHO) $(ECHO) '      "Deyan Ginev <deyan.ginev@gmail.com>"' >> META_new.json
	$(NOECHO) $(ECHO) '   ],' >> META_new.json
	$(NOECHO) $(ECHO) '   "dynamic_config" : 1,' >> META_new.json
	$(NOECHO) $(ECHO) '   "generated_by" : "ExtUtils::MakeMaker version 7.70, CPAN::Meta::Converter version 2.150010",' >> META_new.json
	$(NOECHO) $(ECHO) '   "license" : [' >> META_new.json
	$(NOECHO) $(ECHO) '      "open_source"' >> META_new.json
	$(NOECHO) $(ECHO) '   ],' >> META_new.json
	$(NOECHO) $(ECHO) '   "meta-spec" : {' >> META_new.json
	$(NOECHO) $(ECHO) '      "url" : "http://search.cpan.org/perldoc?CPAN::Meta::Spec",' >> META_new.json
	$(NOECHO) $(ECHO) '      "version" : 2' >> META_new.json
	$(NOECHO) $(ECHO) '   },' >> META_new.json
	$(NOECHO) $(ECHO) '   "name" : "LaTeXML",' >> META_new.json
	$(NOECHO) $(ECHO) '   "no_index" : {' >> META_new.json
	$(NOECHO) $(ECHO) '      "directory" : [' >> META_new.json
	$(NOECHO) $(ECHO) '         "t",' >> META_new.json
	$(NOECHO) $(ECHO) '         "inc"' >> META_new.json
	$(NOECHO) $(ECHO) '      ]' >> META_new.json
	$(NOECHO) $(ECHO) '   },' >> META_new.json
	$(NOECHO) $(ECHO) '   "prereqs" : {' >> META_new.json
	$(NOECHO) $(ECHO) '      "build" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "requires" : {' >> META_new.json
	$(NOECHO) $(ECHO) '            "ExtUtils::MakeMaker" : "0"' >> META_new.json
	$(NOECHO) $(ECHO) '         }' >> META_new.json
	$(NOECHO) $(ECHO) '      },' >> META_new.json
	$(NOECHO) $(ECHO) '      "configure" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "requires" : {' >> META_new.json
	$(NOECHO) $(ECHO) '            "version" : "0.77"' >> META_new.json
	$(NOECHO) $(ECHO) '         }' >> META_new.json
	$(NOECHO) $(ECHO) '      },' >> META_new.json
	$(NOECHO) $(ECHO) '      "runtime" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "requires" : {' >> META_new.json
	$(NOECHO) $(ECHO) '            "Archive::Zip" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "DB_File" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "File::Which" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Getopt::Long" : "2.37",' >> META_new.json
	$(NOECHO) $(ECHO) '            "IO::Handle" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "IO::String" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Image::Size" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "JSON::XS" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "LWP" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "MIME::Base64" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Parse::RecDescent" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Pod::Parser" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Test::More" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Text::Unidecode" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "Time::HiRes" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "URI" : "0",' >> META_new.json
	$(NOECHO) $(ECHO) '            "XML::LibXML" : "1.61",' >> META_new.json
	$(NOECHO) $(ECHO) '            "XML::LibXSLT" : "1.58",' >> META_new.json
	$(NOECHO) $(ECHO) '            "perl" : "5.010001",' >> META_new.json
	$(NOECHO) $(ECHO) '            "version" : "0"' >> META_new.json
	$(NOECHO) $(ECHO) '         }' >> META_new.json
	$(NOECHO) $(ECHO) '      }' >> META_new.json
	$(NOECHO) $(ECHO) '   },' >> META_new.json
	$(NOECHO) $(ECHO) '   "release_status" : "stable",' >> META_new.json
	$(NOECHO) $(ECHO) '   "resources" : {' >> META_new.json
	$(NOECHO) $(ECHO) '      "bugtracker" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "web" : "https://github.com/brucemiller/LaTeXML/issues"' >> META_new.json
	$(NOECHO) $(ECHO) '      },' >> META_new.json
	$(NOECHO) $(ECHO) '      "repository" : {' >> META_new.json
	$(NOECHO) $(ECHO) '         "type" : "git",' >> META_new.json
	$(NOECHO) $(ECHO) '         "url" : "https://github.com/brucemiller/LaTeXML.git",' >> META_new.json
	$(NOECHO) $(ECHO) '         "web" : "https://github.com/brucemiller/LaTeXML"' >> META_new.json
	$(NOECHO) $(ECHO) '      }' >> META_new.json
	$(NOECHO) $(ECHO) '   },' >> META_new.json
	$(NOECHO) $(ECHO) '   "version" : "0.8.7",' >> META_new.json
	$(NOECHO) $(ECHO) '   "x_serialization_backend" : "JSON::PP version 4.06"' >> META_new.json
	$(NOECHO) $(ECHO) '}' >> META_new.json
	-$(NOECHO) $(MV) META_new.json $(DISTVNAME)/META.json


# --- MakeMaker signature section:
signature :
	cpansign -s


# --- MakeMaker dist_basics section:
distclean :: realclean distcheck
	$(NOECHO) $(NOOP)

distcheck :
	$(PERLRUN) "-MExtUtils::Manifest=fullcheck" -e fullcheck

skipcheck :
	$(PERLRUN) "-MExtUtils::Manifest=skipcheck" -e skipcheck

manifest :
	$(PERLRUN) "-MExtUtils::Manifest=mkmanifest" -e mkmanifest

veryclean : realclean
	$(RM_F) *~ */*~ *.orig */*.orig *.bak */*.bak *.old */*.old



# --- MakeMaker dist_core section:

dist : $(DIST_DEFAULT) $(FIRST_MAKEFILE)
	$(NOECHO) $(ABSPERLRUN) -l -e 'print '\''Warning: Makefile possibly out of date with $(VERSION_FROM)'\''' \
	  -e '    if -e '\''$(VERSION_FROM)'\'' and -M '\''$(VERSION_FROM)'\'' < -M '\''$(FIRST_MAKEFILE)'\'';' --

tardist : $(DISTVNAME).tar$(SUFFIX)
	$(NOECHO) $(NOOP)

uutardist : $(DISTVNAME).tar$(SUFFIX)
	uuencode $(DISTVNAME).tar$(SUFFIX) $(DISTVNAME).tar$(SUFFIX) > $(DISTVNAME).tar$(SUFFIX)_uu
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).tar$(SUFFIX)_uu'

$(DISTVNAME).tar$(SUFFIX) : distdir
	$(PREOP)
	$(TO_UNIX)
	$(TAR) $(TARFLAGS) $(DISTVNAME).tar $(DISTVNAME)
	$(RM_RF) $(DISTVNAME)
	$(COMPRESS) $(DISTVNAME).tar
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).tar$(SUFFIX)'
	$(POSTOP)

zipdist : $(DISTVNAME).zip
	$(NOECHO) $(NOOP)

$(DISTVNAME).zip : distdir
	$(PREOP)
	$(ZIP) $(ZIPFLAGS) $(DISTVNAME).zip $(DISTVNAME)
	$(RM_RF) $(DISTVNAME)
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).zip'
	$(POSTOP)

shdist : distdir
	$(PREOP)
	$(SHAR) $(DISTVNAME) > $(DISTVNAME).shar
	$(RM_RF) $(DISTVNAME)
	$(NOECHO) $(ECHO) 'Created $(DISTVNAME).shar'
	$(POSTOP)


# --- MakeMaker distdir section:
create_distdir :
	$(RM_RF) $(DISTVNAME)
	$(PERLRUN) "-MExtUtils::Manifest=manicopy,maniread" \
		-e "manicopy(maniread(),'$(DISTVNAME)', '$(DIST_CP)');"

distdir : create_distdir distmeta 
	$(NOECHO) $(NOOP)



# --- MakeMaker dist_test section:
disttest : distdir
	cd $(DISTVNAME) && $(ABSPERLRUN) Makefile.PL 
	cd $(DISTVNAME) && $(MAKE) $(PASTHRU)
	cd $(DISTVNAME) && $(MAKE) test $(PASTHRU)



# --- MakeMaker dist_ci section:
ci :
	$(ABSPERLRUN) -MExtUtils::Manifest=maniread -e '@all = sort keys %{ maniread() };' \
	  -e 'print(qq{Executing $(CI) @all\n});' \
	  -e 'system(qq{$(CI) @all}) == 0 or die $$!;' \
	  -e 'print(qq{Executing $(RCS_LABEL) ...\n});' \
	  -e 'system(qq{$(RCS_LABEL) @all}) == 0 or die $$!;' --


# --- MakeMaker distmeta section:
distmeta : create_distdir metafile
	$(NOECHO) cd $(DISTVNAME) && $(ABSPERLRUN) -MExtUtils::Manifest=maniadd -e 'exit unless -e q{META.yml};' \
	  -e 'eval { maniadd({q{META.yml} => q{Module YAML meta-data (added by MakeMaker)}}) }' \
	  -e '    or die "Could not add META.yml to MANIFEST: $${'\''@'\''}"' --
	$(NOECHO) cd $(DISTVNAME) && $(ABSPERLRUN) -MExtUtils::Manifest=maniadd -e 'exit unless -f q{META.json};' \
	  -e 'eval { maniadd({q{META.json} => q{Module JSON meta-data (added by MakeMaker)}}) }' \
	  -e '    or die "Could not add META.json to MANIFEST: $${'\''@'\''}"' --



# --- MakeMaker distsignature section:
distsignature : distmeta
	$(NOECHO) cd $(DISTVNAME) && $(ABSPERLRUN) -MExtUtils::Manifest=maniadd -e 'eval { maniadd({q{SIGNATURE} => q{Public-key signature (added by MakeMaker)}}) }' \
	  -e '    or die "Could not add SIGNATURE to MANIFEST: $${'\''@'\''}"' --
	$(NOECHO) cd $(DISTVNAME) && $(TOUCH) SIGNATURE
	cd $(DISTVNAME) && cpansign -s



# --- MakeMaker install section:

install :: pure_install doc_install
	$(NOECHO) $(NOOP)

install_perl :: pure_perl_install doc_perl_install
	$(NOECHO) $(NOOP)

install_site :: pure_site_install doc_site_install
	$(NOECHO) $(NOOP)

install_vendor :: pure_vendor_install doc_vendor_install
	$(NOECHO) $(NOOP)

pure_install :: pure_$(INSTALLDIRS)_install
	$(NOECHO) $(NOOP)

doc_install :: doc_$(INSTALLDIRS)_install
	$(NOECHO) $(NOOP)

pure__install : pure_site_install
	$(NOECHO) $(ECHO) INSTALLDIRS not defined, defaulting to INSTALLDIRS=site

doc__install : doc_site_install
	$(NOECHO) $(ECHO) INSTALLDIRS not defined, defaulting to INSTALLDIRS=site

pure_perl_install :: all
	$(NOECHO) $(MOD_INSTALL) \
		read "$(PERL_ARCHLIB)/auto/$(FULLEXT)/.packlist" \
		write "$(DESTINSTALLARCHLIB)/auto/$(FULLEXT)/.packlist" \
		"$(INST_LIB)" "$(DESTINSTALLPRIVLIB)" \
		"$(INST_ARCHLIB)" "$(DESTINSTALLARCHLIB)" \
		"$(INST_BIN)" "$(DESTINSTALLBIN)" \
		"$(INST_SCRIPT)" "$(DESTINSTALLSCRIPT)" \
		"$(INST_MAN1DIR)" "$(DESTINSTALLMAN1DIR)" \
		"$(INST_MAN3DIR)" "$(DESTINSTALLMAN3DIR)"
	$(NOECHO) $(WARN_IF_OLD_PACKLIST) \
		"$(SITEARCHEXP)/auto/$(FULLEXT)"


pure_site_install :: all
	$(NOECHO) $(MOD_INSTALL) \
		read "$(SITEARCHEXP)/auto/$(FULLEXT)/.packlist" \
		write "$(DESTINSTALLSITEARCH)/auto/$(FULLEXT)/.packlist" \
		"$(INST_LIB)" "$(DESTINSTALLSITELIB)" \
		"$(INST_ARCHLIB)" "$(DESTINSTALLSITEARCH)" \
		"$(INST_BIN)" "$(DESTINSTALLSITEBIN)" \
		"$(INST_SCRIPT)" "$(DESTINSTALLSITESCRIPT)" \
		"$(INST_MAN1DIR)" "$(DESTINSTALLSITEMAN1DIR)" \
		"$(INST_MAN3DIR)" "$(DESTINSTALLSITEMAN3DIR)"
	$(NOECHO) $(WARN_IF_OLD_PACKLIST) \
		"$(PERL_ARCHLIB)/auto/$(FULLEXT)"

pure_vendor_install :: all
	$(NOECHO) $(MOD_INSTALL) \
		read "$(VENDORARCHEXP)/auto/$(FULLEXT)/.packlist" \
		write "$(DESTINSTALLVENDORARCH)/auto/$(FULLEXT)/.packlist" \
		"$(INST_LIB)" "$(DESTINSTALLVENDORLIB)" \
		"$(INST_ARCHLIB)" "$(DESTINSTALLVENDORARCH)" \
		"$(INST_BIN)" "$(DESTINSTALLVENDORBIN)" \
		"$(INST_SCRIPT)" "$(DESTINSTALLVENDORSCRIPT)" \
		"$(INST_MAN1DIR)" "$(DESTINSTALLVENDORMAN1DIR)" \
		"$(INST_MAN3DIR)" "$(DESTINSTALLVENDORMAN3DIR)"


doc_perl_install :: all
	$(NOECHO) $(ECHO) Appending installation info to "$(DESTINSTALLARCHLIB)/perllocal.pod"
	-$(NOECHO) $(MKPATH) "$(DESTINSTALLARCHLIB)"
	-$(NOECHO) $(DOC_INSTALL) \
		"Module" "$(NAME)" \
		"installed into" "$(INSTALLPRIVLIB)" \
		LINKTYPE "$(LINKTYPE)" \
		VERSION "$(VERSION)" \
		EXE_FILES "$(EXE_FILES)" \
		>> "$(DESTINSTALLARCHLIB)/perllocal.pod"

doc_site_install :: all
	$(NOECHO) $(ECHO) Appending installation info to "$(DESTINSTALLARCHLIB)/perllocal.pod"
	-$(NOECHO) $(MKPATH) "$(DESTINSTALLARCHLIB)"
	-$(NOECHO) $(DOC_INSTALL) \
		"Module" "$(NAME)" \
		"installed into" "$(INSTALLSITELIB)" \
		LINKTYPE "$(LINKTYPE)" \
		VERSION "$(VERSION)" \
		EXE_FILES "$(EXE_FILES)" \
		>> "$(DESTINSTALLARCHLIB)/perllocal.pod"

doc_vendor_install :: all
	$(NOECHO) $(ECHO) Appending installation info to "$(DESTINSTALLARCHLIB)/perllocal.pod"
	-$(NOECHO) $(MKPATH) "$(DESTINSTALLARCHLIB)"
	-$(NOECHO) $(DOC_INSTALL) \
		"Module" "$(NAME)" \
		"installed into" "$(INSTALLVENDORLIB)" \
		LINKTYPE "$(LINKTYPE)" \
		VERSION "$(VERSION)" \
		EXE_FILES "$(EXE_FILES)" \
		>> "$(DESTINSTALLARCHLIB)/perllocal.pod"


uninstall :: uninstall_from_$(INSTALLDIRS)dirs
	$(NOECHO) $(NOOP)

uninstall_from_perldirs ::
	$(NOECHO) $(UNINSTALL) "$(PERL_ARCHLIB)/auto/$(FULLEXT)/.packlist"

uninstall_from_sitedirs ::
	$(NOECHO) $(UNINSTALL) "$(SITEARCHEXP)/auto/$(FULLEXT)/.packlist"

uninstall_from_vendordirs ::
	$(NOECHO) $(UNINSTALL) "$(VENDORARCHEXP)/auto/$(FULLEXT)/.packlist"


# --- MakeMaker force section:
# Phony target to force checking subdirectories.
FORCE :
	$(NOECHO) $(NOOP)


# --- MakeMaker perldepend section:


# --- MakeMaker makefile section:
# We take a very conservative approach here, but it's worth it.
# We move Makefile to Makefile.old here to avoid gnu make looping.
$(FIRST_MAKEFILE) : Makefile.PL $(CONFIGDEP)
	$(NOECHO) $(ECHO) "Makefile out-of-date with respect to $?"
	$(NOECHO) $(ECHO) "Cleaning current config before rebuilding Makefile..."
	-$(NOECHO) $(RM_F) $(MAKEFILE_OLD)
	-$(NOECHO) $(MV)   $(FIRST_MAKEFILE) $(MAKEFILE_OLD)
	- $(MAKE) $(USEMAKEFILE) $(MAKEFILE_OLD) clean $(DEV_NULL)
	$(PERLRUN) Makefile.PL 
	$(NOECHO) $(ECHO) "==> Your Makefile has been rebuilt. <=="
	$(NOECHO) $(ECHO) "==> Please rerun the $(MAKE) command.  <=="
	$(FALSE)



# --- MakeMaker staticmake section:

# --- MakeMaker makeaperl section ---
MAP_TARGET    = perl
FULLPERL      = "/usr/bin/perl"
MAP_PERLINC   = "-Iblib/arch" "-Iblib/lib" "-I/usr/lib64/perl5" "-I/usr/share/perl5"

$(MAP_TARGET) :: $(MAKE_APERL_FILE)
	$(MAKE) $(USEMAKEFILE) $(MAKE_APERL_FILE) $@

$(MAKE_APERL_FILE) : static $(FIRST_MAKEFILE) pm_to_blib
	$(NOECHO) $(ECHO) Writing \"$(MAKE_APERL_FILE)\" for this $(MAP_TARGET)
	$(NOECHO) $(PERLRUNINST) \
		Makefile.PL DIR="" \
		MAKEFILE=$(MAKE_APERL_FILE) LINKTYPE=static \
		MAKEAPERL=1 NORECURS=1 CCCDLFLAGS=


# --- MakeMaker test section:
TEST_VERBOSE=0
TEST_TYPE=test_$(LINKTYPE)
TEST_FILE = test.pl
TEST_FILES = t/*.t
TESTDB_SW = -d

testdb :: testdb_$(LINKTYPE)
	$(NOECHO) $(NOOP)

test :: $(TEST_TYPE)
	$(NOECHO) $(NOOP)

# Occasionally we may face this degenerate target:
test_ : test_dynamic
	$(NOECHO) $(NOOP)

subdirs-test_dynamic :: dynamic pure_all

test_dynamic :: subdirs-test_dynamic
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) "-MExtUtils::Command::MM" "-MTest::Harness" "-e" "undef *Test::Harness::Switches; test_harness($(TEST_VERBOSE), '$(INST_LIB)', '$(INST_ARCHLIB)')" $(TEST_FILES)

testdb_dynamic :: dynamic pure_all
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) $(TESTDB_SW) "-I$(INST_LIB)" "-I$(INST_ARCHLIB)" $(TEST_FILE)

subdirs-test_static :: static pure_all

test_static :: subdirs-test_static
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) "-MExtUtils::Command::MM" "-MTest::Harness" "-e" "undef *Test::Harness::Switches; test_harness($(TEST_VERBOSE), '$(INST_LIB)', '$(INST_ARCHLIB)')" $(TEST_FILES)

testdb_static :: static pure_all
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) $(TESTDB_SW) "-I$(INST_LIB)" "-I$(INST_ARCHLIB)" $(TEST_FILE)



# --- MakeMaker ppd section:
# Creates a PPD (Perl Package Description) for a binary distribution.
ppd :
	$(NOECHO) $(ECHO) '<SOFTPKG NAME="LaTeXML" VERSION="0.8.7">' > LaTeXML.ppd
	$(NOECHO) $(ECHO) '    <ABSTRACT>transforms TeX and LaTeX into XML/HTML/MathML</ABSTRACT>' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '    <AUTHOR>Bruce Miller &lt;bruce.miller@nist.gov&gt;, Deyan Ginev &lt;deyan.ginev@gmail.com&gt;</AUTHOR>' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '    <IMPLEMENTATION>' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <PERLCORE VERSION="5,010001,0,0" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Archive::Zip" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="DB_File::" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="File::Which" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Getopt::Long" VERSION="2.37" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="IO::Handle" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="IO::String" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Image::Size" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="JSON::XS" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="LWP::" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="MIME::Base64" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Parse::RecDescent" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Pod::Parser" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Test::More" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Text::Unidecode" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="Time::HiRes" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="URI::" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="XML::LibXML" VERSION="1.61" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="XML::LibXSLT" VERSION="1.58" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <REQUIRE NAME="version::" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <ARCHITECTURE NAME="x86_64-linux-thread-multi-5.32" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '        <CODEBASE HREF="" />' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '    </IMPLEMENTATION>' >> LaTeXML.ppd
	$(NOECHO) $(ECHO) '</SOFTPKG>' >> LaTeXML.ppd


# --- MakeMaker pm_to_blib section:

pm_to_blib : $(FIRST_MAKEFILE) $(TO_INST_PM)
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML.pm' 'blib/lib/LaTeXML.pm' \
	  'lib/LaTeXML/Common/Color.pm' 'blib/lib/LaTeXML/Common/Color.pm' \
	  'lib/LaTeXML/Common/Color/Derived.pm' 'blib/lib/LaTeXML/Common/Color/Derived.pm' \
	  'lib/LaTeXML/Common/Color/cmy.pm' 'blib/lib/LaTeXML/Common/Color/cmy.pm' \
	  'lib/LaTeXML/Common/Color/cmyk.pm' 'blib/lib/LaTeXML/Common/Color/cmyk.pm' \
	  'lib/LaTeXML/Common/Color/gray.pm' 'blib/lib/LaTeXML/Common/Color/gray.pm' \
	  'lib/LaTeXML/Common/Color/hsb.pm' 'blib/lib/LaTeXML/Common/Color/hsb.pm' \
	  'lib/LaTeXML/Common/Color/rgb.pm' 'blib/lib/LaTeXML/Common/Color/rgb.pm' \
	  'lib/LaTeXML/Common/Config.pm' 'blib/lib/LaTeXML/Common/Config.pm' \
	  'lib/LaTeXML/Common/Dimension.pm' 'blib/lib/LaTeXML/Common/Dimension.pm' \
	  'lib/LaTeXML/Common/Error.pm' 'blib/lib/LaTeXML/Common/Error.pm' \
	  'lib/LaTeXML/Common/Float.pm' 'blib/lib/LaTeXML/Common/Float.pm' \
	  'lib/LaTeXML/Common/Font.pm' 'blib/lib/LaTeXML/Common/Font.pm' \
	  'lib/LaTeXML/Common/Font/Metric.pm' 'blib/lib/LaTeXML/Common/Font/Metric.pm' \
	  'lib/LaTeXML/Common/Font/StandardMetrics.pm' 'blib/lib/LaTeXML/Common/Font/StandardMetrics.pm' \
	  'lib/LaTeXML/Common/Glue.pm' 'blib/lib/LaTeXML/Common/Glue.pm' \
	  'lib/LaTeXML/Common/Locator.pm' 'blib/lib/LaTeXML/Common/Locator.pm' \
	  'lib/LaTeXML/Common/Model.pm' 'blib/lib/LaTeXML/Common/Model.pm' \
	  'lib/LaTeXML/Common/Model/DTD.pm' 'blib/lib/LaTeXML/Common/Model/DTD.pm' \
	  'lib/LaTeXML/Common/Model/RelaxNG.pm' 'blib/lib/LaTeXML/Common/Model/RelaxNG.pm' \
	  'lib/LaTeXML/Common/Number.pm' 'blib/lib/LaTeXML/Common/Number.pm' \
	  'lib/LaTeXML/Common/Object.pm' 'blib/lib/LaTeXML/Common/Object.pm' \
	  'lib/LaTeXML/Common/XML.pm' 'blib/lib/LaTeXML/Common/XML.pm' \
	  'lib/LaTeXML/Common/XML/Parser.pm' 'blib/lib/LaTeXML/Common/XML/Parser.pm' \
	  'lib/LaTeXML/Common/XML/RelaxNG.pm' 'blib/lib/LaTeXML/Common/XML/RelaxNG.pm' \
	  'lib/LaTeXML/Common/XML/XPath.pm' 'blib/lib/LaTeXML/Common/XML/XPath.pm' \
	  'lib/LaTeXML/Common/XML/XSLT.pm' 'blib/lib/LaTeXML/Common/XML/XSLT.pm' \
	  'lib/LaTeXML/Core.pm' 'blib/lib/LaTeXML/Core.pm' \
	  'lib/LaTeXML/Core/Alignment.pm' 'blib/lib/LaTeXML/Core/Alignment.pm' \
	  'lib/LaTeXML/Core/Alignment/Template.pm' 'blib/lib/LaTeXML/Core/Alignment/Template.pm' \
	  'lib/LaTeXML/Core/Array.pm' 'blib/lib/LaTeXML/Core/Array.pm' \
	  'lib/LaTeXML/Core/Box.pm' 'blib/lib/LaTeXML/Core/Box.pm' \
	  'lib/LaTeXML/Core/Comment.pm' 'blib/lib/LaTeXML/Core/Comment.pm' \
	  'lib/LaTeXML/Core/Definition.pm' 'blib/lib/LaTeXML/Core/Definition.pm' \
	  'lib/LaTeXML/Core/Definition/CharDef.pm' 'blib/lib/LaTeXML/Core/Definition/CharDef.pm' \
	  'lib/LaTeXML/Core/Definition/Conditional.pm' 'blib/lib/LaTeXML/Core/Definition/Conditional.pm' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Core/Definition/Constructor.pm' 'blib/lib/LaTeXML/Core/Definition/Constructor.pm' \
	  'lib/LaTeXML/Core/Definition/Constructor/Compiler.pm' 'blib/lib/LaTeXML/Core/Definition/Constructor/Compiler.pm' \
	  'lib/LaTeXML/Core/Definition/Expandable.pm' 'blib/lib/LaTeXML/Core/Definition/Expandable.pm' \
	  'lib/LaTeXML/Core/Definition/Primitive.pm' 'blib/lib/LaTeXML/Core/Definition/Primitive.pm' \
	  'lib/LaTeXML/Core/Definition/Register.pm' 'blib/lib/LaTeXML/Core/Definition/Register.pm' \
	  'lib/LaTeXML/Core/Document.pm' 'blib/lib/LaTeXML/Core/Document.pm' \
	  'lib/LaTeXML/Core/Gullet.pm' 'blib/lib/LaTeXML/Core/Gullet.pm' \
	  'lib/LaTeXML/Core/KeyVal.pm' 'blib/lib/LaTeXML/Core/KeyVal.pm' \
	  'lib/LaTeXML/Core/KeyVals.pm' 'blib/lib/LaTeXML/Core/KeyVals.pm' \
	  'lib/LaTeXML/Core/List.pm' 'blib/lib/LaTeXML/Core/List.pm' \
	  'lib/LaTeXML/Core/Mouth.pm' 'blib/lib/LaTeXML/Core/Mouth.pm' \
	  'lib/LaTeXML/Core/Mouth/Binding.pm' 'blib/lib/LaTeXML/Core/Mouth/Binding.pm' \
	  'lib/LaTeXML/Core/Mouth/file.pm' 'blib/lib/LaTeXML/Core/Mouth/file.pm' \
	  'lib/LaTeXML/Core/Mouth/http.pm' 'blib/lib/LaTeXML/Core/Mouth/http.pm' \
	  'lib/LaTeXML/Core/Mouth/https.pm' 'blib/lib/LaTeXML/Core/Mouth/https.pm' \
	  'lib/LaTeXML/Core/MuDimension.pm' 'blib/lib/LaTeXML/Core/MuDimension.pm' \
	  'lib/LaTeXML/Core/MuGlue.pm' 'blib/lib/LaTeXML/Core/MuGlue.pm' \
	  'lib/LaTeXML/Core/Pair.pm' 'blib/lib/LaTeXML/Core/Pair.pm' \
	  'lib/LaTeXML/Core/PairList.pm' 'blib/lib/LaTeXML/Core/PairList.pm' \
	  'lib/LaTeXML/Core/Parameter.pm' 'blib/lib/LaTeXML/Core/Parameter.pm' \
	  'lib/LaTeXML/Core/Parameters.pm' 'blib/lib/LaTeXML/Core/Parameters.pm' \
	  'lib/LaTeXML/Core/Rewrite.pm' 'blib/lib/LaTeXML/Core/Rewrite.pm' \
	  'lib/LaTeXML/Core/State.pm' 'blib/lib/LaTeXML/Core/State.pm' \
	  'lib/LaTeXML/Core/Stomach.pm' 'blib/lib/LaTeXML/Core/Stomach.pm' \
	  'lib/LaTeXML/Core/Token.pm' 'blib/lib/LaTeXML/Core/Token.pm' \
	  'lib/LaTeXML/Core/Tokens.pm' 'blib/lib/LaTeXML/Core/Tokens.pm' \
	  'lib/LaTeXML/Core/Whatsit.pm' 'blib/lib/LaTeXML/Core/Whatsit.pm' \
	  'lib/LaTeXML/Global.pm' 'blib/lib/LaTeXML/Global.pm' \
	  'lib/LaTeXML/LaTeXML.catalog' 'blib/lib/LaTeXML/LaTeXML.catalog' \
	  'lib/LaTeXML/MathParser.pm' 'blib/lib/LaTeXML/MathParser.pm' \
	  'lib/LaTeXML/Package.pm' 'blib/lib/LaTeXML/Package.pm' \
	  'lib/LaTeXML/Package/AmSTeX.pool.ltxml' 'blib/lib/LaTeXML/Package/AmSTeX.pool.ltxml' \
	  'lib/LaTeXML/Package/BibTeX.pool.ltxml' 'blib/lib/LaTeXML/Package/BibTeX.pool.ltxml' \
	  'lib/LaTeXML/Package/IEEEtran.cls.ltxml' 'blib/lib/LaTeXML/Package/IEEEtran.cls.ltxml' \
	  'lib/LaTeXML/Package/JHEP.cls.ltxml' 'blib/lib/LaTeXML/Package/JHEP.cls.ltxml' \
	  'lib/LaTeXML/Package/JHEP2.cls.ltxml' 'blib/lib/LaTeXML/Package/JHEP2.cls.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/JHEP3.cls.ltxml' 'blib/lib/LaTeXML/Package/JHEP3.cls.ltxml' \
	  'lib/LaTeXML/Package/LaTeX.pool.ltxml' 'blib/lib/LaTeXML/Package/LaTeX.pool.ltxml' \
	  'lib/LaTeXML/Package/OmniBus.cls.ltxml' 'blib/lib/LaTeXML/Package/OmniBus.cls.ltxml' \
	  'lib/LaTeXML/Package/PoS.cls.ltxml' 'blib/lib/LaTeXML/Package/PoS.cls.ltxml' \
	  'lib/LaTeXML/Package/SIunits.sty.ltxml' 'blib/lib/LaTeXML/Package/SIunits.sty.ltxml' \
	  'lib/LaTeXML/Package/TeX.pool.ltxml' 'blib/lib/LaTeXML/Package/TeX.pool.ltxml' \
	  'lib/LaTeXML/Package/a0poster.cls.ltxml' 'blib/lib/LaTeXML/Package/a0poster.cls.ltxml' \
	  'lib/LaTeXML/Package/a0size.sty.ltxml' 'blib/lib/LaTeXML/Package/a0size.sty.ltxml' \
	  'lib/LaTeXML/Package/a4.sty.ltxml' 'blib/lib/LaTeXML/Package/a4.sty.ltxml' \
	  'lib/LaTeXML/Package/a4wide.sty.ltxml' 'blib/lib/LaTeXML/Package/a4wide.sty.ltxml' \
	  'lib/LaTeXML/Package/aa.cls.ltxml' 'blib/lib/LaTeXML/Package/aa.cls.ltxml' \
	  'lib/LaTeXML/Package/aa_support.sty.ltxml' 'blib/lib/LaTeXML/Package/aa_support.sty.ltxml' \
	  'lib/LaTeXML/Package/aas_macros.sty.ltxml' 'blib/lib/LaTeXML/Package/aas_macros.sty.ltxml' \
	  'lib/LaTeXML/Package/aas_support.sty.ltxml' 'blib/lib/LaTeXML/Package/aas_support.sty.ltxml' \
	  'lib/LaTeXML/Package/aasms.sty.ltxml' 'blib/lib/LaTeXML/Package/aasms.sty.ltxml' \
	  'lib/LaTeXML/Package/aaspp.sty.ltxml' 'blib/lib/LaTeXML/Package/aaspp.sty.ltxml' \
	  'lib/LaTeXML/Package/aastex.cls.ltxml' 'blib/lib/LaTeXML/Package/aastex.cls.ltxml' \
	  'lib/LaTeXML/Package/aastex.sty.ltxml' 'blib/lib/LaTeXML/Package/aastex.sty.ltxml' \
	  'lib/LaTeXML/Package/accents.sty.ltxml' 'blib/lib/LaTeXML/Package/accents.sty.ltxml' \
	  'lib/LaTeXML/Package/acmart.cls.ltxml' 'blib/lib/LaTeXML/Package/acmart.cls.ltxml' \
	  'lib/LaTeXML/Package/acronym.sty.ltxml' 'blib/lib/LaTeXML/Package/acronym.sty.ltxml' \
	  'lib/LaTeXML/Package/actuarialangle.sty.ltxml' 'blib/lib/LaTeXML/Package/actuarialangle.sty.ltxml' \
	  'lib/LaTeXML/Package/adjustbox.sty.ltxml' 'blib/lib/LaTeXML/Package/adjustbox.sty.ltxml' \
	  'lib/LaTeXML/Package/ae.sty.ltxml' 'blib/lib/LaTeXML/Package/ae.sty.ltxml' \
	  'lib/LaTeXML/Package/aecompl.sty.ltxml' 'blib/lib/LaTeXML/Package/aecompl.sty.ltxml' \
	  'lib/LaTeXML/Package/afterpage.sty.ltxml' 'blib/lib/LaTeXML/Package/afterpage.sty.ltxml' \
	  'lib/LaTeXML/Package/aipcheck.tex.ltxml' 'blib/lib/LaTeXML/Package/aipcheck.tex.ltxml' \
	  'lib/LaTeXML/Package/aipproc.cls.ltxml' 'blib/lib/LaTeXML/Package/aipproc.cls.ltxml' \
	  'lib/LaTeXML/Package/aipproc.sty.ltxml' 'blib/lib/LaTeXML/Package/aipproc.sty.ltxml' \
	  'lib/LaTeXML/Package/algc.sty.ltxml' 'blib/lib/LaTeXML/Package/algc.sty.ltxml' \
	  'lib/LaTeXML/Package/algcompatible.sty.ltxml' 'blib/lib/LaTeXML/Package/algcompatible.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/algmatlab.sty.ltxml' 'blib/lib/LaTeXML/Package/algmatlab.sty.ltxml' \
	  'lib/LaTeXML/Package/algorithm.sty.ltxml' 'blib/lib/LaTeXML/Package/algorithm.sty.ltxml' \
	  'lib/LaTeXML/Package/algorithm2e.sty.ltxml' 'blib/lib/LaTeXML/Package/algorithm2e.sty.ltxml' \
	  'lib/LaTeXML/Package/algorithmic.sty.ltxml' 'blib/lib/LaTeXML/Package/algorithmic.sty.ltxml' \
	  'lib/LaTeXML/Package/algorithmicx.sty.ltxml' 'blib/lib/LaTeXML/Package/algorithmicx.sty.ltxml' \
	  'lib/LaTeXML/Package/algpascal.sty.ltxml' 'blib/lib/LaTeXML/Package/algpascal.sty.ltxml' \
	  'lib/LaTeXML/Package/algpseudocode.sty.ltxml' 'blib/lib/LaTeXML/Package/algpseudocode.sty.ltxml' \
	  'lib/LaTeXML/Package/alltt.sty.ltxml' 'blib/lib/LaTeXML/Package/alltt.sty.ltxml' \
	  'lib/LaTeXML/Package/ams_core.cls.ltxml' 'blib/lib/LaTeXML/Package/ams_core.cls.ltxml' \
	  'lib/LaTeXML/Package/ams_support.sty.ltxml' 'blib/lib/LaTeXML/Package/ams_support.sty.ltxml' \
	  'lib/LaTeXML/Package/amsa.fontmap.ltxml' 'blib/lib/LaTeXML/Package/amsa.fontmap.ltxml' \
	  'lib/LaTeXML/Package/amsaddr.sty.ltxml' 'blib/lib/LaTeXML/Package/amsaddr.sty.ltxml' \
	  'lib/LaTeXML/Package/amsart.cls.ltxml' 'blib/lib/LaTeXML/Package/amsart.cls.ltxml' \
	  'lib/LaTeXML/Package/amsb.fontmap.ltxml' 'blib/lib/LaTeXML/Package/amsb.fontmap.ltxml' \
	  'lib/LaTeXML/Package/amsbook.cls.ltxml' 'blib/lib/LaTeXML/Package/amsbook.cls.ltxml' \
	  'lib/LaTeXML/Package/amsbsy.sty.ltxml' 'blib/lib/LaTeXML/Package/amsbsy.sty.ltxml' \
	  'lib/LaTeXML/Package/amscd.sty.ltxml' 'blib/lib/LaTeXML/Package/amscd.sty.ltxml' \
	  'lib/LaTeXML/Package/amsfonts.sty.ltxml' 'blib/lib/LaTeXML/Package/amsfonts.sty.ltxml' \
	  'lib/LaTeXML/Package/amsgen.sty.ltxml' 'blib/lib/LaTeXML/Package/amsgen.sty.ltxml' \
	  'lib/LaTeXML/Package/amsmath.sty.ltxml' 'blib/lib/LaTeXML/Package/amsmath.sty.ltxml' \
	  'lib/LaTeXML/Package/amsopn.sty.ltxml' 'blib/lib/LaTeXML/Package/amsopn.sty.ltxml' \
	  'lib/LaTeXML/Package/amsppt.sty.ltxml' 'blib/lib/LaTeXML/Package/amsppt.sty.ltxml' \
	  'lib/LaTeXML/Package/amsproc.cls.ltxml' 'blib/lib/LaTeXML/Package/amsproc.cls.ltxml' \
	  'lib/LaTeXML/Package/amsrefs.sty.ltxml' 'blib/lib/LaTeXML/Package/amsrefs.sty.ltxml' \
	  'lib/LaTeXML/Package/amssymb.sty.ltxml' 'blib/lib/LaTeXML/Package/amssymb.sty.ltxml' \
	  'lib/LaTeXML/Package/amstex.sty.ltxml' 'blib/lib/LaTeXML/Package/amstex.sty.ltxml' \
	  'lib/LaTeXML/Package/amstex.tex.ltxml' 'blib/lib/LaTeXML/Package/amstex.tex.ltxml' \
	  'lib/LaTeXML/Package/amstext.sty.ltxml' 'blib/lib/LaTeXML/Package/amstext.sty.ltxml' \
	  'lib/LaTeXML/Package/amsthm.sty.ltxml' 'blib/lib/LaTeXML/Package/amsthm.sty.ltxml' \
	  'lib/LaTeXML/Package/amsxtra.sty.ltxml' 'blib/lib/LaTeXML/Package/amsxtra.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/apjfonts.sty.ltxml' 'blib/lib/LaTeXML/Package/apjfonts.sty.ltxml' \
	  'lib/LaTeXML/Package/appendix.sty.ltxml' 'blib/lib/LaTeXML/Package/appendix.sty.ltxml' \
	  'lib/LaTeXML/Package/applemac.def.ltxml' 'blib/lib/LaTeXML/Package/applemac.def.ltxml' \
	  'lib/LaTeXML/Package/array.sty.ltxml' 'blib/lib/LaTeXML/Package/array.sty.ltxml' \
	  'lib/LaTeXML/Package/article.cls.ltxml' 'blib/lib/LaTeXML/Package/article.cls.ltxml' \
	  'lib/LaTeXML/Package/attachfile.sty.ltxml' 'blib/lib/LaTeXML/Package/attachfile.sty.ltxml' \
	  'lib/LaTeXML/Package/atveryend.sty.ltxml' 'blib/lib/LaTeXML/Package/atveryend.sty.ltxml' \
	  'lib/LaTeXML/Package/authblk.sty.ltxml' 'blib/lib/LaTeXML/Package/authblk.sty.ltxml' \
	  'lib/LaTeXML/Package/auxhook.sty.ltxml' 'blib/lib/LaTeXML/Package/auxhook.sty.ltxml' \
	  'lib/LaTeXML/Package/avant.sty.ltxml' 'blib/lib/LaTeXML/Package/avant.sty.ltxml' \
	  'lib/LaTeXML/Package/babel.def.ltxml' 'blib/lib/LaTeXML/Package/babel.def.ltxml' \
	  'lib/LaTeXML/Package/babel.sty.ltxml' 'blib/lib/LaTeXML/Package/babel.sty.ltxml' \
	  'lib/LaTeXML/Package/babel_support.sty.ltxml' 'blib/lib/LaTeXML/Package/babel_support.sty.ltxml' \
	  'lib/LaTeXML/Package/balance.sty.ltxml' 'blib/lib/LaTeXML/Package/balance.sty.ltxml' \
	  'lib/LaTeXML/Package/bbding.sty.ltxml' 'blib/lib/LaTeXML/Package/bbding.sty.ltxml' \
	  'lib/LaTeXML/Package/bbm.sty.ltxml' 'blib/lib/LaTeXML/Package/bbm.sty.ltxml' \
	  'lib/LaTeXML/Package/bbold.sty.ltxml' 'blib/lib/LaTeXML/Package/bbold.sty.ltxml' \
	  'lib/LaTeXML/Package/beamer.cls.ltxml' 'blib/lib/LaTeXML/Package/beamer.cls.ltxml' \
	  'lib/LaTeXML/Package/beton.sty.ltxml' 'blib/lib/LaTeXML/Package/beton.sty.ltxml' \
	  'lib/LaTeXML/Package/bezier.sty.ltxml' 'blib/lib/LaTeXML/Package/bezier.sty.ltxml' \
	  'lib/LaTeXML/Package/bibunits.sty.ltxml' 'blib/lib/LaTeXML/Package/bibunits.sty.ltxml' \
	  'lib/LaTeXML/Package/bigintcalc.sty.ltxml' 'blib/lib/LaTeXML/Package/bigintcalc.sty.ltxml' \
	  'lib/LaTeXML/Package/bitset.sty.ltxml' 'blib/lib/LaTeXML/Package/bitset.sty.ltxml' \
	  'lib/LaTeXML/Package/blindtext.sty.ltxml' 'blib/lib/LaTeXML/Package/blindtext.sty.ltxml' \
	  'lib/LaTeXML/Package/bm.sty.ltxml' 'blib/lib/LaTeXML/Package/bm.sty.ltxml' \
	  'lib/LaTeXML/Package/book.cls.ltxml' 'blib/lib/LaTeXML/Package/book.cls.ltxml' \
	  'lib/LaTeXML/Package/bookman.sty.ltxml' 'blib/lib/LaTeXML/Package/bookman.sty.ltxml' \
	  'lib/LaTeXML/Package/bookmark.sty.ltxml' 'blib/lib/LaTeXML/Package/bookmark.sty.ltxml' \
	  'lib/LaTeXML/Package/booktabs.sty.ltxml' 'blib/lib/LaTeXML/Package/booktabs.sty.ltxml' \
	  'lib/LaTeXML/Package/braket.sty.ltxml' 'blib/lib/LaTeXML/Package/braket.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/breakurl.sty.ltxml' 'blib/lib/LaTeXML/Package/breakurl.sty.ltxml' \
	  'lib/LaTeXML/Package/calc.sty.ltxml' 'blib/lib/LaTeXML/Package/calc.sty.ltxml' \
	  'lib/LaTeXML/Package/calrsfs.sty.ltxml' 'blib/lib/LaTeXML/Package/calrsfs.sty.ltxml' \
	  'lib/LaTeXML/Package/cancel.sty.ltxml' 'blib/lib/LaTeXML/Package/cancel.sty.ltxml' \
	  'lib/LaTeXML/Package/caption.sty.ltxml' 'blib/lib/LaTeXML/Package/caption.sty.ltxml' \
	  'lib/LaTeXML/Package/cases.sty.ltxml' 'blib/lib/LaTeXML/Package/cases.sty.ltxml' \
	  'lib/LaTeXML/Package/ccfonts.sty.ltxml' 'blib/lib/LaTeXML/Package/ccfonts.sty.ltxml' \
	  'lib/LaTeXML/Package/chancery.sty.ltxml' 'blib/lib/LaTeXML/Package/chancery.sty.ltxml' \
	  'lib/LaTeXML/Package/chapterbib.sty.ltxml' 'blib/lib/LaTeXML/Package/chapterbib.sty.ltxml' \
	  'lib/LaTeXML/Package/charter.sty.ltxml' 'blib/lib/LaTeXML/Package/charter.sty.ltxml' \
	  'lib/LaTeXML/Package/chngcntr.sty.ltxml' 'blib/lib/LaTeXML/Package/chngcntr.sty.ltxml' \
	  'lib/LaTeXML/Package/circuitikz.sty.ltxml' 'blib/lib/LaTeXML/Package/circuitikz.sty.ltxml' \
	  'lib/LaTeXML/Package/cite.sty.ltxml' 'blib/lib/LaTeXML/Package/cite.sty.ltxml' \
	  'lib/LaTeXML/Package/citesort.sty.ltxml' 'blib/lib/LaTeXML/Package/citesort.sty.ltxml' \
	  'lib/LaTeXML/Package/cleveref.sty.ltxml' 'blib/lib/LaTeXML/Package/cleveref.sty.ltxml' \
	  'lib/LaTeXML/Package/cmbright.sty.ltxml' 'blib/lib/LaTeXML/Package/cmbright.sty.ltxml' \
	  'lib/LaTeXML/Package/color.sty.ltxml' 'blib/lib/LaTeXML/Package/color.sty.ltxml' \
	  'lib/LaTeXML/Package/colordvi.sty.ltxml' 'blib/lib/LaTeXML/Package/colordvi.sty.ltxml' \
	  'lib/LaTeXML/Package/colortbl.sty.ltxml' 'blib/lib/LaTeXML/Package/colortbl.sty.ltxml' \
	  'lib/LaTeXML/Package/comment.sty.ltxml' 'blib/lib/LaTeXML/Package/comment.sty.ltxml' \
	  'lib/LaTeXML/Package/concmath.sty.ltxml' 'blib/lib/LaTeXML/Package/concmath.sty.ltxml' \
	  'lib/LaTeXML/Package/courier.sty.ltxml' 'blib/lib/LaTeXML/Package/courier.sty.ltxml' \
	  'lib/LaTeXML/Package/cp852.def.ltxml' 'blib/lib/LaTeXML/Package/cp852.def.ltxml' \
	  'lib/LaTeXML/Package/crop.sty.ltxml' 'blib/lib/LaTeXML/Package/crop.sty.ltxml' \
	  'lib/LaTeXML/Package/cropmark.sty.ltxml' 'blib/lib/LaTeXML/Package/cropmark.sty.ltxml' \
	  'lib/LaTeXML/Package/csquotes.def.ltxml' 'blib/lib/LaTeXML/Package/csquotes.def.ltxml' \
	  'lib/LaTeXML/Package/csquotes.sty.ltxml' 'blib/lib/LaTeXML/Package/csquotes.sty.ltxml' \
	  'lib/LaTeXML/Package/dcolumn.sty.ltxml' 'blib/lib/LaTeXML/Package/dcolumn.sty.ltxml' \
	  'lib/LaTeXML/Package/deluxetable.sty.ltxml' 'blib/lib/LaTeXML/Package/deluxetable.sty.ltxml' \
	  'lib/LaTeXML/Package/diagbox.sty.ltxml' 'blib/lib/LaTeXML/Package/diagbox.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/ding.fontmap.ltxml' 'blib/lib/LaTeXML/Package/ding.fontmap.ltxml' \
	  'lib/LaTeXML/Package/doi.sty.ltxml' 'blib/lib/LaTeXML/Package/doi.sty.ltxml' \
	  'lib/LaTeXML/Package/doublespace.sty.ltxml' 'blib/lib/LaTeXML/Package/doublespace.sty.ltxml' \
	  'lib/LaTeXML/Package/dsfont.sty.ltxml' 'blib/lib/LaTeXML/Package/dsfont.sty.ltxml' \
	  'lib/LaTeXML/Package/eTeX.pool.ltxml' 'blib/lib/LaTeXML/Package/eTeX.pool.ltxml' \
	  'lib/LaTeXML/Package/ed.sty.ltxml' 'blib/lib/LaTeXML/Package/ed.sty.ltxml' \
	  'lib/LaTeXML/Package/ellipsis.sty.ltxml' 'blib/lib/LaTeXML/Package/ellipsis.sty.ltxml' \
	  'lib/LaTeXML/Package/elsart.cls.ltxml' 'blib/lib/LaTeXML/Package/elsart.cls.ltxml' \
	  'lib/LaTeXML/Package/elsart.sty.ltxml' 'blib/lib/LaTeXML/Package/elsart.sty.ltxml' \
	  'lib/LaTeXML/Package/elsart_support.sty.ltxml' 'blib/lib/LaTeXML/Package/elsart_support.sty.ltxml' \
	  'lib/LaTeXML/Package/elsart_support_core.sty.ltxml' 'blib/lib/LaTeXML/Package/elsart_support_core.sty.ltxml' \
	  'lib/LaTeXML/Package/elsarticle.cls.ltxml' 'blib/lib/LaTeXML/Package/elsarticle.cls.ltxml' \
	  'lib/LaTeXML/Package/empheq.sty.ltxml' 'blib/lib/LaTeXML/Package/empheq.sty.ltxml' \
	  'lib/LaTeXML/Package/emulateapj.cls.ltxml' 'blib/lib/LaTeXML/Package/emulateapj.cls.ltxml' \
	  'lib/LaTeXML/Package/emulateapj.sty.ltxml' 'blib/lib/LaTeXML/Package/emulateapj.sty.ltxml' \
	  'lib/LaTeXML/Package/emulateapj5.sty.ltxml' 'blib/lib/LaTeXML/Package/emulateapj5.sty.ltxml' \
	  'lib/LaTeXML/Package/endnotes.sty.ltxml' 'blib/lib/LaTeXML/Package/endnotes.sty.ltxml' \
	  'lib/LaTeXML/Package/english.sty.ltxml' 'blib/lib/LaTeXML/Package/english.sty.ltxml' \
	  'lib/LaTeXML/Package/enumerate.sty.ltxml' 'blib/lib/LaTeXML/Package/enumerate.sty.ltxml' \
	  'lib/LaTeXML/Package/enumitem.sty.ltxml' 'blib/lib/LaTeXML/Package/enumitem.sty.ltxml' \
	  'lib/LaTeXML/Package/epigraph.sty.ltxml' 'blib/lib/LaTeXML/Package/epigraph.sty.ltxml' \
	  'lib/LaTeXML/Package/epsf.sty.ltxml' 'blib/lib/LaTeXML/Package/epsf.sty.ltxml' \
	  'lib/LaTeXML/Package/epsf.tex.ltxml' 'blib/lib/LaTeXML/Package/epsf.tex.ltxml' \
	  'lib/LaTeXML/Package/epsfig.sty.ltxml' 'blib/lib/LaTeXML/Package/epsfig.sty.ltxml' \
	  'lib/LaTeXML/Package/epstopdf.sty.ltxml' 'blib/lib/LaTeXML/Package/epstopdf.sty.ltxml' \
	  'lib/LaTeXML/Package/esint.sty.ltxml' 'blib/lib/LaTeXML/Package/esint.sty.ltxml' \
	  'lib/LaTeXML/Package/espcrc.sty.ltxml' 'blib/lib/LaTeXML/Package/espcrc.sty.ltxml' \
	  'lib/LaTeXML/Package/etex.sty.ltxml' 'blib/lib/LaTeXML/Package/etex.sty.ltxml' \
	  'lib/LaTeXML/Package/etoolbox.sty.ltxml' 'blib/lib/LaTeXML/Package/etoolbox.sty.ltxml' \
	  'lib/LaTeXML/Package/eucal.sty.ltxml' 'blib/lib/LaTeXML/Package/eucal.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/eufrak.sty.ltxml' 'blib/lib/LaTeXML/Package/eufrak.sty.ltxml' \
	  'lib/LaTeXML/Package/euler.sty.ltxml' 'blib/lib/LaTeXML/Package/euler.sty.ltxml' \
	  'lib/LaTeXML/Package/eulervm.sty.ltxml' 'blib/lib/LaTeXML/Package/eulervm.sty.ltxml' \
	  'lib/LaTeXML/Package/eurosym.sty.ltxml' 'blib/lib/LaTeXML/Package/eurosym.sty.ltxml' \
	  'lib/LaTeXML/Package/euscript.sty.ltxml' 'blib/lib/LaTeXML/Package/euscript.sty.ltxml' \
	  'lib/LaTeXML/Package/expl3.ltx.ltxml' 'blib/lib/LaTeXML/Package/expl3.ltx.ltxml' \
	  'lib/LaTeXML/Package/expl3.pool.ltxml' 'blib/lib/LaTeXML/Package/expl3.pool.ltxml' \
	  'lib/LaTeXML/Package/expl3.sty.ltxml' 'blib/lib/LaTeXML/Package/expl3.sty.ltxml' \
	  'lib/LaTeXML/Package/exscale.sty.ltxml' 'blib/lib/LaTeXML/Package/exscale.sty.ltxml' \
	  'lib/LaTeXML/Package/fancybox.sty.ltxml' 'blib/lib/LaTeXML/Package/fancybox.sty.ltxml' \
	  'lib/LaTeXML/Package/fancyhdr.sty.ltxml' 'blib/lib/LaTeXML/Package/fancyhdr.sty.ltxml' \
	  'lib/LaTeXML/Package/fancyheadings.sty.ltxml' 'blib/lib/LaTeXML/Package/fancyheadings.sty.ltxml' \
	  'lib/LaTeXML/Package/fancyvrb.sty.ltxml' 'blib/lib/LaTeXML/Package/fancyvrb.sty.ltxml' \
	  'lib/LaTeXML/Package/feynmf.sty.ltxml' 'blib/lib/LaTeXML/Package/feynmf.sty.ltxml' \
	  'lib/LaTeXML/Package/filehook.sty.ltxml' 'blib/lib/LaTeXML/Package/filehook.sty.ltxml' \
	  'lib/LaTeXML/Package/fix-cm.sty.ltxml' 'blib/lib/LaTeXML/Package/fix-cm.sty.ltxml' \
	  'lib/LaTeXML/Package/fixltx2e.sty.ltxml' 'blib/lib/LaTeXML/Package/fixltx2e.sty.ltxml' \
	  'lib/LaTeXML/Package/fixme.sty.ltxml' 'blib/lib/LaTeXML/Package/fixme.sty.ltxml' \
	  'lib/LaTeXML/Package/flafter.sty.ltxml' 'blib/lib/LaTeXML/Package/flafter.sty.ltxml' \
	  'lib/LaTeXML/Package/fleqn.sty.ltxml' 'blib/lib/LaTeXML/Package/fleqn.sty.ltxml' \
	  'lib/LaTeXML/Package/float.sty.ltxml' 'blib/lib/LaTeXML/Package/float.sty.ltxml' \
	  'lib/LaTeXML/Package/floatfig.sty.ltxml' 'blib/lib/LaTeXML/Package/floatfig.sty.ltxml' \
	  'lib/LaTeXML/Package/floatflt.sty.ltxml' 'blib/lib/LaTeXML/Package/floatflt.sty.ltxml' \
	  'lib/LaTeXML/Package/floatpag.sty.ltxml' 'blib/lib/LaTeXML/Package/floatpag.sty.ltxml' \
	  'lib/LaTeXML/Package/flowchart.sty.ltxml' 'blib/lib/LaTeXML/Package/flowchart.sty.ltxml' \
	  'lib/LaTeXML/Package/flushend.sty.ltxml' 'blib/lib/LaTeXML/Package/flushend.sty.ltxml' \
	  'lib/LaTeXML/Package/fontenc.sty.ltxml' 'blib/lib/LaTeXML/Package/fontenc.sty.ltxml' \
	  'lib/LaTeXML/Package/fontspec.sty.ltxml' 'blib/lib/LaTeXML/Package/fontspec.sty.ltxml' \
	  'lib/LaTeXML/Package/footmisc.sty.ltxml' 'blib/lib/LaTeXML/Package/footmisc.sty.ltxml' \
	  'lib/LaTeXML/Package/footnote.sty.ltxml' 'blib/lib/LaTeXML/Package/footnote.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/fourier.sty.ltxml' 'blib/lib/LaTeXML/Package/fourier.sty.ltxml' \
	  'lib/LaTeXML/Package/framed.sty.ltxml' 'blib/lib/LaTeXML/Package/framed.sty.ltxml' \
	  'lib/LaTeXML/Package/french.ldf.ltxml' 'blib/lib/LaTeXML/Package/french.ldf.ltxml' \
	  'lib/LaTeXML/Package/frenchb.ldf.ltxml' 'blib/lib/LaTeXML/Package/frenchb.ldf.ltxml' \
	  'lib/LaTeXML/Package/fullpage.sty.ltxml' 'blib/lib/LaTeXML/Package/fullpage.sty.ltxml' \
	  'lib/LaTeXML/Package/gen-j-l.cls.ltxml' 'blib/lib/LaTeXML/Package/gen-j-l.cls.ltxml' \
	  'lib/LaTeXML/Package/gen-m-l.cls.ltxml' 'blib/lib/LaTeXML/Package/gen-m-l.cls.ltxml' \
	  'lib/LaTeXML/Package/gen-p-l.cls.ltxml' 'blib/lib/LaTeXML/Package/gen-p-l.cls.ltxml' \
	  'lib/LaTeXML/Package/gensymb.sty.ltxml' 'blib/lib/LaTeXML/Package/gensymb.sty.ltxml' \
	  'lib/LaTeXML/Package/geometry.sty.ltxml' 'blib/lib/LaTeXML/Package/geometry.sty.ltxml' \
	  'lib/LaTeXML/Package/german.sty.ltxml' 'blib/lib/LaTeXML/Package/german.sty.ltxml' \
	  'lib/LaTeXML/Package/gettitlestring.sty.ltxml' 'blib/lib/LaTeXML/Package/gettitlestring.sty.ltxml' \
	  'lib/LaTeXML/Package/glossaries.sty.ltxml' 'blib/lib/LaTeXML/Package/glossaries.sty.ltxml' \
	  'lib/LaTeXML/Package/graphics.sty.ltxml' 'blib/lib/LaTeXML/Package/graphics.sty.ltxml' \
	  'lib/LaTeXML/Package/graphicx.sty.ltxml' 'blib/lib/LaTeXML/Package/graphicx.sty.ltxml' \
	  'lib/LaTeXML/Package/grffile.sty.ltxml' 'blib/lib/LaTeXML/Package/grffile.sty.ltxml' \
	  'lib/LaTeXML/Package/helvet.sty.ltxml' 'blib/lib/LaTeXML/Package/helvet.sty.ltxml' \
	  'lib/LaTeXML/Package/hepunits.sty.ltxml' 'blib/lib/LaTeXML/Package/hepunits.sty.ltxml' \
	  'lib/LaTeXML/Package/here.sty.ltxml' 'blib/lib/LaTeXML/Package/here.sty.ltxml' \
	  'lib/LaTeXML/Package/hhline.sty.ltxml' 'blib/lib/LaTeXML/Package/hhline.sty.ltxml' \
	  'lib/LaTeXML/Package/html.sty.ltxml' 'blib/lib/LaTeXML/Package/html.sty.ltxml' \
	  'lib/LaTeXML/Package/hypcap.sty.ltxml' 'blib/lib/LaTeXML/Package/hypcap.sty.ltxml' \
	  'lib/LaTeXML/Package/hyperref.sty.ltxml' 'blib/lib/LaTeXML/Package/hyperref.sty.ltxml' \
	  'lib/LaTeXML/Package/hyperxmp.sty.ltxml' 'blib/lib/LaTeXML/Package/hyperxmp.sty.ltxml' \
	  'lib/LaTeXML/Package/icml.sty.ltxml' 'blib/lib/LaTeXML/Package/icml.sty.ltxml' \
	  'lib/LaTeXML/Package/icml_support.sty.ltxml' 'blib/lib/LaTeXML/Package/icml_support.sty.ltxml' \
	  'lib/LaTeXML/Package/ieeeconf.cls.ltxml' 'blib/lib/LaTeXML/Package/ieeeconf.cls.ltxml' \
	  'lib/LaTeXML/Package/ifblk.fontmap.ltxml' 'blib/lib/LaTeXML/Package/ifblk.fontmap.ltxml' \
	  'lib/LaTeXML/Package/ifclk.fontmap.ltxml' 'blib/lib/LaTeXML/Package/ifclk.fontmap.ltxml' \
	  'lib/LaTeXML/Package/ifetex.sty.ltxml' 'blib/lib/LaTeXML/Package/ifetex.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/ifgeo.fontmap.ltxml' 'blib/lib/LaTeXML/Package/ifgeo.fontmap.ltxml' \
	  'lib/LaTeXML/Package/ifluatex.sty.ltxml' 'blib/lib/LaTeXML/Package/ifluatex.sty.ltxml' \
	  'lib/LaTeXML/Package/ifpdf.sty.ltxml' 'blib/lib/LaTeXML/Package/ifpdf.sty.ltxml' \
	  'lib/LaTeXML/Package/ifplatform.sty.ltxml' 'blib/lib/LaTeXML/Package/ifplatform.sty.ltxml' \
	  'lib/LaTeXML/Package/ifsym.fontmap.ltxml' 'blib/lib/LaTeXML/Package/ifsym.fontmap.ltxml' \
	  'lib/LaTeXML/Package/ifsym.sty.ltxml' 'blib/lib/LaTeXML/Package/ifsym.sty.ltxml' \
	  'lib/LaTeXML/Package/iftex.sty.ltxml' 'blib/lib/LaTeXML/Package/iftex.sty.ltxml' \
	  'lib/LaTeXML/Package/ifthen.sty.ltxml' 'blib/lib/LaTeXML/Package/ifthen.sty.ltxml' \
	  'lib/LaTeXML/Package/ifvtex.sty.ltxml' 'blib/lib/LaTeXML/Package/ifvtex.sty.ltxml' \
	  'lib/LaTeXML/Package/ifwea.fontmap.ltxml' 'blib/lib/LaTeXML/Package/ifwea.fontmap.ltxml' \
	  'lib/LaTeXML/Package/ifxetex.sty.ltxml' 'blib/lib/LaTeXML/Package/ifxetex.sty.ltxml' \
	  'lib/LaTeXML/Package/ijcai.sty.ltxml' 'blib/lib/LaTeXML/Package/ijcai.sty.ltxml' \
	  'lib/LaTeXML/Package/import.sty.ltxml' 'blib/lib/LaTeXML/Package/import.sty.ltxml' \
	  'lib/LaTeXML/Package/indentfirst.sty.ltxml' 'blib/lib/LaTeXML/Package/indentfirst.sty.ltxml' \
	  'lib/LaTeXML/Package/infwarerr.sty.ltxml' 'blib/lib/LaTeXML/Package/infwarerr.sty.ltxml' \
	  'lib/LaTeXML/Package/inputenc.sty.ltxml' 'blib/lib/LaTeXML/Package/inputenc.sty.ltxml' \
	  'lib/LaTeXML/Package/inst_support.sty.ltxml' 'blib/lib/LaTeXML/Package/inst_support.sty.ltxml' \
	  'lib/LaTeXML/Package/intcalc.sty.ltxml' 'blib/lib/LaTeXML/Package/intcalc.sty.ltxml' \
	  'lib/LaTeXML/Package/iopams.sty.ltxml' 'blib/lib/LaTeXML/Package/iopams.sty.ltxml' \
	  'lib/LaTeXML/Package/iopart.cls.ltxml' 'blib/lib/LaTeXML/Package/iopart.cls.ltxml' \
	  'lib/LaTeXML/Package/iopart_support.sty.ltxml' 'blib/lib/LaTeXML/Package/iopart_support.sty.ltxml' \
	  'lib/LaTeXML/Package/jheppub.sty.ltxml' 'blib/lib/LaTeXML/Package/jheppub.sty.ltxml' \
	  'lib/LaTeXML/Package/keyval.sty.ltxml' 'blib/lib/LaTeXML/Package/keyval.sty.ltxml' \
	  'lib/LaTeXML/Package/kvdefinekeys.sty.ltxml' 'blib/lib/LaTeXML/Package/kvdefinekeys.sty.ltxml' \
	  'lib/LaTeXML/Package/kvoptions.sty.ltxml' 'blib/lib/LaTeXML/Package/kvoptions.sty.ltxml' \
	  'lib/LaTeXML/Package/kvsetkeys.sty.ltxml' 'blib/lib/LaTeXML/Package/kvsetkeys.sty.ltxml' \
	  'lib/LaTeXML/Package/l3keys2e.sty.ltxml' 'blib/lib/LaTeXML/Package/l3keys2e.sty.ltxml' \
	  'lib/LaTeXML/Package/lastpage.sty.ltxml' 'blib/lib/LaTeXML/Package/lastpage.sty.ltxml' \
	  'lib/LaTeXML/Package/latexml.sty.ltxml' 'blib/lib/LaTeXML/Package/latexml.sty.ltxml' \
	  'lib/LaTeXML/Package/latexsym.sty.ltxml' 'blib/lib/LaTeXML/Package/latexsym.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/latin10.def.ltxml' 'blib/lib/LaTeXML/Package/latin10.def.ltxml' \
	  'lib/LaTeXML/Package/lgr.fontmap.ltxml' 'blib/lib/LaTeXML/Package/lgr.fontmap.ltxml' \
	  'lib/LaTeXML/Package/lineno.sty.ltxml' 'blib/lib/LaTeXML/Package/lineno.sty.ltxml' \
	  'lib/LaTeXML/Package/lipsum.sty.ltxml' 'blib/lib/LaTeXML/Package/lipsum.sty.ltxml' \
	  'lib/LaTeXML/Package/listings.sty.ltxml' 'blib/lib/LaTeXML/Package/listings.sty.ltxml' \
	  'lib/LaTeXML/Package/listingsutf8.sty.ltxml' 'blib/lib/LaTeXML/Package/listingsutf8.sty.ltxml' \
	  'lib/LaTeXML/Package/llncs.cls.ltxml' 'blib/lib/LaTeXML/Package/llncs.cls.ltxml' \
	  'lib/LaTeXML/Package/lmodern.sty.ltxml' 'blib/lib/LaTeXML/Package/lmodern.sty.ltxml' \
	  'lib/LaTeXML/Package/longtable.sty.ltxml' 'blib/lib/LaTeXML/Package/longtable.sty.ltxml' \
	  'lib/LaTeXML/Package/lscape.sty.ltxml' 'blib/lib/LaTeXML/Package/lscape.sty.ltxml' \
	  'lib/LaTeXML/Package/ltxcmds.sty.ltxml' 'blib/lib/LaTeXML/Package/ltxcmds.sty.ltxml' \
	  'lib/LaTeXML/Package/luximono.sty.ltxml' 'blib/lib/LaTeXML/Package/luximono.sty.ltxml' \
	  'lib/LaTeXML/Package/lxRDFa.sty.ltxml' 'blib/lib/LaTeXML/Package/lxRDFa.sty.ltxml' \
	  'lib/LaTeXML/Package/ly1.fontmap.ltxml' 'blib/lib/LaTeXML/Package/ly1.fontmap.ltxml' \
	  'lib/LaTeXML/Package/makecell.sty.ltxml' 'blib/lib/LaTeXML/Package/makecell.sty.ltxml' \
	  'lib/LaTeXML/Package/makeidx.sty.ltxml' 'blib/lib/LaTeXML/Package/makeidx.sty.ltxml' \
	  'lib/LaTeXML/Package/marvosym.sty.ltxml' 'blib/lib/LaTeXML/Package/marvosym.sty.ltxml' \
	  'lib/LaTeXML/Package/mathabx.sty.ltxml' 'blib/lib/LaTeXML/Package/mathabx.sty.ltxml' \
	  'lib/LaTeXML/Package/mathbbol.sty.ltxml' 'blib/lib/LaTeXML/Package/mathbbol.sty.ltxml' \
	  'lib/LaTeXML/Package/mathdots.sty.ltxml' 'blib/lib/LaTeXML/Package/mathdots.sty.ltxml' \
	  'lib/LaTeXML/Package/mathpazo.sty.ltxml' 'blib/lib/LaTeXML/Package/mathpazo.sty.ltxml' \
	  'lib/LaTeXML/Package/mathpple.sty.ltxml' 'blib/lib/LaTeXML/Package/mathpple.sty.ltxml' \
	  'lib/LaTeXML/Package/mathptm.sty.ltxml' 'blib/lib/LaTeXML/Package/mathptm.sty.ltxml' \
	  'lib/LaTeXML/Package/mathptmx.sty.ltxml' 'blib/lib/LaTeXML/Package/mathptmx.sty.ltxml' \
	  'lib/LaTeXML/Package/mathrsfs.sty.ltxml' 'blib/lib/LaTeXML/Package/mathrsfs.sty.ltxml' \
	  'lib/LaTeXML/Package/mathtools.sty.ltxml' 'blib/lib/LaTeXML/Package/mathtools.sty.ltxml' \
	  'lib/LaTeXML/Package/microtype.sty.ltxml' 'blib/lib/LaTeXML/Package/microtype.sty.ltxml' \
	  'lib/LaTeXML/Package/minimal.cls.ltxml' 'blib/lib/LaTeXML/Package/minimal.cls.ltxml' \
	  'lib/LaTeXML/Package/mleftright.sty.ltxml' 'blib/lib/LaTeXML/Package/mleftright.sty.ltxml' \
	  'lib/LaTeXML/Package/mn.cls.ltxml' 'blib/lib/LaTeXML/Package/mn.cls.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/mn2e.cls.ltxml' 'blib/lib/LaTeXML/Package/mn2e.cls.ltxml' \
	  'lib/LaTeXML/Package/mn2e_support.sty.ltxml' 'blib/lib/LaTeXML/Package/mn2e_support.sty.ltxml' \
	  'lib/LaTeXML/Package/mnras.cls.ltxml' 'blib/lib/LaTeXML/Package/mnras.cls.ltxml' \
	  'lib/LaTeXML/Package/moderncv.cls.ltxml' 'blib/lib/LaTeXML/Package/moderncv.cls.ltxml' \
	  'lib/LaTeXML/Package/multicol.sty.ltxml' 'blib/lib/LaTeXML/Package/multicol.sty.ltxml' \
	  'lib/LaTeXML/Package/multido.sty.ltxml' 'blib/lib/LaTeXML/Package/multido.sty.ltxml' \
	  'lib/LaTeXML/Package/multirow.sty.ltxml' 'blib/lib/LaTeXML/Package/multirow.sty.ltxml' \
	  'lib/LaTeXML/Package/nameref.sty.ltxml' 'blib/lib/LaTeXML/Package/nameref.sty.ltxml' \
	  'lib/LaTeXML/Package/natbib.sty.ltxml' 'blib/lib/LaTeXML/Package/natbib.sty.ltxml' \
	  'lib/LaTeXML/Package/neurips.sty.ltxml' 'blib/lib/LaTeXML/Package/neurips.sty.ltxml' \
	  'lib/LaTeXML/Package/newcent.sty.ltxml' 'blib/lib/LaTeXML/Package/newcent.sty.ltxml' \
	  'lib/LaTeXML/Package/newfloat.sty.ltxml' 'blib/lib/LaTeXML/Package/newfloat.sty.ltxml' \
	  'lib/LaTeXML/Package/newlfont.sty.ltxml' 'blib/lib/LaTeXML/Package/newlfont.sty.ltxml' \
	  'lib/LaTeXML/Package/newtxmath.sty.ltxml' 'blib/lib/LaTeXML/Package/newtxmath.sty.ltxml' \
	  'lib/LaTeXML/Package/newtxtext.sty.ltxml' 'blib/lib/LaTeXML/Package/newtxtext.sty.ltxml' \
	  'lib/LaTeXML/Package/ngerman.sty.ltxml' 'blib/lib/LaTeXML/Package/ngerman.sty.ltxml' \
	  'lib/LaTeXML/Package/nicefrac.sty.ltxml' 'blib/lib/LaTeXML/Package/nicefrac.sty.ltxml' \
	  'lib/LaTeXML/Package/nil.ldf.ltxml' 'blib/lib/LaTeXML/Package/nil.ldf.ltxml' \
	  'lib/LaTeXML/Package/nomencl.sty.ltxml' 'blib/lib/LaTeXML/Package/nomencl.sty.ltxml' \
	  'lib/LaTeXML/Package/nopageno.sty.ltxml' 'blib/lib/LaTeXML/Package/nopageno.sty.ltxml' \
	  'lib/LaTeXML/Package/ntheorem.sty.ltxml' 'blib/lib/LaTeXML/Package/ntheorem.sty.ltxml' \
	  'lib/LaTeXML/Package/numprint.sty.ltxml' 'blib/lib/LaTeXML/Package/numprint.sty.ltxml' \
	  'lib/LaTeXML/Package/ot4.fontmap.ltxml' 'blib/lib/LaTeXML/Package/ot4.fontmap.ltxml' \
	  'lib/LaTeXML/Package/overpic.sty.ltxml' 'blib/lib/LaTeXML/Package/overpic.sty.ltxml' \
	  'lib/LaTeXML/Package/palatino.sty.ltxml' 'blib/lib/LaTeXML/Package/palatino.sty.ltxml' \
	  'lib/LaTeXML/Package/paralist.sty.ltxml' 'blib/lib/LaTeXML/Package/paralist.sty.ltxml' \
	  'lib/LaTeXML/Package/parskip.sty.ltxml' 'blib/lib/LaTeXML/Package/parskip.sty.ltxml' \
	  'lib/LaTeXML/Package/pdfTeX.pool.ltxml' 'blib/lib/LaTeXML/Package/pdfTeX.pool.ltxml' \
	  'lib/LaTeXML/Package/pdflscape.sty.ltxml' 'blib/lib/LaTeXML/Package/pdflscape.sty.ltxml' \
	  'lib/LaTeXML/Package/pdfpages.sty.ltxml' 'blib/lib/LaTeXML/Package/pdfpages.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/pdfsync.sty.ltxml' 'blib/lib/LaTeXML/Package/pdfsync.sty.ltxml' \
	  'lib/LaTeXML/Package/pdftexcmds.sty.ltxml' 'blib/lib/LaTeXML/Package/pdftexcmds.sty.ltxml' \
	  'lib/LaTeXML/Package/pgf.sty.ltxml' 'blib/lib/LaTeXML/Package/pgf.sty.ltxml' \
	  'lib/LaTeXML/Package/pgfkeys.code.tex.ltxml' 'blib/lib/LaTeXML/Package/pgfkeys.code.tex.ltxml' \
	  'lib/LaTeXML/Package/pgfmath.code.tex.ltxml' 'blib/lib/LaTeXML/Package/pgfmath.code.tex.ltxml' \
	  'lib/LaTeXML/Package/pgfmathcalc.code.tex.ltxml' 'blib/lib/LaTeXML/Package/pgfmathcalc.code.tex.ltxml' \
	  'lib/LaTeXML/Package/pgfplots.sty.ltxml' 'blib/lib/LaTeXML/Package/pgfplots.sty.ltxml' \
	  'lib/LaTeXML/Package/pgfplotstable.sty.ltxml' 'blib/lib/LaTeXML/Package/pgfplotstable.sty.ltxml' \
	  'lib/LaTeXML/Package/pgfsys-latexml.def.ltxml' 'blib/lib/LaTeXML/Package/pgfsys-latexml.def.ltxml' \
	  'lib/LaTeXML/Package/pgfutil-common.tex.ltxml' 'blib/lib/LaTeXML/Package/pgfutil-common.tex.ltxml' \
	  'lib/LaTeXML/Package/physics.sty.ltxml' 'blib/lib/LaTeXML/Package/physics.sty.ltxml' \
	  'lib/LaTeXML/Package/pifont.sty.ltxml' 'blib/lib/LaTeXML/Package/pifont.sty.ltxml' \
	  'lib/LaTeXML/Package/placeins.sty.ltxml' 'blib/lib/LaTeXML/Package/placeins.sty.ltxml' \
	  'lib/LaTeXML/Package/prettyref.sty.ltxml' 'blib/lib/LaTeXML/Package/prettyref.sty.ltxml' \
	  'lib/LaTeXML/Package/preview.sty.ltxml' 'blib/lib/LaTeXML/Package/preview.sty.ltxml' \
	  'lib/LaTeXML/Package/proof.sty.ltxml' 'blib/lib/LaTeXML/Package/proof.sty.ltxml' \
	  'lib/LaTeXML/Package/proofwiki.sty.ltxml' 'blib/lib/LaTeXML/Package/proofwiki.sty.ltxml' \
	  'lib/LaTeXML/Package/psfig.sty.ltxml' 'blib/lib/LaTeXML/Package/psfig.sty.ltxml' \
	  'lib/LaTeXML/Package/psfig.tex.ltxml' 'blib/lib/LaTeXML/Package/psfig.tex.ltxml' \
	  'lib/LaTeXML/Package/psfrag.sty.ltxml' 'blib/lib/LaTeXML/Package/psfrag.sty.ltxml' \
	  'lib/LaTeXML/Package/pslatex.sty.ltxml' 'blib/lib/LaTeXML/Package/pslatex.sty.ltxml' \
	  'lib/LaTeXML/Package/pspicture.sty.ltxml' 'blib/lib/LaTeXML/Package/pspicture.sty.ltxml' \
	  'lib/LaTeXML/Package/pst-grad.sty.ltxml' 'blib/lib/LaTeXML/Package/pst-grad.sty.ltxml' \
	  'lib/LaTeXML/Package/pst-node.sty.ltxml' 'blib/lib/LaTeXML/Package/pst-node.sty.ltxml' \
	  'lib/LaTeXML/Package/pstricks.sty.ltxml' 'blib/lib/LaTeXML/Package/pstricks.sty.ltxml' \
	  'lib/LaTeXML/Package/pstricks.tex.ltxml' 'blib/lib/LaTeXML/Package/pstricks.tex.ltxml' \
	  'lib/LaTeXML/Package/pxfonts.sty.ltxml' 'blib/lib/LaTeXML/Package/pxfonts.sty.ltxml' \
	  'lib/LaTeXML/Package/pzd.fontmap.ltxml' 'blib/lib/LaTeXML/Package/pzd.fontmap.ltxml' \
	  'lib/LaTeXML/Package/quantumarticle.cls.ltxml' 'blib/lib/LaTeXML/Package/quantumarticle.cls.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/ragged2e.sty.ltxml' 'blib/lib/LaTeXML/Package/ragged2e.sty.ltxml' \
	  'lib/LaTeXML/Package/refcount.sty.ltxml' 'blib/lib/LaTeXML/Package/refcount.sty.ltxml' \
	  'lib/LaTeXML/Package/relsize.sty.ltxml' 'blib/lib/LaTeXML/Package/relsize.sty.ltxml' \
	  'lib/LaTeXML/Package/remreset.sty.ltxml' 'blib/lib/LaTeXML/Package/remreset.sty.ltxml' \
	  'lib/LaTeXML/Package/report.cls.ltxml' 'blib/lib/LaTeXML/Package/report.cls.ltxml' \
	  'lib/LaTeXML/Package/revsymb.sty.ltxml' 'blib/lib/LaTeXML/Package/revsymb.sty.ltxml' \
	  'lib/LaTeXML/Package/revtex.cls.ltxml' 'blib/lib/LaTeXML/Package/revtex.cls.ltxml' \
	  'lib/LaTeXML/Package/revtex.sty.ltxml' 'blib/lib/LaTeXML/Package/revtex.sty.ltxml' \
	  'lib/LaTeXML/Package/revtex3_support.sty.ltxml' 'blib/lib/LaTeXML/Package/revtex3_support.sty.ltxml' \
	  'lib/LaTeXML/Package/revtex4-1.cls.ltxml' 'blib/lib/LaTeXML/Package/revtex4-1.cls.ltxml' \
	  'lib/LaTeXML/Package/revtex4.cls.ltxml' 'blib/lib/LaTeXML/Package/revtex4.cls.ltxml' \
	  'lib/LaTeXML/Package/revtex4.sty.ltxml' 'blib/lib/LaTeXML/Package/revtex4.sty.ltxml' \
	  'lib/LaTeXML/Package/revtex4_support.sty.ltxml' 'blib/lib/LaTeXML/Package/revtex4_support.sty.ltxml' \
	  'lib/LaTeXML/Package/rotate.sty.ltxml' 'blib/lib/LaTeXML/Package/rotate.sty.ltxml' \
	  'lib/LaTeXML/Package/rotating.sty.ltxml' 'blib/lib/LaTeXML/Package/rotating.sty.ltxml' \
	  'lib/LaTeXML/Package/rsfs.sty.ltxml' 'blib/lib/LaTeXML/Package/rsfs.sty.ltxml' \
	  'lib/LaTeXML/Package/scalefnt.sty.ltxml' 'blib/lib/LaTeXML/Package/scalefnt.sty.ltxml' \
	  'lib/LaTeXML/Package/sectsty.sty.ltxml' 'blib/lib/LaTeXML/Package/sectsty.sty.ltxml' \
	  'lib/LaTeXML/Package/setspace.sty.ltxml' 'blib/lib/LaTeXML/Package/setspace.sty.ltxml' \
	  'lib/LaTeXML/Package/showkeys.sty.ltxml' 'blib/lib/LaTeXML/Package/showkeys.sty.ltxml' \
	  'lib/LaTeXML/Package/sidecap.sty.ltxml' 'blib/lib/LaTeXML/Package/sidecap.sty.ltxml' \
	  'lib/LaTeXML/Package/siunitx.sty.ltxml' 'blib/lib/LaTeXML/Package/siunitx.sty.ltxml' \
	  'lib/LaTeXML/Package/slashbox.sty.ltxml' 'blib/lib/LaTeXML/Package/slashbox.sty.ltxml' \
	  'lib/LaTeXML/Package/slashed.sty.ltxml' 'blib/lib/LaTeXML/Package/slashed.sty.ltxml' \
	  'lib/LaTeXML/Package/slides.cls.ltxml' 'blib/lib/LaTeXML/Package/slides.cls.ltxml' \
	  'lib/LaTeXML/Package/soul.sty.ltxml' 'blib/lib/LaTeXML/Package/soul.sty.ltxml' \
	  'lib/LaTeXML/Package/srcltx.sty.ltxml' 'blib/lib/LaTeXML/Package/srcltx.sty.ltxml' \
	  'lib/LaTeXML/Package/standalone.cls.ltxml' 'blib/lib/LaTeXML/Package/standalone.cls.ltxml' \
	  'lib/LaTeXML/Package/standalone.sty.ltxml' 'blib/lib/LaTeXML/Package/standalone.sty.ltxml' \
	  'lib/LaTeXML/Package/stfloats.sty.ltxml' 'blib/lib/LaTeXML/Package/stfloats.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/stmaryrd.sty.ltxml' 'blib/lib/LaTeXML/Package/stmaryrd.sty.ltxml' \
	  'lib/LaTeXML/Package/subcaption.sty.ltxml' 'blib/lib/LaTeXML/Package/subcaption.sty.ltxml' \
	  'lib/LaTeXML/Package/subeqn.sty.ltxml' 'blib/lib/LaTeXML/Package/subeqn.sty.ltxml' \
	  'lib/LaTeXML/Package/subeqnarray.sty.ltxml' 'blib/lib/LaTeXML/Package/subeqnarray.sty.ltxml' \
	  'lib/LaTeXML/Package/subfig.sty.ltxml' 'blib/lib/LaTeXML/Package/subfig.sty.ltxml' \
	  'lib/LaTeXML/Package/subfigure.sty.ltxml' 'blib/lib/LaTeXML/Package/subfigure.sty.ltxml' \
	  'lib/LaTeXML/Package/subfiles.cls.ltxml' 'blib/lib/LaTeXML/Package/subfiles.cls.ltxml' \
	  'lib/LaTeXML/Package/subfiles.sty.ltxml' 'blib/lib/LaTeXML/Package/subfiles.sty.ltxml' \
	  'lib/LaTeXML/Package/subfloat.sty.ltxml' 'blib/lib/LaTeXML/Package/subfloat.sty.ltxml' \
	  'lib/LaTeXML/Package/supertabular.sty.ltxml' 'blib/lib/LaTeXML/Package/supertabular.sty.ltxml' \
	  'lib/LaTeXML/Package/sv_support.sty.ltxml' 'blib/lib/LaTeXML/Package/sv_support.sty.ltxml' \
	  'lib/LaTeXML/Package/svg.sty.ltxml' 'blib/lib/LaTeXML/Package/svg.sty.ltxml' \
	  'lib/LaTeXML/Package/svjour.cls.ltxml' 'blib/lib/LaTeXML/Package/svjour.cls.ltxml' \
	  'lib/LaTeXML/Package/svjour3.cls.ltxml' 'blib/lib/LaTeXML/Package/svjour3.cls.ltxml' \
	  'lib/LaTeXML/Package/svmult.cls.ltxml' 'blib/lib/LaTeXML/Package/svmult.cls.ltxml' \
	  'lib/LaTeXML/Package/t1.fontmap.ltxml' 'blib/lib/LaTeXML/Package/t1.fontmap.ltxml' \
	  'lib/LaTeXML/Package/t1enc.def.ltxml' 'blib/lib/LaTeXML/Package/t1enc.def.ltxml' \
	  'lib/LaTeXML/Package/t1enc.sty.ltxml' 'blib/lib/LaTeXML/Package/t1enc.sty.ltxml' \
	  'lib/LaTeXML/Package/t2a.fontmap.ltxml' 'blib/lib/LaTeXML/Package/t2a.fontmap.ltxml' \
	  'lib/LaTeXML/Package/t2b.fontmap.ltxml' 'blib/lib/LaTeXML/Package/t2b.fontmap.ltxml' \
	  'lib/LaTeXML/Package/t2c.fontmap.ltxml' 'blib/lib/LaTeXML/Package/t2c.fontmap.ltxml' \
	  'lib/LaTeXML/Package/tablefootnote.sty.ltxml' 'blib/lib/LaTeXML/Package/tablefootnote.sty.ltxml' \
	  'lib/LaTeXML/Package/tabularx.sty.ltxml' 'blib/lib/LaTeXML/Package/tabularx.sty.ltxml' \
	  'lib/LaTeXML/Package/tabulary.sty.ltxml' 'blib/lib/LaTeXML/Package/tabulary.sty.ltxml' \
	  'lib/LaTeXML/Package/tcilatex.tex.ltxml' 'blib/lib/LaTeXML/Package/tcilatex.tex.ltxml' \
	  'lib/LaTeXML/Package/tcolorbox.sty.ltxml' 'blib/lib/LaTeXML/Package/tcolorbox.sty.ltxml' \
	  'lib/LaTeXML/Package/textcase.sty.ltxml' 'blib/lib/LaTeXML/Package/textcase.sty.ltxml' \
	  'lib/LaTeXML/Package/textcomp.sty.ltxml' 'blib/lib/LaTeXML/Package/textcomp.sty.ltxml' \
	  'lib/LaTeXML/Package/texvc.sty.ltxml' 'blib/lib/LaTeXML/Package/texvc.sty.ltxml' \
	  'lib/LaTeXML/Package/theorem.sty.ltxml' 'blib/lib/LaTeXML/Package/theorem.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/thm-restate.sty.ltxml' 'blib/lib/LaTeXML/Package/thm-restate.sty.ltxml' \
	  'lib/LaTeXML/Package/thmtools.sty.ltxml' 'blib/lib/LaTeXML/Package/thmtools.sty.ltxml' \
	  'lib/LaTeXML/Package/threeparttable.sty.ltxml' 'blib/lib/LaTeXML/Package/threeparttable.sty.ltxml' \
	  'lib/LaTeXML/Package/tikz-3dplot.sty.ltxml' 'blib/lib/LaTeXML/Package/tikz-3dplot.sty.ltxml' \
	  'lib/LaTeXML/Package/tikz.sty.ltxml' 'blib/lib/LaTeXML/Package/tikz.sty.ltxml' \
	  'lib/LaTeXML/Package/tikzbricks.sty.ltxml' 'blib/lib/LaTeXML/Package/tikzbricks.sty.ltxml' \
	  'lib/LaTeXML/Package/times.sty.ltxml' 'blib/lib/LaTeXML/Package/times.sty.ltxml' \
	  'lib/LaTeXML/Package/titlesec.sty.ltxml' 'blib/lib/LaTeXML/Package/titlesec.sty.ltxml' \
	  'lib/LaTeXML/Package/titling.sty.ltxml' 'blib/lib/LaTeXML/Package/titling.sty.ltxml' \
	  'lib/LaTeXML/Package/tocbibind.sty.ltxml' 'blib/lib/LaTeXML/Package/tocbibind.sty.ltxml' \
	  'lib/LaTeXML/Package/todonotes.sty.ltxml' 'blib/lib/LaTeXML/Package/todonotes.sty.ltxml' \
	  'lib/LaTeXML/Package/tracefnt.sty.ltxml' 'blib/lib/LaTeXML/Package/tracefnt.sty.ltxml' \
	  'lib/LaTeXML/Package/transparent.sty.ltxml' 'blib/lib/LaTeXML/Package/transparent.sty.ltxml' \
	  'lib/LaTeXML/Package/ts1.fontmap.ltxml' 'blib/lib/LaTeXML/Package/ts1.fontmap.ltxml' \
	  'lib/LaTeXML/Package/turing.sty.ltxml' 'blib/lib/LaTeXML/Package/turing.sty.ltxml' \
	  'lib/LaTeXML/Package/twoopt.sty.ltxml' 'blib/lib/LaTeXML/Package/twoopt.sty.ltxml' \
	  'lib/LaTeXML/Package/txfonts.sty.ltxml' 'blib/lib/LaTeXML/Package/txfonts.sty.ltxml' \
	  'lib/LaTeXML/Package/txtbabel.def.ltxml' 'blib/lib/LaTeXML/Package/txtbabel.def.ltxml' \
	  'lib/LaTeXML/Package/type1cm.sty.ltxml' 'blib/lib/LaTeXML/Package/type1cm.sty.ltxml' \
	  'lib/LaTeXML/Package/ulem.sty.ltxml' 'blib/lib/LaTeXML/Package/ulem.sty.ltxml' \
	  'lib/LaTeXML/Package/underscore.sty.ltxml' 'blib/lib/LaTeXML/Package/underscore.sty.ltxml' \
	  'lib/LaTeXML/Package/undertilde.sty.ltxml' 'blib/lib/LaTeXML/Package/undertilde.sty.ltxml' \
	  'lib/LaTeXML/Package/units.sty.ltxml' 'blib/lib/LaTeXML/Package/units.sty.ltxml' \
	  'lib/LaTeXML/Package/upgreek.sty.ltxml' 'blib/lib/LaTeXML/Package/upgreek.sty.ltxml' \
	  'lib/LaTeXML/Package/upquote.sty.ltxml' 'blib/lib/LaTeXML/Package/upquote.sty.ltxml' \
	  'lib/LaTeXML/Package/upref.sty.ltxml' 'blib/lib/LaTeXML/Package/upref.sty.ltxml' \
	  'lib/LaTeXML/Package/url.sty.ltxml' 'blib/lib/LaTeXML/Package/url.sty.ltxml' \
	  'lib/LaTeXML/Package/utf8.def.ltxml' 'blib/lib/LaTeXML/Package/utf8.def.ltxml' \
	  'lib/LaTeXML/Package/utf8x.def.ltxml' 'blib/lib/LaTeXML/Package/utf8x.def.ltxml' \
	  'lib/LaTeXML/Package/utopia.sty.ltxml' 'blib/lib/LaTeXML/Package/utopia.sty.ltxml' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Package/varioref.sty.ltxml' 'blib/lib/LaTeXML/Package/varioref.sty.ltxml' \
	  'lib/LaTeXML/Package/varwidth.sty.ltxml' 'blib/lib/LaTeXML/Package/varwidth.sty.ltxml' \
	  'lib/LaTeXML/Package/verbatim.sty.ltxml' 'blib/lib/LaTeXML/Package/verbatim.sty.ltxml' \
	  'lib/LaTeXML/Package/vmargin.sty.ltxml' 'blib/lib/LaTeXML/Package/vmargin.sty.ltxml' \
	  'lib/LaTeXML/Package/wasysym.sty.ltxml' 'blib/lib/LaTeXML/Package/wasysym.sty.ltxml' \
	  'lib/LaTeXML/Package/wiki.sty.ltxml' 'blib/lib/LaTeXML/Package/wiki.sty.ltxml' \
	  'lib/LaTeXML/Package/wrapfig.sty.ltxml' 'blib/lib/LaTeXML/Package/wrapfig.sty.ltxml' \
	  'lib/LaTeXML/Package/xargs.sty.ltxml' 'blib/lib/LaTeXML/Package/xargs.sty.ltxml' \
	  'lib/LaTeXML/Package/xcolor.sty.ltxml' 'blib/lib/LaTeXML/Package/xcolor.sty.ltxml' \
	  'lib/LaTeXML/Package/xfrac.sty.ltxml' 'blib/lib/LaTeXML/Package/xfrac.sty.ltxml' \
	  'lib/LaTeXML/Package/xkeyval.sty.ltxml' 'blib/lib/LaTeXML/Package/xkeyval.sty.ltxml' \
	  'lib/LaTeXML/Package/xkvview.sty.ltxml' 'blib/lib/LaTeXML/Package/xkvview.sty.ltxml' \
	  'lib/LaTeXML/Package/xparse.sty.ltxml' 'blib/lib/LaTeXML/Package/xparse.sty.ltxml' \
	  'lib/LaTeXML/Package/xspace.sty.ltxml' 'blib/lib/LaTeXML/Package/xspace.sty.ltxml' \
	  'lib/LaTeXML/Package/xunicode.sty.ltxml' 'blib/lib/LaTeXML/Package/xunicode.sty.ltxml' \
	  'lib/LaTeXML/Package/xurl.sty.ltxml' 'blib/lib/LaTeXML/Package/xurl.sty.ltxml' \
	  'lib/LaTeXML/Package/xy.sty.ltxml' 'blib/lib/LaTeXML/Package/xy.sty.ltxml' \
	  'lib/LaTeXML/Package/xy.tex.ltxml' 'blib/lib/LaTeXML/Package/xy.tex.ltxml' \
	  'lib/LaTeXML/Package/xylatexml.tex.ltxml' 'blib/lib/LaTeXML/Package/xylatexml.tex.ltxml' \
	  'lib/LaTeXML/Package/xypic.sty.ltxml' 'blib/lib/LaTeXML/Package/xypic.sty.ltxml' \
	  'lib/LaTeXML/Package/xypic.tex.ltxml' 'blib/lib/LaTeXML/Package/xypic.tex.ltxml' \
	  'lib/LaTeXML/Package/yfonts.sty.ltxml' 'blib/lib/LaTeXML/Package/yfonts.sty.ltxml' \
	  'lib/LaTeXML/Post.pm' 'blib/lib/LaTeXML/Post.pm' \
	  'lib/LaTeXML/Post/Collector.pm' 'blib/lib/LaTeXML/Post/Collector.pm' \
	  'lib/LaTeXML/Post/CrossRef.pm' 'blib/lib/LaTeXML/Post/CrossRef.pm' \
	  'lib/LaTeXML/Post/Graphics.pm' 'blib/lib/LaTeXML/Post/Graphics.pm' \
	  'lib/LaTeXML/Post/LaTeXImages.pm' 'blib/lib/LaTeXML/Post/LaTeXImages.pm' \
	  'lib/LaTeXML/Post/LexMath.pm' 'blib/lib/LaTeXML/Post/LexMath.pm' \
	  'lib/LaTeXML/Post/MakeBibliography.pm' 'blib/lib/LaTeXML/Post/MakeBibliography.pm' \
	  'lib/LaTeXML/Post/MakeIndex.pm' 'blib/lib/LaTeXML/Post/MakeIndex.pm' \
	  'lib/LaTeXML/Post/Manifest.pm' 'blib/lib/LaTeXML/Post/Manifest.pm' \
	  'lib/LaTeXML/Post/Manifest/Epub.pm' 'blib/lib/LaTeXML/Post/Manifest/Epub.pm' \
	  'lib/LaTeXML/Post/MathImages.pm' 'blib/lib/LaTeXML/Post/MathImages.pm' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/Post/MathML.pm' 'blib/lib/LaTeXML/Post/MathML.pm' \
	  'lib/LaTeXML/Post/MathML/Content.pm' 'blib/lib/LaTeXML/Post/MathML/Content.pm' \
	  'lib/LaTeXML/Post/MathML/Linebreaker.pm' 'blib/lib/LaTeXML/Post/MathML/Linebreaker.pm' \
	  'lib/LaTeXML/Post/MathML/OperatorDictionary.pm' 'blib/lib/LaTeXML/Post/MathML/OperatorDictionary.pm' \
	  'lib/LaTeXML/Post/MathML/Presentation.pm' 'blib/lib/LaTeXML/Post/MathML/Presentation.pm' \
	  'lib/LaTeXML/Post/OpenMath.pm' 'blib/lib/LaTeXML/Post/OpenMath.pm' \
	  'lib/LaTeXML/Post/PictureImages.pm' 'blib/lib/LaTeXML/Post/PictureImages.pm' \
	  'lib/LaTeXML/Post/SVG.pm' 'blib/lib/LaTeXML/Post/SVG.pm' \
	  'lib/LaTeXML/Post/Scan.pm' 'blib/lib/LaTeXML/Post/Scan.pm' \
	  'lib/LaTeXML/Post/Split.pm' 'blib/lib/LaTeXML/Post/Split.pm' \
	  'lib/LaTeXML/Post/TeXMath.pm' 'blib/lib/LaTeXML/Post/TeXMath.pm' \
	  'lib/LaTeXML/Post/UnicodeMath.pm' 'blib/lib/LaTeXML/Post/UnicodeMath.pm' \
	  'lib/LaTeXML/Post/Writer.pm' 'blib/lib/LaTeXML/Post/Writer.pm' \
	  'lib/LaTeXML/Post/XMath.pm' 'blib/lib/LaTeXML/Post/XMath.pm' \
	  'lib/LaTeXML/Post/XSLT.pm' 'blib/lib/LaTeXML/Post/XSLT.pm' \
	  'lib/LaTeXML/Pre/BibTeX.pm' 'blib/lib/LaTeXML/Pre/BibTeX.pm' \
	  'lib/LaTeXML/Pre/BibTeX/Entry.pm' 'blib/lib/LaTeXML/Pre/BibTeX/Entry.pm' \
	  'lib/LaTeXML/Util/Geometry.pm' 'blib/lib/LaTeXML/Util/Geometry.pm' \
	  'lib/LaTeXML/Util/Image.pm' 'blib/lib/LaTeXML/Util/Image.pm' \
	  'lib/LaTeXML/Util/ObjectDB.pm' 'blib/lib/LaTeXML/Util/ObjectDB.pm' \
	  'lib/LaTeXML/Util/ObjectDB/Entry.pm' 'blib/lib/LaTeXML/Util/ObjectDB/Entry.pm' \
	  'lib/LaTeXML/Util/Pack.pm' 'blib/lib/LaTeXML/Util/Pack.pm' \
	  'lib/LaTeXML/Util/Pathname.pm' 'blib/lib/LaTeXML/Util/Pathname.pm' \
	  'lib/LaTeXML/Util/Radix.pm' 'blib/lib/LaTeXML/Util/Radix.pm' \
	  'lib/LaTeXML/Util/Test.pm' 'blib/lib/LaTeXML/Util/Test.pm' \
	  'lib/LaTeXML/Util/Transform.pm' 'blib/lib/LaTeXML/Util/Transform.pm' \
	  'lib/LaTeXML/Util/Unicode.pm' 'blib/lib/LaTeXML/Util/Unicode.pm' \
	  'lib/LaTeXML/Util/WWW.pm' 'blib/lib/LaTeXML/Util/WWW.pm' \
	  'lib/LaTeXML/resources/CSS/LaTeXML-blue.css' 'blib/lib/LaTeXML/resources/CSS/LaTeXML-blue.css' \
	  'lib/LaTeXML/resources/CSS/LaTeXML-epub.css' 'blib/lib/LaTeXML/resources/CSS/LaTeXML-epub.css' \
	  'lib/LaTeXML/resources/CSS/LaTeXML-marginpar.css' 'blib/lib/LaTeXML/resources/CSS/LaTeXML-marginpar.css' \
	  'lib/LaTeXML/resources/CSS/LaTeXML-navbar-left.css' 'blib/lib/LaTeXML/resources/CSS/LaTeXML-navbar-left.css' \
	  'lib/LaTeXML/resources/CSS/LaTeXML-navbar-right.css' 'blib/lib/LaTeXML/resources/CSS/LaTeXML-navbar-right.css' \
	  'lib/LaTeXML/resources/CSS/LaTeXML.css' 'blib/lib/LaTeXML/resources/CSS/LaTeXML.css' \
	  'lib/LaTeXML/resources/CSS/ltx-amsart.css' 'blib/lib/LaTeXML/resources/CSS/ltx-amsart.css' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/resources/CSS/ltx-apj.css' 'blib/lib/LaTeXML/resources/CSS/ltx-apj.css' \
	  'lib/LaTeXML/resources/CSS/ltx-article.css' 'blib/lib/LaTeXML/resources/CSS/ltx-article.css' \
	  'lib/LaTeXML/resources/CSS/ltx-book.css' 'blib/lib/LaTeXML/resources/CSS/ltx-book.css' \
	  'lib/LaTeXML/resources/CSS/ltx-cv.css' 'blib/lib/LaTeXML/resources/CSS/ltx-cv.css' \
	  'lib/LaTeXML/resources/CSS/ltx-listings.css' 'blib/lib/LaTeXML/resources/CSS/ltx-listings.css' \
	  'lib/LaTeXML/resources/CSS/ltx-report.css' 'blib/lib/LaTeXML/resources/CSS/ltx-report.css' \
	  'lib/LaTeXML/resources/CSS/ltx-svjour.css' 'blib/lib/LaTeXML/resources/CSS/ltx-svjour.css' \
	  'lib/LaTeXML/resources/CSS/ltx-ulem.css' 'blib/lib/LaTeXML/resources/CSS/ltx-ulem.css' \
	  'lib/LaTeXML/resources/Profiles/fragment-html.opt' 'blib/lib/LaTeXML/resources/Profiles/fragment-html.opt' \
	  'lib/LaTeXML/resources/Profiles/fragment-xhtml.opt' 'blib/lib/LaTeXML/resources/Profiles/fragment-xhtml.opt' \
	  'lib/LaTeXML/resources/Profiles/fragment.opt' 'blib/lib/LaTeXML/resources/Profiles/fragment.opt' \
	  'lib/LaTeXML/resources/Profiles/math.opt' 'blib/lib/LaTeXML/resources/Profiles/math.opt' \
	  'lib/LaTeXML/resources/Profiles/modern.opt' 'blib/lib/LaTeXML/resources/Profiles/modern.opt' \
	  'lib/LaTeXML/resources/Profiles/standard.opt' 'blib/lib/LaTeXML/resources/Profiles/standard.opt' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-bib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-bib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-bib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-bib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-block.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-block.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-block.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-block.rng' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-common.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-common.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-common.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-common.rng' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-inline.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-inline.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-inline.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-inline.rng' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-math.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-math.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-math.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-math.rng' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-meta.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-meta.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-meta.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-meta.rng' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-misc.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-misc.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-misc.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-misc.rng' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-para.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-para.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-para.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-para.rng' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-picture.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-picture.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-picture.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-picture.rng' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-structure.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-structure.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-structure.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-structure.rng' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-tabular.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-tabular.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML-tabular.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML-tabular.rng' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML.model' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML.model' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/LaTeXML.rng' 'blib/lib/LaTeXML/resources/RelaxNG/LaTeXML.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-animation.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-animation.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-animation.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-animation.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-animevents-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-animevents-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-animevents-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-animevents-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-clip.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-clip.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-clip.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-clip.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-filter.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-filter.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-filter.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-filter.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-font.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-font.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-font.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-font.rng' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-graphics-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-graphics-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-graphics-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-graphics-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-structure.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-structure.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-structure.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-structure.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-text.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-text.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-basic-text.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-basic-text.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-clip.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-clip.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-clip.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-clip.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-conditional.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-conditional.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-conditional.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-conditional.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-container-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-container-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-container-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-container-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-core-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-core-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-core-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-core-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-cursor.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-cursor.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-cursor.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-cursor.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-datatypes.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-datatypes.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-datatypes.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-datatypes.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-docevents-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-docevents-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-docevents-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-docevents-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-extensibility.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-extensibility.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-extensibility.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-extensibility.rng' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-extresources-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-extresources-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-extresources-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-extresources-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-filter.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-filter.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-filter.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-filter.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-font.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-font.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-font.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-font.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-gradient.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-gradient.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-gradient.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-gradient.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-graphevents-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-graphevents-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-graphevents-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-graphevents-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-graphics-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-graphics-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-graphics-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-graphics-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-hyperlink.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-hyperlink.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-hyperlink.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-hyperlink.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-image.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-image.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-image.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-image.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-marker.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-marker.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-marker.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-marker.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-mask.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-mask.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-mask.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-mask.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-opacity-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-opacity-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-opacity-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-opacity-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-paint-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-paint-attrib.rnc' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-paint-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-paint-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-pattern.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-pattern.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-pattern.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-pattern.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-profile.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-profile.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-profile.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-profile.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-script.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-script.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-script.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-script.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-shape.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-shape.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-shape.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-shape.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-structure.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-structure.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-structure.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-structure.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-style.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-style.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-style.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-style.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-text.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-text.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-text.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-text.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-view.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-view.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-view.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-view.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-viewport-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-viewport-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-viewport-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-viewport-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-xlink-attrib.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-xlink-attrib.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg-xlink-attrib.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg-xlink-attrib.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg11-inc.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg11-inc.rnc' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg11-inc.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg11-inc.rng' \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg11.rnc' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg11.rnc' 
	$(NOECHO) $(ABSPERLRUN) -MExtUtils::Install -e 'pm_to_blib({@ARGV}, '\''$(INST_LIB)/auto'\'', q[$(PM_FILTER)], '\''$(PERM_DIR)'\'')' -- \
	  'lib/LaTeXML/resources/RelaxNG/svg/svg11.rng' 'blib/lib/LaTeXML/resources/RelaxNG/svg/svg11.rng' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-all-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-all-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-bib-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-bib-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-block-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-block-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-common.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-common.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-epub3.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-epub3.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-html4.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-html4.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-html5.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-html5.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-inline-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-inline-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-jats.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-jats.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-math-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-math-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-meta-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-meta-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-misc-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-misc-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-para-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-para-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-picture-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-picture-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-structure-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-structure-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-tabular-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-tabular-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-tei.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-tei.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-webpage-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-webpage-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-xhtml.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-xhtml.xsl' \
	  'lib/LaTeXML/resources/XSLT/LaTeXML-xhtml5.xsl' 'blib/lib/LaTeXML/resources/XSLT/LaTeXML-xhtml5.xsl' \
	  'lib/LaTeXML/resources/javascript/LaTeXML-maybeMathjax.js' 'blib/lib/LaTeXML/resources/javascript/LaTeXML-maybeMathjax.js' \
	  'lib/LaTeXML/texmf/latexml.sty' 'blib/lib/LaTeXML/texmf/latexml.sty' \
	  'lib/LaTeXML/texmf/lxRDFa.sty' 'blib/lib/LaTeXML/texmf/lxRDFa.sty' 
	$(NOECHO) $(TOUCH) pm_to_blib


# --- MakeMaker selfdocument section:

# here so even if top_targets is overridden, these will still be defined
# gmake will silently still work if any are .PHONY-ed but nmake won't

static ::
	$(NOECHO) $(NOOP)

dynamic ::
	$(NOECHO) $(NOOP)

config ::
	$(NOECHO) $(NOOP)


# --- MakeMaker postamble section:

# Always set revision if version module template is newer

pure_all :: $(REVISION_FILE)

$(REVISION_FILE): lib/LaTeXML/Version.in
	$(NOECHO) $(MKPATH) $(INST_LIBDIR)/LaTeXML
	$(RECORD_REVISION) lib/LaTeXML/Version.in > $(REVISION_FILE)


# Precompile the (Recursive Descent) MathGrammar
pure_all :: $(INST_LIBDIR)/LaTeXML/MathGrammar.pm

$(INST_LIBDIR)/LaTeXML/MathGrammar.pm: lib/LaTeXML/MathGrammar
	$(PERLRUN) -MParse::RecDescent - lib/LaTeXML/MathGrammar LaTeXML::MathGrammar Parse::RecDescent
	@$(PERLRUN) -e "exit(1) unless -e 'MathGrammar.pm';" || \
		(echo "Parse::RecDescent failed to created parser, trying to use old implementation. " && \
		$(PERLRUN) -MParse::RecDescent - lib/LaTeXML/MathGrammar LaTeXML::MathGrammar)
	$(NOECHO) $(MKPATH) $(INST_LIBDIR)/LaTeXML
	$(MV) MathGrammar.pm blib/lib/LaTeXML/MathGrammar.pm

pure_install ::
	$(NOECHO) (($(PERLRUN) -e "exit(1) unless shift;" -- "$(INSTALLTEXMFBASEDIR)") && \
	$(MKPATH) "$(DESTINSTALLTEXMFDIR)" && \
	$(MOD_INSTALL) \
		read "$(INSTALLTEXMFDIR)/.packlist" \
		write "$(DESTINSTALLTEXMFDIR)/.packlist" \
		"$(INST_TEXMFDIR)" "$(DESTINSTALLTEXMFDIR)" ) \
	||   echo "No TeX installation, skipping installing LaTeXML TeX packages"

uninstall ::
	$(NOECHO) (($(PERLRUN) -e "exit(1) unless -w shift;" -- "$(DESTINSTALLTEXMFBASEDIR)") && \
		$(UNINSTALL) "$(INSTALLTEXMFDIR)/.packlist") \
	|| echo "No write permission for $(INSTALLTEXMFBASEDIR), skipping uninstalling LaTeXML TeX packages"

pure_install ::
	$(NOECHO) ($(PERLRUN) -e "exit(1) if -w shift;" -- "$(INSTALLTEXMFBASEDIR)" || mktexlsr) \
	||   echo "No write permission for $(INSTALLTEXMFBASEDIR), skipping mktexlsr"

uninstall ::
	$(NOECHO) ($(PERLRUN) -e "exit(1) if -w shift;" -- "$(INSTALLTEXMFBASEDIR)" || mktexlsr) \
	||   echo "No write permission for $(INSTALLTEXMFBASEDIR), skipping mktexlsr"


EXTRA_TEST_FILES = t/*.tt

fulltest : test extratest

extratest ::
	PERL_DL_NONLAZY=1 $(FULLPERLRUN) "-MExtUtils::Command::MM" "-e" "test_harness($(TEST_VERBOSE), '$(INST_LIB)', '$(INST_ARCHLIB)')" $(EXTRA_TEST_FILES)



# End.
