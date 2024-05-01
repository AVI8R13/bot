#nix-shell
#for use with nixOS, ignore if sing a differant operating system

let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    pkgs.python312
    (pkgs.python312.withPackages (ps: with ps; [
      qrcode
      aiohttp
      ping3
      requests
      discordpy
    ]))
  ];
}