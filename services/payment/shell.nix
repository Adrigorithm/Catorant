{ pkgs ? import <nixpkgs> {} }:

let
  lib = pkgs.lib;
  vscodeExtensions = [
    "ms-python.python"
    "ms-python.vscode-pylance"
    "ms-python.debugpy"
  ];
in
pkgs.mkShell {
  nativeBuildInputs = with pkgs.buildPackages; [ python312 python312Packages.grpcio python312Packages.grpcio-tools ];
  
  shellHook = ''
    for ext in ${lib.concatStringsSep " " vscodeExtensions}; do
      code --install-extension $ext || true
    done
  '';
}
