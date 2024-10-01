{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    nativeBuildInputs = with pkgs.buildPackages; [ python312 python312Packages.grpcio python312Packages.grpcio-tools ];
}