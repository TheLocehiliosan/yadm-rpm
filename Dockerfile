FROM fedora:latest
MAINTAINER Tim Byrne <sultan@locehilios.com>
RUN dnf install -y fedora-packager bats expect git gnupg hostname
RUN useradd tbyrne && usermod -a -G mock tbyrne
