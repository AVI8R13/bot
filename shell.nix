#shell-nix
#for use with nix-os

let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      # select Python packages here
      python-pkgs.discordpy
      python-pkgs.qrcode
      python-pkgs.aiohttp
      python-pkgs.ping3
      python-pkgs.requests
    ]))
  ];
}
