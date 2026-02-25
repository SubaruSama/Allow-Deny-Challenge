# BUG 1 - Invalid insertion of URL with no valid domain and valid scheme

The bouncer adds the URL if the scheme is present and valid (http://, https:// or ftp://).

## Steps to reproduce

Using CLI enter an URL with invalid domain, such as ```test```. Ex: python -m bouncer.main --add-allowlist http://test

## Current

It adds the URL with invalid domain and the default scheme.

## Exptected

Given the URL ```http://test```, it should return an exception and close the program.
