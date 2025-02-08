@echo off
set SPHINXBUILD=sphinx-build
set SOURCEDIR=.
set BUILDDIR=_build

%SPHINXBUILD% -b html %SOURCEDIR% %BUILDDIR%/html
echo.
echo Build fertig. Die HTML-Dateien befinden sich in %BUILDDIR%/html.
pause
