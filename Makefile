VERSION=1.08

buildhost:
	docker run -h yadm-buildhost --rm -it -v "$$PWD:/home/tbyrne/yadm-rpm" -v "$$HOME/.buildhost:/home/tbyrne" yadm/buildhost:latest su - tbyrne

tarball:
	curl -fLO 'https://github.com/TheLocehiliosan/yadm/archive/${VERSION}.tar.gz#/yadm-${VERSION}.tar.gz'
