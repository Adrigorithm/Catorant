{ pkgs ? import <nixpkgs> {} }:

let
  lib = pkgs.lib;
  vscodeExtensions = [
    "golang.Go"
  ];
in
pkgs.mkShell {
  nativeBuildInputs = with pkgs.buildPackages; [ go gopls ];
  
  shellHook = ''
    for ext in ${lib.concatStringsSep " " vscodeExtensions}; do
      code --install-extension $ext || true
    done
  '';
}
