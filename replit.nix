{pkgs}: {
  deps = [
    pkgs.ccache
    pkgs.zlib
    pkgs.pkg-config
    pkgs.libtool
    pkgs.automake
    pkgs.autoconf
    pkgs.which
    pkgs.git
    pkgs.unzip
    pkgs.zip
    pkgs.openjdk17
  ];
}
