# Validation scope

Run checks from the repository root:

```sh
python tools/validate-package.py
python tools/test-package-validator.py
python -m pip install Pillow
python tools/test-image-transport.py
```

The structural validator checks the 32-skill inventory, frontmatter, workflow dependencies, review policy, profile paths, local Markdown links, and untranslated Cyrillic text. Its Markdown and YAML parsers are deliberately limited; it does not resolve remote URLs or prove the meaning of an instruction.

Validator regression tests use isolated copies to exercise portable installation and rejection of invalid contracts. Image tests exercise actual local files, including whole-frame preservation, alpha, hashes, preparation budgets, repeatability, and path boundaries. The image helper performs no network calls.

GitHub Actions runs these checks on Windows and Linux with Python 3.10 and 3.12. A successful run establishes only the tested package properties. It does not prove game quality, runtime correctness, accessibility compliance, production capacity, or readiness of a specific game.
