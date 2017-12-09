# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2017-12-09
## Changed
- Options are now passed as a dictionary.

## [0.3.0] - 2017-09-29
### Added
- Identify some elements during tokenization. This cover some cases where some keywords are separated by uncommon delimiters or no delimiters at all creating tokens that doesn't match with any keyword.

### Fixed
- Remove accents from strings before trying to match it with a keyword.

## [0.2.0] - 2017-09-19
### Added
- Parse alternative episode numbers.

### Fixed
- Fix a bug where passing some special characters to the allowed delimiters may result in regex parsing strings incorrectly.
- Ignored strings option is now working.

## [0.1.1] - 2017-09-18
### Fixed
- Expose the `Options` class through the `__init__.py`.

## 0.1.0 - 2017-09-17
### Added
- Working parser for the majority of anime filenames.

[Unreleased]: https://github.com/igorcmoura/anitopy/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/igorcmoura/anitopy/compare/v0.3.0...v1.0.0
[0.3.0]: https://github.com/igorcmoura/anitopy/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/igorcmoura/anitopy/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/igorcmoura/anitopy/compare/v0.1.0...v0.1.1
