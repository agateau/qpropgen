git checkout dev

Update CHANGELOG.md:

    r!git log --pretty=format:'- \%s (\%an)' x.y.z-1..HEAD

Bump version number in qpropgen/__init__.py

Check/update README.md

Commit

Package and run tests

    tox --recreate --skip-missing-interpreters

Check the content of qpropgen.egg-info/PKG-INFO.

Push

    git push

If Travis is happy:

    git checkout master
    git pull
    git merge origin/dev

    ./setup.py sdist
    version=$(./setup.py --version)
    git tag -a $version -m "Releasing $version"
    git push
    git push --tags
    twine upload dist/qpropgen-$version.tar.gz

Update project page

Blog
