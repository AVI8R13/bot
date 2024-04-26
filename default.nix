with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "my-project-env";
  buildInputs = [
    (python3.withPackages (python-pkgs: [
      python-pkgs.discordpy
      python-pkgs.qrcode
      python-pkgs.aiohttp
      python-pkgs.ping3
      python-pkgs.requests
    ]))
  ];
}