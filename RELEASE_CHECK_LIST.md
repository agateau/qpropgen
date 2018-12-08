Update CHANGELOG.md:

    r!git log --pretty=format:'- \%s (\%an)' x.y.z-1..HEAD

Bump version number in qpropgen/__init__.py

Commit

Create tarball:

    ./setup.py sdist

Install tarball in virtual env:

    pew mktmpenv
    cd /tmp
    tar xf path/to/qpropgen/dists/qpropgen-$version.tar.gz
    cd qpropgen-$version
    ./setup.py install

Run functional tests:

    ./tests.sh

    exit

If OK, create "x.y.z" tag:

    git tag -a x.y.z

Push:

    git push
    git push --tags

Publish on PyPI:

    Check the content of qpropgen.egg-info/PKG-INFO

    twine upload dist/qpropgen-$version.tar.gz

Update project page

Blog
