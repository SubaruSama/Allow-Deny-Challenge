# BUG 1 - Invalid check of domain

Invalid check on structure of domain.

## Steps to reproduce

Using CLI enter an URL with invalid domain, such as ```test```. Ex: python -m bouncer.main --add-allowlist test

## Current

It adds the URL with invalid domain and adds the default scheme.

## Exptected

Given the URL ```test```, it should return an exception and close the program.
